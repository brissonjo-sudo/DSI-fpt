"""Tests logiciels du lanceur : CLI simulées, aucun appel ni score réel du skill."""

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import eval_suite
import mesure_locale as mesure


class CampagneLocale(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.prepared = self.root / "prepare"
        eval_suite.prepare_run(self.prepared, "modèle factice de test", "juge factice de test")
        self.kit = self.root / "kit"
        self.archive = mesure.export_kit(self.kit, self.prepared)
        self.calls = []
        self.fail_judge = False

    def fake_cli(self, cmd, **kwargs):
        if cmd[-1] == "--version":
            return subprocess.CompletedProcess(cmd, 0, "CLI factice 1.0\n", "")
        workspace = Path(kwargs["cwd"])
        payload = kwargs["input"]
        role = "juge" if "<attendus>" in payload else "respondant"
        files = [p.relative_to(workspace).as_posix() for p in workspace.rglob("*") if p.is_file()]
        self.calls.append({"role": role, "payload": payload, "files": files,
                           "workspace": str(workspace), "command": cmd})
        if role == "juge" and self.fail_judge:
            return subprocess.CompletedProcess(cmd, 1, "", "Échec simulé de test logiciel")
        response = (json.dumps({"verdict": "RÉUSSITE", "notes": "Jugement factice, test logiciel."}, ensure_ascii=False)
                    if role == "juge" else "Réponse factice, aucune mesure réelle du skill.")
        if cmd[0] == "codex":
            Path(cmd[cmd.index("--output-last-message") + 1]).write_text(response, encoding="utf-8")
            stdout = json.dumps({"type": "item.completed", "item": {"type": "agent_message", "text": response}}) + "\n"
        else:
            stdout = json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": response}) + "\n"
        return subprocess.CompletedProcess(cmd, 0, stdout, "")

    def launch(self, engine="claude", responder="modèle factice", cases=None, dry=False):
        with patch.object(mesure.shutil, "which", return_value="/cli-factice"), \
             patch.object(mesure.subprocess, "run", side_effect=self.fake_cli), \
             contextlib.redirect_stdout(io.StringIO()):
            mesure.launch(self.kit, engine, responder, "juge factice", False,
                          ["cas-21"] if cases is None else cases, dry)

    def test_entrees_separees_et_dossiers_neufs(self):
        case = dict(mesure.verify_kit(self.kit)[20])
        case["attendus"] = ["ATTENDU-CANARI-INTERDIT-AU-REPONDANT"]
        self.assertNotIn(case["attendus"][0], mesure.input_for(self.kit, case, "respondant", "claude"))
        self.launch()
        respondent, judge = self.calls
        self.assertEqual(len(respondent["files"]), 30)
        self.assertTrue(all(p.startswith(".claude/skills/dsi-fpt/") for p in respondent["files"]))
        self.assertEqual(judge["files"], [])
        self.assertNotIn("<entree_skill>", judge["payload"])
        self.assertIn("<attendus>", judge["payload"])
        self.assertNotEqual(respondent["workspace"], judge["workspace"])
        self.assertTrue(all(not Path(c["workspace"]).exists() for c in self.calls))
        self.assertIn("--restricted", respondent["command"])
        self.assertEqual(judge["command"][judge["command"].index("--tools") + 1], "")
        self.assertFalse((self.kit / "resultats" / "summary.json").exists())

    def test_reprise_apres_echec_ne_rejoue_pas_reponse(self):
        self.fail_judge = True
        with self.assertRaisesRegex(ValueError, "CLI code"):
            self.launch()
        self.assertTrue((self.kit / "resultats" / "cas-21" / "response.md").exists())
        self.assertFalse((self.kit / "resultats" / "cas-21" / "judgment.json").exists())
        self.fail_judge = False
        self.launch()
        self.assertEqual([c["role"] for c in self.calls], ["respondant", "juge", "juge"])
        self.launch()
        self.assertEqual(len(self.calls), 3)

    def test_reprise_refuse_changement_modele(self):
        self.launch()
        with self.assertRaisesRegex(ValueError, "différents"):
            self.launch(responder="autre modèle factice")
        self.assertEqual(len(self.calls), 2)

    def test_reprise_refuse_reponse_modifiee(self):
        self.launch()
        (self.kit / "resultats" / "cas-21" / "response.md").write_text("Réponse modifiée")
        with self.assertRaisesRegex(ValueError, "Preuve modifiée"):
            self.launch()
        self.assertEqual(len(self.calls), 2)

    def test_reprise_refuse_trace_modifiee(self):
        self.launch()
        (self.kit / "resultats" / "cas-21" / "juge-stdout.txt").write_text("Trace modifiée")
        with self.assertRaisesRegex(ValueError, "Preuve modifiée"):
            self.launch()

    def test_runtime_altere_refuse_avant_appel(self):
        (self.kit / "runtime" / "SKILL.md").write_text("Runtime altéré")
        with self.assertRaisesRegex(ValueError, "Runtime figé"):
            self.launch()
        self.assertEqual(self.calls, [])

    def test_lanceur_altere_refuse_avant_appel(self):
        (self.kit / "scripts" / "eval_suite.py").write_text("Lanceur altéré")
        with self.assertRaisesRegex(ValueError, "Lanceur altéré"):
            self.launch()
        self.assertEqual(self.calls, [])

    def test_export_necrase_pas_archive_existante(self):
        destination = self.root / "nouveau-kit"
        archive = Path(str(destination) + ".zip")
        archive.write_text("Archive à conserver")
        with self.assertRaisesRegex(ValueError, "Archive déjà existante"):
            mesure.export_kit(destination, self.prepared)
        self.assertEqual(archive.read_text(), "Archive à conserver")
        self.assertFalse(destination.exists())

    def test_nom_archive_conserve_version_complete(self):
        destination = self.root / "campagne-v0.2.0"
        archive = mesure.export_kit(destination, self.prepared)
        self.assertEqual(archive.name, "campagne-v0.2.0.zip")

    def test_dry_run_kit_autonome_sans_cli(self):
        # Le processus Python réel vérifie la portabilité ; aucune CLI modèle n'est exécutée.
        extracted = self.root / "extraction"
        with zipfile.ZipFile(self.archive) as archive:
            archive.extractall(extracted)
        standalone = extracted / "kit"
        result = subprocess.run([sys.executable, str(standalone / "scripts" / "mesure_locale.py"),
                                 "run", "--kit", str(standalone), "--engine", "claude",
                                 "--responder-model", "modèle factice", "--judge-model", "juge factice",
                                 "--dry-run"], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout)["appels"], 56)
        self.assertFalse((standalone / "resultats" / "execution.json").exists())
        self.assertFalse(list(standalone.glob("resultats/cas-*/response.md")))

    def test_codex_native_et_web_explicitement_desactive(self):
        self.launch(engine="codex")
        self.assertTrue(all(p.startswith(".agents/skills/dsi-fpt/") for p in self.calls[0]["files"]))
        self.assertEqual(self.calls[1]["files"], [])
        self.assertTrue(all('web_search="disabled"' in call["command"] for call in self.calls))
        judgment = mesure.load(self.kit / "resultats" / "cas-21" / "judgment.json")
        self.assertEqual(judgment["response_sha256"], mesure.digest(
            (self.kit / "resultats" / "cas-21" / "response.md").read_bytes()))

    def test_jugement_non_objet_ou_sans_notes_refuse(self):
        for invalid in ('[]', '{"verdict":"RÉUSSITE","notes":""}', '{"verdict":"inconnu","notes":"Test"}'):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                mesure.parse_judgment(invalid, b"Reponse factice")

    def test_erreur_claude_sans_resultat_success_refusee(self):
        with self.assertRaises(ValueError):
            mesure.response_text("claude", json.dumps({"type": "result", "subtype": "error_max_turns",
                                                       "is_error": True}), self.root)

    def test_complete_simulee_verifie_56_preuves_sans_publication(self):
        self.launch(cases=[])
        self.assertEqual(len(self.calls), 56)
        self.assertEqual(len({c["workspace"] for c in self.calls}), 56)
        summary = mesure.load(self.kit / "resultats" / "summary.json")
        self.assertEqual(summary["case_count"], 28)
        self.assertFalse(summary["publication_ready"])
        manifest = mesure.load(self.kit / "resultats" / "manifest.json")
        self.assertEqual(manifest["responder"], "claude : modèle factice")
        # Même avec un sous-ensemble, une synthèse refuse une preuve d'un autre cas altérée.
        (self.kit / "resultats" / "cas-01" / "respondant-stderr.txt").write_text("Altération")
        with self.assertRaisesRegex(ValueError, "Preuve modifiée"):
            self.launch(cases=["cas-28"])


if __name__ == "__main__":
    unittest.main()
