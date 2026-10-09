"""Prépare puis applique une correction DSI bornée ; aucune mesure comportementale."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGIN = ROOT / 'Collectivite-corrections-pr5'
SOURCE = ROOT / 'DSI-corrections-pr5'
sys.path.insert(0, str(PLUGIN / 'scripts'))
import sync_skills
from instruction_overlays import apply_overlays, replace_description, replace_block


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_source(*args, cwd=None, input_data=None):
    command = ['git', '-c', 'core.longpaths=true', '-c', 'safe.directory=' + Path(cwd).as_posix(), *args]
    result = subprocess.run(command, cwd=cwd, input=input_data, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.decode('utf-8', errors='replace'))
    return result.stdout


def json_bytes(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def replacement(content: bytes, old: str, new: str) -> bytes:
    before, after = old.encode('utf-8'), new.encode('utf-8')
    if content.count(before) != 1:
        raise ValueError('Ancre exacte absente ou ambiguë')
    return content.replace(before, after, 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    original_upstream = (PLUGIN / 'upstream.json').read_bytes()
    upstream = json.loads(original_upstream)
    original_spec = upstream['skills']['dsi-fpt']
    if original_spec['commit'] != '704e5dd6a3d15994ed431b23585aabd72086ca75':
        raise ValueError('Pin DSI inattendu')
    sync_skills.run_git = git_source
    files = sync_skills.archive_files(SOURCE, original_spec)
    current_generated = apply_overlays(PLUGIN, files, original_spec['instruction_overlays'])['SKILL.md']
    current_runtime = (PLUGIN / 'skills/dsi-fpt/SKILL.md').read_bytes()
    if current_generated != current_runtime:
        raise ValueError('Runtime DSI actuel différent des blobs et overlays déclarés')
    protected = {}
    for prefix in ('tests/evidence', 'docs/qualification'):
        for path in (PLUGIN / prefix).rglob('*'):
            if path.is_file():
                protected[path.relative_to(PLUGIN).as_posix()] = sha(path.read_bytes())
    runtime_before = {path.relative_to(PLUGIN).as_posix(): sha(path.read_bytes())
                      for path in (PLUGIN / 'skills').rglob('*') if path.is_file()}
    if len(runtime_before) != 166:
        raise ValueError('Inventaire runtime inattendu')
    description_path = 'overlays/dsi-fpt-description.md'
    contract_path = 'overlays/dsi-fpt.md'
    incident_path = 'overlays/dsi-fpt-incident-stop.md'
    planned = {}
    planned[description_path] = replacement(
        (PLUGIN / description_path).read_bytes(),
        '  STOP avant Skill ou toute annonce pour incident cyber ou surveillance,\n'
        '  y compris nouvel indice concernant un incident ancien ou clos.\n',
        '  Incident cyber ou surveillance, y compris nouvel indice concernant un incident\n'
        '  ancien ou clos : le premier message visible commence par STOP. Cette priorité\n'
        '  vaut aussi pour le commentaire de progression avant outils : émettre le STOP,\n'
        '  puis charger les skills et les sources, sans annonce préalable.\n')
    planned[contract_path] = replacement(
        (PLUGIN / contract_path).read_bytes(),
        '   Un STOP dans la réponse finale ne répare jamais un préambule déjà émis.\n',
        '   Le STOP constitue le premier commentaire de progression avant outils.\n'
        '   Si un point d’avancement est attendu, commencer ce commentaire par STOP ;\n'
        '   annoncer le chargement des rôles ou des sources seulement ensuite.\n'
        '   Un STOP dans la réponse finale ne répare jamais un préambule déjà émis.\n')
    planned[incident_path] = replacement(
        (PLUGIN / incident_path).read_bytes(),
        'Dès qu\'un déclencheur apparaît, le **premier livrable, avant tout autre\n'
        'contenu**, est :\n',
        'Dès qu\'un déclencheur apparaît, le **premier texte visible de la session**,\n'
        'y compris le commentaire de progression avant outils, commence par le STOP\n'
        'ci-dessous. Les annonces de chargement viennent seulement ensuite :\n')
    projected = dict(files)
    for overlay in original_spec['instruction_overlays']:
        content = planned[overlay['source']]
        base = projected[overlay['target']]
        overlay['base_sha256'] = sha(base)
        overlay['source_sha256'] = sha(content)
        anchor = overlay['anchor'].encode('utf-8')
        operation = overlay.get('operation', 'insert-before')
        if operation == 'insert-before':
            if base.count(anchor) != 1:
                raise ValueError('Ancre insertion non unique')
            projected[overlay['target']] = base.replace(anchor, content.rstrip(b'\n') + b'\n\n' + anchor, 1)
        elif operation == 'replace-description':
            projected[overlay['target']] = replace_description(base, anchor, content)
        else:
            projected[overlay['target']] = replace_block(base, anchor, content)
    planned['upstream.json'] = json_bytes(upstream)
    planned['skills/dsi-fpt/SKILL.md'] = projected['SKILL.md']
    for relative in ('.claude-plugin/plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/marketplace.json'):
        value = json.loads((PLUGIN / relative).read_bytes())
        if relative.endswith('marketplace.json'):
            if value['plugins'][0]['version'] != '1.2.0-dev.6':
                raise ValueError('Version marketplace inattendue')
            value['plugins'][0]['version'] = '1.2.0-dev.7'
        else:
            if value['version'] != '1.2.0-dev.6':
                raise ValueError('Version packaging inattendue')
            value['version'] = '1.2.0-dev.7'
        planned[relative] = json_bytes(value)
    planned['docs/adr/0008-stop-premier-commentaire-codex.md'] = '''# STOP dans le premier commentaire de progression

Date : 2026-10-08. Statut : hypothèse de correction, candidat 1.2.0-dev.7 non mesuré.

Le pilote dev.6 contient un échec observable sur `plugin-dsi-reouverture` :
l’annonce de chargement e3 précède le STOP e4 puis le chargement DSI e5.
Le STOP ouvrant la réponse finale e24 ne répare pas ce préambule.
La description et le contrat demandaient déjà de commencer par STOP ;
la règle n’était pas absente et la cause de sa non-application n’est pas établie.

Le candidat dev.7 précise, dans la description disponible avant le chargement
et dans les deux overlays DSI, que le STOP constitue le premier commentaire
de progression avant outils. Les annonces de chargement viennent ensuite.
Les mesures conservatoires, les frontières métier, les six commits amont et
les exigences de preuve primaire ou d’abstention restent identiques.
Seul le SKILL DSI généré change parmi les 166 fichiers runtime.

La génération est ciblée depuis les blobs Git du pin DSI, avec les opérations
bornées déjà déclarées dans `upstream.json`. Les autres runtimes et les preuves
historiques, gels et release dev.6 ne sont pas réécrits. L’installation isolée
dev.6 utilisée pour le smoke n’est pas modifiée.

Cette formulation est une hypothèse jusqu’à une nouvelle mesure sur les octets
dev.7 committés et gelés, avec répondants et juges frais. Aucun résultat dev.6,
dev.5 ou DSI autonome n’est transféré. Contrôler le premier événement assistant
visible, y compris les commentaires avant outils ; une annonce puis un STOP
reste un échec. Distinguer lecture de fichier, sélection et activation réelle,
réception de source primaire et abstention. La release reste bloquée tant que
la campagne, le smoke propre au candidat et les avis humains restent ouverts.
'''.encode('utf-8')
    release = {
        'plugin_version': '1.2.0-dev.7', 'plugin_commit': None,
        'candidate_commit_status': 'uncommitted_not_measured', 'release_ready': False,
        'available_skills': ['dpm-fpt', 'drh-fpt', 'dpo-ct', 'dirfi-fpt', 'recherche-juridique', 'dsi-fpt'],
        'upstream_commits': {name: spec['commit'] for name, spec in upstream['skills'].items()},
        'historical_scores_reused': False, 'measurement_status': 'not_measured', 'runs': [],
        'review': {'human_legal_validation': False, 'human_dsi_validation': False},
        'codex_smoke': {'status': 'not_established', 'plugin_commit': None},
        'release_blockers': ['Correctif STOP dev.7 non mesuré ; aucun score antérieur transféré',
                             'Campagne complète sur les octets dev.7 non réalisée',
                             'Activation réelle et smoke d’usage dev.7 non établis',
                             'Avis DSI/RSSI et juridique humains non recueillis'],
        'frozen_inventory_path': None,
        'correction_status': 'hypothesis_pending_new_measurement',
        'preceding_measurement': {
            'summary_path': 'tests/evidence/coactivation-codex-dev6-PARTIEL/synthese-PARTIELLE.json',
            'runtime_source_commit': '3f0df285898cf1e36d1ddda8d85d0c4cd5e0903b',
            'activation_kind': 'file_read_fragments', 'transferred': False},
    }
    planned['tests/evidence/release-1.2.0-dev.7.json'] = json_bytes(release)
    for relative in ('docs/adr/0008-stop-premier-commentaire-codex.md', 'tests/evidence/release-1.2.0-dev.7.json'):
        if (PLUGIN / relative).exists():
            raise ValueError('Nouvelle destination déjà présente : ' + relative)
    report = {
        'created_at': datetime.now(timezone.utc).isoformat(), 'applied': args.apply,
        'source_pin_dsi': original_spec['commit'], 'source_skill_sha256': sha(files['SKILL.md']),
        'runtime_before_sha256': sha(current_runtime), 'runtime_after_sha256': sha(projected['SKILL.md']),
        'planned_files': {relative: sha(content) for relative, content in planned.items()},
        'declared_dsi_overlays': original_spec['instruction_overlays'],
        'historical_protected_file_count': len(protected), 'runtime_file_count': len(runtime_before),
        'measurement_status': 'not_measured', 'historical_scores_reused': False,
    }
    if args.apply:
        for relative, content in planned.items():
            target = PLUGIN / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        generated = apply_overlays(PLUGIN, files, original_spec['instruction_overlays'])['SKILL.md']
        if generated != projected['SKILL.md']:
            raise ValueError('Génération ciblée divergente')
        for relative, digest in protected.items():
            if sha((PLUGIN / relative).read_bytes()) != digest:
                raise ValueError('Preuve historique modifiée : ' + relative)
        changed_runtime = [relative for relative, digest in runtime_before.items()
                           if sha((PLUGIN / relative).read_bytes()) != digest]
        if changed_runtime != ['skills/dsi-fpt/SKILL.md']:
            raise ValueError('Runtime modifié hors périmètre : ' + repr(changed_runtime))
        report['changed_runtime'] = changed_runtime
        report['historical_bytes_unchanged'] = True
        receipt = ROOT / 'correctif-dev7-verification-locale.json'
        with receipt.open('xb') as stream:
            stream.write(json_bytes(report))
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
