"""Contrôler le catalogue réellement assemblé, sans inférence ni activation."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
import configuration_codex_dev6 as configuration

ROOT = Path(__file__).resolve().parent
SMOKE = ROOT / 'smoke-dev6-isole-20261007-211629-4dc9cd90'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify() -> dict:
    """Relier six entrées de contexte au cache et à ses descriptions complètes."""
    stdout = SMOKE / 'prompt-input.stdout.txt'
    execution = json.loads((SMOKE / 'prompt-input.execution.json').read_text(encoding='utf-8'))
    assert execution['exit_code'] == 0 and execution['completed_before_timeout'] is True
    assert sha(stdout) == execution['stdout_sha256']
    messages = json.loads(stdout.read_text(encoding='utf-8'))
    texts = [item['text'] for message in messages for item in message.get('content', []) if item.get('type') == 'input_text']
    catalogues = [text for text in texts if '<skills_instructions>' in text]
    assert len(catalogues) == 1
    catalogue = catalogues[0]
    root_match = re.search(r"^- `r1` = `([^`]+)`$", catalogue, re.M)
    assert root_match is not None
    cache = Path(root_match[1])
    installed = json.loads((SMOKE / 'installation.json').read_text(encoding='utf-8'))
    assert cache.resolve() == (Path(installed['installed_path']) / 'skills').resolve()
    assert '1.1.1' not in catalogue
    matches = re.findall(r'^- collectivite-territoriale:([^:]+): (.*?) \(file: r1/([^/]+)/SKILL.md\)$', catalogue, re.M)
    assert len(matches) == 6 and len({row[0] for row in matches}) == 6
    rows = []
    for name, description, folder in matches:
        assert name == folder
        source = configuration.CANDIDATE / 'skills' / name / 'SKILL.md'
        target = cache / name / 'SKILL.md'
        assert description == configuration.description(source)
        assert sha(source) == sha(target)
        rows.append({'name': name, 'description_characters': len(description), 'description_sha256': hashlib.sha256(description.encode('utf-8')).hexdigest(), 'skill_sha256': sha(target), 'installed_path': target.as_posix()})
    return {'created_at': datetime.now(timezone.utc).isoformat(), 'status': 'passed', 'scope': 'native_cli_prompt_construction_without_inference', 'runtime_source_commit': configuration.SOURCE,
            'stdout_sha256': sha(stdout), 'execution_receipt_sha256': sha(SMOKE / 'prompt-input.execution.json'), 'controller_sha256': sha(Path(__file__)), 'skills': rows,
            'plugin_skill_count': 6, 'total_catalogue_skill_count': len(re.findall(r'^- [^\n]+ \(file: r\d+/[^\n]+\)$', catalogue, re.M)),
            'actual_plugin_activation_verified': False, 'model_response_observed': False, 'inference_requested': False, 'authentication_tested': False, 'mcp_actual_exposure_verified': False, 'network_activity_measured': False, 'release_ready': False}


if __name__ == '__main__':
    result = verify()
    with (SMOKE / 'discovery-verification.json').open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(json.dumps({key: value for key, value in result.items() if key != 'skills'}, ensure_ascii=False, indent=2))
