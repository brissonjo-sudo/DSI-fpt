"""Régressions : mesure incomplète, preuve altérée et exclusion du cache."""

import hashlib
import json
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import eval_suite
import package_skill
import validate_repo


class PreuvesMesure(unittest.TestCase):
    """Exerce des échecs qui pourraient attribuer un score trompeur."""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.run = Path(self.temporary.name) / "mesure"
        eval_suite.prepare_run(self.run, "modèle de test", "juge de test")

    def complete(self, critical_failure=False):
        for case in eval_suite.load_cases():
            directory = self.run / eval_suite.case_dir_name(case)
            response = directory / "response.md"
            response.write_text("Réponse factice de test logiciel, aucune mesure du skill.\n")
            judgment = {"verdict": "ÉCHEC" if critical_failure and case["id"] == "cas-21" else "RÉUSSITE",
                        "notes": "Artefact factice de test logiciel.",
                        "response_sha256": eval_suite.suite_digest(response)}
            (directory / "judgment.json").write_text(json.dumps(judgment))

    def test_campagne_preparee_ne_produit_pas_de_score(self):
        with self.assertRaisesRegex(ValueError, "Artefacts manquants"):
            eval_suite.validate_run(self.run)
        self.assertFalse((self.run / "summary.json").exists())

    def test_preparation_non_ecrasable(self):
        with self.assertRaises(ValueError):
            eval_suite.prepare_run(self.run, "autre", "autre")

    def test_suite_alteree_refusee(self):
        (self.run / "suite.json").write_text("[]")
        with self.assertRaisesRegex(ValueError, "empreinte"):
            eval_suite.validate_run(self.run)

    def test_bareme_altere_refuse(self):
        (self.run / "bareme.md").write_text("barème différent")
        with self.assertRaisesRegex(ValueError, "Barème"):
            eval_suite.validate_run(self.run)

    def test_prompt_altere_refuse(self):
        (self.run / "cas-01" / "prompt.md").write_text("autre prompt")
        with self.assertRaisesRegex(ValueError, "prompt altéré"):
            eval_suite.validate_run(self.run)

    def test_jugement_non_lie_refuse(self):
        self.complete()
        (self.run / "cas-01" / "response.md").write_text("réponse modifiée")
        with self.assertRaisesRegex(ValueError, "jugement non rattaché"):
            eval_suite.validate_run(self.run)

    def test_echec_critique_bloque_malgre_score_global(self):
        self.complete(critical_failure=True)
        totals = eval_suite.validate_run(self.run)
        summary = json.loads(eval_suite.write_summary(self.run, totals).read_text())
        self.assertEqual(summary["totals"]["RÉUSSITE"], 27)
        self.assertFalse(summary["threshold_passed"])
        self.assertEqual(summary["critical_failures"], ["cas-21"])

    def test_seuil_ne_remplace_pas_relecture_praticien(self):
        self.complete()
        summary = json.loads(eval_suite.write_summary(self.run, eval_suite.validate_run(self.run)).read_text())
        self.assertTrue(summary["threshold_passed"])
        self.assertFalse(summary["publication_ready"])


class Packaging(unittest.TestCase):
    def test_cache_et_conception_exclus(self):
        paths = {p.relative_to(package_skill.ROOT).as_posix() for p in package_skill.runtime_files()}
        self.assertIn("references/references-verifiees.md", paths)
        self.assertNotIn("references/cache-valeurs.md", paths)
        self.assertFalse(any(p.startswith(("tests/", "docs/", "vault/")) for p in paths))

    def test_destination_hors_depot_refusee(self):
        with self.assertRaises(ValueError):
            package_skill.checked_output("/tmp/dsi-fpt.zip", "0.2.0")

    def test_source_non_ecrasable(self):
        with self.assertRaises(ValueError):
            package_skill.checked_output("SKILL.md", "0.2.0")

    def test_determinisme_archive(self):
        with tempfile.TemporaryDirectory() as temporary:
            first, second = (Path(temporary) / name for name in ("a.zip", "b.zip"))
            package_skill.write_package(first)
            package_skill.write_package(second)
            self.assertEqual(hashlib.sha256(first.read_bytes()).digest(),
                             hashlib.sha256(second.read_bytes()).digest())


class ValeursInterdites(unittest.TestCase):
    """Vérifie le diagnostic du validateur sur de véritables fichiers runtime."""

    def inspecter(self, texte: str) -> list[str]:
        """Évalue un runtime minimal isolé et retourne les erreurs bloquantes."""
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "references").mkdir()
            (root / "references" / "securite-si.md").write_text(
                texte, encoding="utf-8")
            validation = validate_repo.Validation()
            with patch.object(validate_repo, "ROOT", root):
                validate_repo.validate_forbidden_content(validation)
            return validation.errors

    def test_titre_journalisation_ne_declenche_pas_un_delai(self) -> None:
        self.assertEqual(self.inspecter("### 5.9 Journalisation\n"), [])

    def test_delais_reels_restent_bloquants(self) -> None:
        for value in ("72 heures", "9 jours", "1 jour", "2 semaines",
                      "12 mois", "2 ans", "1 année", "3 h"):
            with self.subTest(value=value):
                self.assertTrue(any("délai chiffré" in error
                                    for error in self.inspecter(value)))


if __name__ == "__main__":
    unittest.main()
