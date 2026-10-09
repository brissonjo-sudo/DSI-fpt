"""Prépare des copies publiques du pilote PARTIEL, sans exécuter le smoke.

Sans --apply : prévalidation en lecture seule. Avec --apply : nouvelles copies
de preuves, README et état de qualification ; aucun runtime ni commande Git.
Le stdout développeur brut reste local ; seules six entrées plugin en dérivent.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from typing import Any
import zipfile

ROOT = Path(__file__).resolve().parent
RUN = ROOT / "qualification-coactivation-dev6-codex-r1"
PLUGIN = ROOT / "Collectivite-corrections-pr5"
DSI = ROOT / "DSI-corrections-pr5/docs/qualification/2026-10-07"
SMOKE = ROOT / "smoke-dev6-isole-20261007-211629-4dc9cd90"
PROOF = PLUGIN / "tests/evidence/coactivation-codex-dev6-PARTIEL"
DOC = DSI / "dev6-PARTIEL"
ARCHIVE = ROOT / "livrables/Preuves-coactivation-Codex-dev6-PARTIEL-2026-10-07.zip"
CONTROL = ROOT / "livrables/Controle-archive-Codex-dev6-PARTIEL-2026-10-07.json"
SOURCE = "3f0df285898cf1e36d1ddda8d85d0c4cd5e0903b"
CANDIDATE = "1a12b347448809864ba6d14d5501585a4a038206"
REJECTED = "plugin-garde-fou-apja"
EXPECTED = ("plugin-prime-depart-retraite", "plugin-violation-donnees",
            "plugin-dsi-reouverture", "plugin-spontane-budget",
            "plugin-spontane-reversibilite")
SMOKE_ROOT_FILES = (
    "smoke-dev6-faisabilite.md", "smoke-dev6-installation-addendum-2026-10-07.md",
    "smoke-dev6-installation-addendum-2026-10-07.json", "smoke-dev6-decouverte-2026-10-07.md",
    "smoke-dev6-isole.ps1", "observer-contexte-smoke-dev6.ps1",
    "controler-decouverte-smoke-dev6.py", "ouvrir-smoke-dev6.ps1",
    "statut-auth-smoke-dev6-2026-10-07.json",
)
SMOKE_RECEIPTS = ("installation.json", "discovery-verification.json", "prompt-input.execution.json")


def require(condition: bool, message: str) -> None:
    """Refuse explicitement une preuve absente ou une portée ambiguë."""
    if not condition:
        raise ValueError(message)


def sha(data: bytes) -> str:
    """Empreinte des octets, sans normalisation."""
    return hashlib.sha256(data).hexdigest()


def load(path: Path) -> dict[str, Any]:
    """Lit un objet JSON sans modifier sa pièce source."""
    result = json.loads(path.read_bytes())
    require(isinstance(result, dict), f"Objet JSON attendu : {path}")
    return result


def encoded(document: dict[str, Any]) -> bytes:
    """Encode les seules nouvelles pièces dérivées en UTF-8/LF."""
    return (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def safe_archive_name(name: str) -> PurePosixPath:
    """Vérifie un chemin relatif fermé avant extraction explicite."""
    path = PurePosixPath(name)
    require(bool(name) and not path.is_absolute() and "\\" not in name and ":" not in name,
            f"Chemin ZIP absolu ou ambigu : {name}")
    require(all(part not in ("", ".", "..") for part in name.split("/")), f"Chemin ZIP invalide : {name}")
    forbidden = {"auth.json", "config.toml", "codex-state", ".codex", "prompt-input.stdout.txt", "prompt-input.stderr.txt"}
    require(not forbidden.intersection(path.parts), f"État privé dans le ZIP : {name}")
    return path


def verified_archive() -> tuple[dict[str, bytes], dict[str, Any]]:
    """Rejoue CRC, liste exhaustive et SHA de chaque entrée du ZIP partiel."""
    control = load(CONTROL)
    require(control.get("scope") == "PARTIEL" and control.get("full_suite_complete") is False,
            "Contrôle ZIP de portée différente")
    require(control.get("archive_sha256") == sha(ARCHIVE.read_bytes()), "ZIP modifié")
    with zipfile.ZipFile(ARCHIVE) as package:
        names = package.namelist()
        require(len(names) == len(set(names)), "Entrées ZIP dupliquées")
        require(package.testzip() is None, "CRC ZIP incorrect")
        inventory = json.loads(package.read("inventory.json"))
        require(isinstance(inventory, dict) and set(names) == set(inventory) | {"inventory.json"},
                "Liste ZIP différente de l'inventaire")
        require(control.get("entry_count") == len(names), "Compte ZIP différent")
        files = {}
        for name in names:
            safe_archive_name(name)
            info = package.getinfo(name)
            require(not info.is_dir() and (info.external_attr >> 16) & 0o170000 != 0o120000,
                    f"Entrée ZIP spéciale : {name}")
            data = package.read(name)
            if name != "inventory.json":
                require(isinstance(inventory[name], str) and re.fullmatch(r"[0-9a-f]{64}", inventory[name]) is not None,
                        f"SHA invalide : {name}")
                require(sha(data) == inventory[name], f"Octets ZIP divergents : {name}")
            files[name] = data
    return files, control


def verified_partial(files: dict[str, bytes], control: dict[str, Any]) -> dict[str, Any]:
    """Exige cinq jugements, un rejet hors score et dix cas non exécutés."""
    for name in ("rapport-PARTIEL.md", "synthese-PARTIELLE.json", "audit-natif-PARTIEL-final.json"):
        require(files[name] == (RUN / name).read_bytes(), f"Source/ZIP différents : {name}")
    summary = json.loads(files["synthese-PARTIELLE.json"])
    audit = json.loads(files["audit-natif-PARTIEL-final.json"])
    expected = {"candidate_commit": CANDIDATE, "runtime_source_commit": SOURCE,
                "prepared_cases": 16, "executed_case_count": 6, "bound_respondent_count": 5,
                "judged_case_count": 5, "retained_unique_role_count": 10,
                "rejected_protocol_case_count": 1, "full_suite_complete": False,
                "historical_scores_reused": False, "actual_plugin_activation_verified": False,
                "release_ready": False, "total_observed_unique_roles_including_rejected": 11}
    for field, value in expected.items():
        require(summary.get(field) == value, f"Synthèse partielle incompatible : {field}")
    require(tuple(row["case_id"] for row in summary["results"]) == EXPECTED, "Cas jugés différents")
    require(len(summary["not_executed_cases"]) == len(set(summary["not_executed_cases"])) == 10,
            "Dix absences distinctes attendues")
    require(summary["rejected_protocol_cases"][0]["case_id"] == REJECTED, "Rejet différent")
    require(sum(summary["counts"].values()) == 5, "Comptes limités aux cinq jugements")
    require(sum(summary["atomic_results"].values()) == summary["effectively_judged_atomic_count"],
            "Compte atomique partiel divergent")
    require(audit.get("status") == "passed" and audit.get("require_complete") is False,
            "Audit partiel absent ou présenté comme complet")
    require((audit.get("respondents_verified"), audit.get("judges_verified"), audit.get("unique_retained_roles")) == (5, 5, 10),
            "Identités liées incompatibles")
    require([row["assessment"] for row in audit["judges"]] == summary["results"], "Jugements différents de l'audit")
    require(summary["native_audit_sha256"] == control["native_audit_sha256"] == sha(files["audit-natif-PARTIEL-final.json"]),
            "SHA audit divergent")
    for path in (PLUGIN / ".codex-plugin/plugin.json", PLUGIN / ".claude-plugin/plugin.json"):
        require(load(path)["version"] == "1.2.0-dev.6", "Version courante différente")
    return summary


def derived_plugin_catalogue() -> bytes:
    """Extrait seulement six entrées plugin du stdout conservé localement."""
    original = (SMOKE / "prompt-input.stdout.txt").read_bytes()
    execution = load(SMOKE / "prompt-input.execution.json")
    discovery = load(SMOKE / "discovery-verification.json")
    require(execution["exit_code"] == 0 and execution["completed_before_timeout"] is True, "Diagnostic incomplet")
    require(sha(original) == execution["stdout_sha256"] == discovery["stdout_sha256"], "Stdout local modifié")
    require(discovery["status"] == "passed" and discovery["plugin_skill_count"] == 6, "Découverte non confirmée")
    require(discovery["runtime_source_commit"] == SOURCE, "Source du diagnostic différente")
    installed = load(SMOKE / "installation.json")
    require(installed.get("installed") is True and installed.get("installed_manifest_version") == "1.2.0-dev.6",
            "Installation du candidat non confirmée")
    require(installed.get("candidate_commit") == SOURCE and
            (installed.get("installed_files_verified"), installed.get("runtime_files_verified")) == (214, 166),
            "Inventaire installé différent")
    require(discovery.get("actual_plugin_activation_verified") is False and discovery.get("inference_requested") is False,
            "Portée du diagnostic modifiée : examiner avant copie")
    status = load(ROOT / "statut-auth-smoke-dev6-2026-10-07.json")
    require(status.get("record_kind") == "root_observation_of_actual_cli_login_status" and
            status.get("safe_status") == "not_logged_in" and status.get("upstream_authentication_verified") is False,
            "Observation datée d'authentification différente")
    require(discovery["execution_receipt_sha256"] == sha((SMOKE / "prompt-input.execution.json").read_bytes()), "Reçu différent")
    texts = [piece["text"] for message in json.loads(original) for piece in message.get("content", [])
             if piece.get("type") == "input_text" and "<skills_instructions>" in piece.get("text", "")]
    require(len(texts) == 1, "Catalogue natif ambigu")
    text = texts[0]
    roots = re.findall(r"^- `r1` = `([^`]+)`$", text, re.M)
    require(len(roots) == 1, "Racine plugin ambiguë")
    matches = re.findall(r"^- collectivite-territoriale:([^:]+): (.*?) \(file: r1/([^/]+)/SKILL.md\)$", text, re.M)
    require(len(matches) == len({name for name, _, _ in matches}) == 6, "Six descriptions distinctes requises")
    proofs = {row["name"]: row for row in discovery["skills"]}
    rows = []
    for name, description, folder in matches:
        require(name == folder and name in proofs, "Entrée catalogue différente")
        proof = proofs[name]
        require(sha(description.encode("utf-8")) == proof["description_sha256"] and len(description) == proof["description_characters"],
                f"Description différente : {name}")
        installed = (Path(roots[0]) / folder / "SKILL.md").as_posix()
        require(installed == proof["installed_path"], f"Chemin plugin différent : {name}")
        rows.append({"name": name, "description": description, "installed_path": installed,
                     "description_sha256": proof["description_sha256"], "skill_sha256": proof["skill_sha256"]})
    return encoded({"created_at": datetime.now(timezone.utc).isoformat(), "derived_piece": True,
                    "source_local_file": "prompt-input.stdout.txt (non publié)", "source_local_stdout_sha256": sha(original),
                    "extraction_script_sha256": sha(Path(__file__).read_bytes()), "runtime_source_commit": SOURCE,
                    "scope": "six plugin entries only; global developer/system context excluded", "skills": rows,
                    "actual_plugin_activation_verified": False, "authentication_verified": False,
                    "inference_requested": False, "release_ready": False})


def summary_text(summary: dict[str, Any]) -> str:
    """Rédige exclusivement les résultats partiels disponibles."""
    counts = summary["counts"]
    atoms = summary["atomic_results"]
    return f"""Le pilote dev.6 est **PARTIEL** : seize cas et 124 exigences préparés,
