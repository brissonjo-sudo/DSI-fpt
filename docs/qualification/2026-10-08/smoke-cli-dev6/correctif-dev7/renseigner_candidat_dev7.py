"""Gèle les octets dev.7 committés ; aucune inférence ni reprise de score."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGIN = ROOT / 'Collectivite-corrections-pr5'
sys.path.insert(0, str(PLUGIN / 'scripts'))
from corrected_candidate import inventory, git_bytes, git_revision, source_overlays


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-commit', required=True)
    args = parser.parse_args()
    commit = args.source_commit
    if re.fullmatch(r'[0-9a-f]{40}', commit) is None or git_revision(PLUGIN, 'HEAD') != commit:
        raise ValueError('Le commit source explicite doit être le HEAD committé')
    frozen_path = PLUGIN / 'docs/qualification/gel-dev7-non-mesure.json'
    if frozen_path.exists():
        raise ValueError('Le gel dev.7 existe déjà ; ne pas le réécrire')
    release_path = PLUGIN / 'tests/evidence/release-1.2.0-dev.7.json'
    release = json.loads(release_path.read_bytes())
    if (release['plugin_version'] != '1.2.0-dev.7' or release['plugin_commit'] is not None
            or release['runs'] or release['release_ready'] or release['historical_scores_reused']
            or release['measurement_status'] != 'not_measured'):
        raise ValueError('Statut dev.7 non mesuré inattendu')
    packaging = json.loads((PLUGIN / '.codex-plugin/plugin.json').read_bytes())
    if packaging['version'] != '1.2.0-dev.7':
        raise ValueError('Packaging différent de dev.7')
    paths = inventory(PLUGIN)
    blobs = git_bytes(PLUGIN, commit, paths)
    hashes = {}
    for relative in sorted(paths):
        data = (PLUGIN / relative).read_bytes()
        if data != blobs[relative]:
            raise ValueError('Octets différents du commit source : ' + relative)
        hashes[relative] = digest(data)
    if hashes['skills/dsi-fpt/SKILL.md'] != '2b9df5adb10f8dfdb7e1cc86b454b587c39e3194692f91388212cc38aa02fded':
        raise ValueError('Runtime DSI différent du correctif dev.7 revu')
    runtime_count = sum(name.startswith('skills/') for name in hashes)
    if runtime_count != 166:
        raise ValueError('Inventaire runtime différent de 166')
    frozen = {
        'created_at': datetime.now(timezone.utc).isoformat(),
        'profile': 'codex-candidate-byte-inventory-v1',
        'plugin_version': '1.2.0-dev.7', 'candidate_commit': commit,
        'candidate_tree': git_revision(PLUGIN, 'HEAD^{tree}'),
        'files': hashes, 'file_count': len(hashes), 'runtime_files': runtime_count,
        'declared_overlays': source_overlays(PLUGIN), 'git_blob_bytes_verified': True,
        'measurement_status': 'not_measured', 'model': None,
        'historical_scores_reused': False, 'actual_plugin_activation_verified': False,
        'release_ready': False,
        'correction_status': 'hypothesis_pending_new_measurement',
        'claim': 'Gel statique des octets dev.7 committés ; aucune campagne ni activation de plugin.',
    }
    with frozen_path.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(frozen, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    release.update(plugin_commit=commit, candidate_commit_status='committed_not_measured',
                   frozen_inventory_path='docs/qualification/gel-dev7-non-mesure.json')
    release_path.write_text(json.dumps(release, ensure_ascii=False, indent=2) + '\n',
                            encoding='utf-8', newline='\n')
    print(json.dumps({key: frozen[key] for key in ('candidate_commit', 'file_count',
                                                  'runtime_files', 'measurement_status')}))


if __name__ == '__main__':
    main()
