"""Copier le diagnostic explicite sur liste blanche, sans état ni contexte brut."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOC = ROOT / 'DSI-corrections-pr5/docs/qualification/2026-10-07'
TARGET = DOC / 'dev6-PARTIEL'
PLUGIN = ROOT / 'Collectivite-corrections-pr5'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def publish() -> dict:
    """Relier les nouvelles pièces aux hashes réels, sans remplacer un reçu."""
    receipt = json.loads((ROOT / 'smoke-dev6-explicite-diagnostic-2026-10-07.json').read_bytes())
    assert receipt['exit_code'] == 0 and receipt['attempts'] == 1
    assert receipt['metadata_discovery_verified'] is True
    assert receipt['full_skill_context_injection_verified'] is False
    assert receipt['model_inference_requested'] is False
    assert receipt['candidate_cache_and_config_unchanged'] is True
    execution = ROOT / receipt['diagnostic_relative_directory'] / 'execution.json'
    assert sha(execution) == receipt['execution_receipt_sha256']
    assert sha(ROOT / 'diagnostic-smoke-dev6-explicite.ps1') == receipt['execution_script_sha256']
    assert sha(ROOT / 'analyser-diagnostic-smoke-dev6-explicite.py') == receipt['analysis_script_sha256']
    source = json.loads((PLUGIN / 'docs/qualification/gel-dev6-non-mesure.json').read_bytes())
    for relative, digest in source['files'].items():
        assert sha(PLUGIN / relative) == digest
    files = {name: ROOT / name for name in ('smoke-dev6-explicite-diagnostic-2026-10-07.md', 'smoke-dev6-explicite-diagnostic-2026-10-07.json', 'diagnostic-smoke-dev6-explicite.ps1', 'analyser-diagnostic-smoke-dev6-explicite.py')}
    files['smoke/explicite-execution.json'] = execution
    files['outillage/publier_complement_smoke_dev6.py'] = Path(__file__)
    records = []
    for name, path in files.items():
        target = TARGET / name
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as stream:
            stream.write(path.read_bytes())
        assert sha(target) == sha(path)
        records.append({'path': name, 'sha256': sha(target)})
    paragraph = '\nLe diagnostic explicite du 7 octobre à 21:47 UTC conserve le marqueur `$collectivite-territoriale:dsi-fpt` comme texte utilisateur. Aucun bloc contenant les instructions complètes DSI n’est attesté ; seule la découverte est confirmée. Aucune inférence ni connexion demandée. Voir les pièces distinctes `smoke-dev6-explicite-diagnostic-2026-10-07.md/json`. Les reçus antérieurs restent des snapshots datés.\n'
    changed = []
    for path in (TARGET / 'README.md', DOC / 'README.md', PLUGIN / 'docs/qualification/README.md'):
        before = sha(path)
        path.write_bytes(path.read_bytes() + paragraph.encode('utf-8'))
        changed.append({'path': path.relative_to(ROOT).as_posix(), 'before_sha256': before, 'after_sha256': sha(path)})
    result = {'created_at': datetime.now(timezone.utc).isoformat(), 'copies': records, 'updated_readmes': changed,
              'raw_developer_context_published': False, 'auth_or_state_published': False,
              'model_inference_requested': False, 'actual_plugin_activation_verified': False,
              'release_ready': False}
    with (TARGET / 'Controle-complement-smoke.json').open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    inventory_path = DOC / 'inventaire-livrables.json'
    inventory = {path.relative_to(DOC).as_posix(): sha(path) for path in sorted(DOC.rglob('*')) if path.is_file() and path != inventory_path}
    inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    return {'copied': len(records), 'frozen_files_unchanged': len(source['files']), 'inventory_files': len(inventory), 'release_ready': False}


if __name__ == '__main__':
    print(json.dumps(publish(), ensure_ascii=False, indent=2))