six cas exécutés, cinq réponses liées et cinq juges frais (dix rôles retenus).
Le cas APJA est rejeté hors score : six lectures ont été regroupées dans un
seul appel. Sa réponse et son journal natif sont conservés sans remplacement.
Dix cas ne sont pas exécutés. Les seuls cinq cas jugés donnent
{counts['reussite']} réussites, {counts['echec']} échecs et {counts['bloque']} bloqués.
{summary['effectively_judged_atomic_count']} exigences sont effectivement jugées :
{atoms['true']} vraies, {atoms['false']} fausses et {atoms['null']} indéterminées.
Ce bilan ne constitue pas un résultat de la suite complète.

Candidat mesuré : `{CANDIDATE}` ; source runtime : `{SOURCE}`,
version `1.2.0-dev.6`. L'audit partiel contrôle cinq répondants et cinq juges,
pas seize paires. Le contrôle complet reste non satisfait. Les acteurs chargent
des fichiers candidats par fragments ; l'activation réelle du plugin n'est
pas démontrée. Messages initiaux opaques, isolation absolue, sélections forcées,
source primaire pertinente et vérification de vigueur restent distingués.
Aucun score dev.5 ni DSI autonome n'est transféré.

Le contrôle isolé, hors campagne, a installé et comparé 214 fichiers, dont
166 runtime. `codex debug prompt-input` a construit le catalogue contenant
les six descriptions complètes du plugin. Cette découverte native ne démontre
ni sélection ni chargement par un modèle, ni réponse métier. L'observation
datée de `login status` indique `Not logged in` dans cet état isolé ; elle ne
prouve pas un état d'authentification futur. Aucun modèle ni smoke d'usage n'a
été lancé. Le MCP est configuré désactivé et son exposition effective reste
non vérifiée. Le stdout développeur brut, l'état Codex et les fichiers
d'authentification/configuration ne sont pas publiés. Une pièce dérivée ne
contient que les six descriptions et chemins du plugin, reliés au SHA local.

