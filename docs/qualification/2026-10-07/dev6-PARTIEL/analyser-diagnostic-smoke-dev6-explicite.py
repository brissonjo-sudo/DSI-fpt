"""Analyse locale sans exposer les textes du contexte ni relancer Codex."""
import datetime
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
DIAG = ROOT / 'smoke-dev6-isole-20261007-211629-4dc9cd90/diagnostic-explicite-20261007-214736-45f6ee78'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

execution = json.loads((DIAG / 'execution.json').read_text(encoding='utf-8'))
assert sha(DIAG / 'stdout.json') == execution['stdout_sha256']
assert sha(DIAG / 'stderr.txt') == execution['stderr_sha256']
assert execution['attempts'] == 1
packet = json.loads((DIAG / 'stdout.json').read_bytes())
install = json.loads((DIAG.parent / 'installation.json').read_text(encoding='utf-8'))
cache_skill = pathlib.Path(install['installed_path']) / 'skills/dsi-fpt/SKILL.md'
candidate_skill = ROOT / 'Collectivite-corrections-pr5/skills/dsi-fpt/SKILL.md'
skill_bytes = cache_skill.read_bytes()
assert skill_bytes == candidate_skill.read_bytes()
texts = []
for index, item in enumerate(packet):
    for content_index, part in enumerate(item.get('content', [])):
        if isinstance(part, dict) and isinstance(part.get('text'), str):
            texts.append((index, content_index, item.get('role'), part['text']))

full_matches = [dict(message_index=i, content_index=k, role=role)
                for i, k, role, text in texts if skill_bytes in text.encode('utf-8')]
wrapper_positions = [dict(message_index=i, content_index=k, role=role)
                     for i, k, role, text in texts if '<skill>' in text or '<skill ' in text]
catalogue = texts[0][3]
catalogue_rows = []
for line in catalogue.splitlines():
    if line.startswith('- collectivite-territoriale:') and '(file:' in line:
        catalogue_rows.append({
            'name': line.split(': ', 1)[0].removeprefix('- '),
            'aliased_path': line.split('(file:', 1)[1].strip().removesuffix(')'),
        })
alias_lines = [line for line in catalogue.splitlines()
               if '= ' in line and 'plugins/cache/smoke-dev6/' in line.replace('\\', '/')]
assert len(alias_lines) == 1
alias_path = alias_lines[0].split(' = ', 1)[1].strip('`')
expected_alias = (pathlib.Path(install['installed_path']) / 'skills').as_posix()
assert alias_path.lower() == expected_alias.lower()
marker = '$collectivite-territoriale:dsi-fpt'
literal_user_positions = [dict(message_index=i, content_index=k, text_chars=len(text))
                          for i, k, role, text in texts if role == 'user' and text == marker]
assert len(catalogue_rows) == 6 and len(literal_user_positions) == 1
result = {
    'analyzed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'explicit_literal_mention_context_construction_only',
    'analysis_script_sha256': sha(pathlib.Path(__file__)),
    'execution_script_sha256': execution['script_sha256'],
    'diagnostic_relative_directory': str(DIAG.relative_to(ROOT)).replace('\\', '/'),
    'started_at': execution['started_at'],
    'finished_at': execution['finished_at'],
    'argv': execution['argv'],
    'attempts': 1,
    'exit_code': execution['exit_code'],
    'timed_out': execution['timed_out'],
    'stdout_bytes': execution['stdout_bytes'],
    'stderr_bytes': execution['stderr_bytes'],
    'stdout_sha256': execution['stdout_sha256'],
    'stderr_sha256': execution['stderr_sha256'],
    'execution_receipt_sha256': sha(DIAG / 'execution.json'),
    'candidate_commit': execution['candidate_commit'],
    'candidate_cache_and_config_unchanged': execution['candidate_cache_and_config_unchanged'],
    'unchanged_files_checked': execution['unchanged_files_checked'],
    'json_complete_parse_passed': True,
    'message_count': len(packet),
    'literal_user_marker_positions': literal_user_positions,
    'metadata_discovery_verified': True,
    'catalogue_skills': catalogue_rows,
    'catalogue_root_alias_path': alias_path,
    'dsi_candidate_cache_bytes_equal': True,
    'dsi_skill_bytes': len(skill_bytes),
    'dsi_skill_sha256': sha(cache_skill),
    'full_skill_byte_matches': full_matches,
    'skill_wrapper_positions': wrapper_positions,
    'full_skill_context_injection_verified': bool(full_matches),
    'explicit_skill_selection_verified': False,
    'actual_plugin_activation_verified': False,
    'model_inference_requested': False,
    'model_usage_verified': False,
    'spontaneous_selection_verified': False,
    'login_requested': False,
    'authentication_current_state_not_read': True,
    'network_offline_guarantee': False,
    'human_validation': False,
    'raw_developer_context_published': False,
    'release_ready': False,
    'sources': [
        'https://learn.chatgpt.com/docs/build-skills',
        'https://learn.chatgpt.com/docs/developer-commands',
        'https://learn.chatgpt.com/docs/app-server',
    ],
}
target = ROOT / 'smoke-dev6-explicite-diagnostic-2026-10-07.json'
with target.open('x', encoding='utf-8', newline='\n') as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
    handle.write('\n')
print(json.dumps({k: result[k] for k in ('exit_code', 'metadata_discovery_verified', 'full_skill_context_injection_verified', 'explicit_skill_selection_verified', 'candidate_cache_and_config_unchanged')}, ensure_ascii=False))