La campagne utilise les sous-agents natifs Codex, sans lancement de Claude.
Avis humains DSI/RSSI et juridiques, smoke d'usage et suite complète restent
ouverts ; `release_ready=false`. Les PR restent brouillon, sans fusion ni release.
"""


def new_release(summary: dict[str, Any], discovery_hash: str) -> bytes:
    """Actualise seulement l'état partiel, en préservant runs et les revues."""
    evidence = load(PLUGIN / "tests/evidence/release-1.2.0-dev.6.json")
    require(evidence["release_ready"] is False and evidence["runs"] == [], "État de release différent")
    require(evidence["review"] == {"human_legal_validation": False, "human_dsi_validation": False}, "Revue humaine modifiée")
    evidence.update(candidate_commit_status="committed_partially_measured_native_file_load",
                    measurement_status="partial_native_file_load_pilot",
                    native_codex_partial_measurement={"summary_path": "tests/evidence/coactivation-codex-dev6-PARTIEL/synthese-PARTIELLE.json",
                        "candidate_commit": CANDIDATE, "runtime_source_commit": SOURCE,
                        "prepared_cases": 16, "executed_cases": 6, "bound_cases": 5, "judged_cases": 5,
                        "retained_roles": 10, "rejected_protocol_cases": 1, "not_executed_cases": 10,
                        "counts_bound_only": summary["counts"], "effectively_judged_atoms": summary["effectively_judged_atomic_count"],
                        "full_suite_complete": False, "actual_plugin_activation_verified": False,
                        "historical_scores_reused": False},
                    native_discovery={"status": "catalogue_constructed_without_inference", "plugin_skill_count": 6,
                        "runtime_source_commit": SOURCE, "receipt_sha256": discovery_hash,
                        "actual_plugin_activation_verified": False, "authentication_verified": False,
                        "usage_smoke_complete": False})
    evidence["release_blockers"] = ["Pilote dev.6 partiel : un rejet hors score et dix cas non exécutés",
                                   "Activation réelle et smoke d'usage du candidat non établis",
                                   "Avis DSI/RSSI et juridique humains non recueillis"]
    require(evidence["codex_smoke"]["status"] == "not_established", "Smoke déjà établi : examiner avant mise à jour")
    return encoded(evidence)


def main() -> None:
    """Prévalide puis copie sur liste blanche, sans réseau ni commande externe."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    options = parser.parse_args()
    files, control = verified_archive()
    summary = verified_partial(files, control)
    projection = derived_plugin_catalogue()
    scope = summary_text(summary)
    copies = {name: (ROOT / name).read_bytes() for name in SMOKE_ROOT_FILES}
    copies.update({"smoke/" + name: (SMOKE / name).read_bytes() for name in SMOKE_RECEIPTS})
    copies.update({name: files[name] for name in ("rapport-PARTIEL.md", "synthese-PARTIELLE.json", "audit-natif-PARTIEL-final.json")})
    copies[ARCHIVE.name] = ARCHIVE.read_bytes()
    copies[CONTROL.name] = CONTROL.read_bytes()
    copies["smoke/catalogue-plugin-DERIVE.json"] = projection
    copies["outillage/publier_codex_dev6_PARTIEL.py"] = Path(__file__).read_bytes()
    copies["README.md"] = ("# Dev.6 : pilote PARTIEL et découverte native\n\n" + scope +
                            "\nLes rapports de faisabilité et d'installation sont des snapshots datés.\n"
                            "Le reçu de découverte postérieur complète leurs constats sans les réécrire.\n").encode("utf-8")
    current_inventory = DSI / "inventaire-livrables.json"
    historical_inventory = DSI / "inventaire-livrables-v7-historique.json"
    history_readme = DSI / "README-v7-historique.md"
    plugin_history = PLUGIN / "docs/qualification/README-dev5-r2-historique.md"
    for target in (PROOF, DOC, historical_inventory, history_readme, plugin_history):
        require(not target.exists(), f"Destination historique/nouvelle existante : {target}")
    release_path = PLUGIN / "tests/evidence/release-1.2.0-dev.6.json"
    release_history = PLUGIN / "docs/qualification/release-dev6-avant-PARTIEL.json"
    require(not release_history.exists(), "Snapshot release déjà présent")
    release_bytes = new_release(summary, sha((SMOKE / "discovery-verification.json").read_bytes()))
    root_readme = PLUGIN / "README.md"
    root_text = root_readme.read_text(encoding="utf-8")
    statuses = re.findall(r"^> \*\*Statut :\*\* .+$", root_text, re.M)
    require(len(statuses) == 1, "Statut README ambigu")
    root_text = root_text.replace(statuses[0], "> **Statut :** candidat `1.2.0-dev.6`, pilote natif **PARTIEL** : cinq cas jugés, un rejet hors score et dix cas non exécutés. Installation isolée et découverte des six descriptions établies ; activation et smoke d'usage non établis. Avis humains ouverts ; `release_ready=false`. Aucun score dev.5 transféré. Voir [qualification](docs/qualification/README.md).", 1)
    updates = {root_readme: root_text.encode("utf-8"), release_path: release_bytes,
        PLUGIN / "docs/qualification/README.md": ("# Qualification actuelle : dev.6 PARTIEL\n\n" + scope +
            "\n[Rapport partiel](../../tests/evidence/coactivation-codex-dev6-PARTIEL/rapport-PARTIEL.md) · "
            "[Synthèse partielle](../../tests/evidence/coactivation-codex-dev6-PARTIEL/synthese-PARTIELLE.json)\n\n"
            "Le [bilan dev.5 historique](README-dev5-r2-historique.md) conserve sa portée : "
            "16 réponses/16 juges, 4 réussites, 6 échecs, 6 bloqués ; 107/6/11 atomes. "
            "Les preuves dev.4/r7 et antérieures restent conservées.\n").encode("utf-8"),
        DSI / "README.md": ("# Bilan courant : dev.6 PARTIEL\n\n" + scope +
            "\n[Pièces dev.6 PARTIEL](dev6-PARTIEL/README.md) · [rapport](dev6-PARTIEL/rapport-PARTIEL.md)\n\n"
            "La présentation v7 reste **historique** : elle décrivait dev.6 non mesuré à sa date. "
            "Elle ne présente pas ces résultats partiels. Aucun nouveau PowerPoint n'est produit. "
            "Ses contrôles propres et l'inventaire v7 sont conservés sans transfert. "
            "Voir [README historique v7](README-v7-historique.md).\n\n"
            "Dev.5 R2 reste historique : 4 réussites, 6 échecs et 6 bloqués sur 16 cas ; "
            "DSI autonome reste 28/28 sur son propre commit. Avis humains et ouverture "
            "PowerPoint native restent ouverts. CI à vérifier sur chaque nouveau SHA après push.\n").encode("utf-8")}
    runtime_before = {path.relative_to(PLUGIN).as_posix(): sha(path.read_bytes())
                      for path in (PLUGIN / "skills").rglob("*") if path.is_file()}
    require(len(runtime_before) == 166, "Runtime différent")
    frozen = json.loads(files["manifest.json"])["files"]
    require(runtime_before == {name: value for name, value in frozen.items() if name.startswith("skills/")},
            "Runtime courant différent des octets mesurés")
    if not options.apply:
        print(json.dumps({"status": "ready_without_writes", "scope": "PARTIEL", "results": summary["counts"],
                          "archive_entries_verified": len(files), "smoke_whitelist": list(copies),
                          "raw_developer_context_published": False}, ensure_ascii=False, indent=2))
        return
    before = {path.relative_to(ROOT).as_posix(): sha(path.read_bytes()) for path in updates}
    snapshots = {historical_inventory: current_inventory.read_bytes(), history_readme: (DSI / "README.md").read_bytes(),
                 plugin_history: (PLUGIN / "docs/qualification/README.md").read_bytes(), release_history: release_path.read_bytes()}
    records = []
    for destination, entries in ((PROOF, files), (DOC, copies)):
        for name, data in entries.items():
            safe_archive_name(name)
            target = destination.joinpath(*PurePosixPath(name).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(data)
            require(target.read_bytes() == data, f"Copie différente : {target}")
            records.append({"path": target.relative_to(ROOT).as_posix(), "sha256": sha(data), "bytes": len(data)})
    for target, data in snapshots.items():
        with target.open("xb") as stream:
            stream.write(data)
        require(target.read_bytes() == data, "Snapshot modifié")
    for target, data in updates.items():
        target.write_bytes(data)
    require(runtime_before == {path.relative_to(PLUGIN).as_posix(): sha(path.read_bytes())
                               for path in (PLUGIN / "skills").rglob("*") if path.is_file()}, "Runtime modifié")
    receipt = {"created_at": datetime.now(timezone.utc).isoformat(), "scope": "PARTIEL", "candidate_commit": CANDIDATE,
               "runtime_source_commit": SOURCE, "archive_sha256": control["archive_sha256"], "copies": records,
               "snapshots": {path.relative_to(ROOT).as_posix(): sha(data) for path, data in snapshots.items()},
               "updated": [{"path": path.relative_to(ROOT).as_posix(), "before_sha256": before[path.relative_to(ROOT).as_posix()],
                            "after_sha256": sha(path.read_bytes())} for path in updates],
               "runtime_files_unchanged": 166, "global_developer_context_published": False,
               "codex_state_auth_config_published": False, "activation_verified": False, "release_ready": False}
    with (DOC / "Controle-copies-PARTIEL.json").open("xb") as stream:
        stream.write(encoded(receipt))
    inventory = {path.relative_to(DSI).as_posix(): sha(path.read_bytes()) for path in sorted(DSI.rglob("*"))
                 if path.is_file() and path != current_inventory}
    current_inventory.write_bytes(encoded(inventory))
    print(json.dumps({"scope": "PARTIEL", "copied_files": len(records), "runtime_unchanged": 166,
                      "inventory": str(current_inventory), "release_ready": False}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
