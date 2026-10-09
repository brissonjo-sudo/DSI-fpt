[CmdletBinding()]
param()
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$workspaceRoot = [IO.Path]::GetFullPath($PSScriptRoot)
$smokeRoot = Join-Path $workspaceRoot 'smoke-dev6-isole-20261007-211629-4dc9cd90'
$stateRoot = Join-Path $smokeRoot 'codex-state'
$receiptPath = Join-Path $smokeRoot 'installation.json'
$installed = Get-Content -LiteralPath $receiptPath -Raw | ConvertFrom-Json
$candidateRoot = Join-Path $workspaceRoot 'Collectivite-corrections-pr5'
$frozen = Get-Content -LiteralPath (Join-Path $candidateRoot 'docs/qualification/gel-dev6-non-mesure.json') -Raw | ConvertFrom-Json
if ($installed.installed_manifest_version -ne '1.2.0-dev.6' -or $installed.candidate_commit -ne $frozen.candidate_commit) { throw 'Etat candidat inattendu.' }
$tracked = [Collections.Generic.List[object]]::new()
foreach ($entry in $frozen.files.PSObject.Properties) {
    foreach ($scope in @('candidate','cache')) {
        $base = if ($scope -eq 'candidate') { $candidateRoot } else { [string]$installed.installed_path }
        $path = Join-Path $base $entry.Name
        $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($hash -ne $entry.Value) { throw 'Bytes geles modifies avant diagnostic.' }
        $tracked.Add([pscustomobject]@{ scope = $scope; path = $path; sha256 = $hash })
    }
}
$configPath = Join-Path $stateRoot 'config.toml'
$tracked.Add([pscustomobject]@{ scope = 'isolated_config'; path = $configPath; sha256 = (Get-FileHash -LiteralPath $configPath -Algorithm SHA256).Hash.ToLowerInvariant() })
$diagnosticRoot = Join-Path $smokeRoot ('diagnostic-explicite-' + [DateTime]::UtcNow.ToString('yyyyMMdd-HHmmss') + '-' + [Guid]::NewGuid().ToString('N').Substring(0,8))
if (Test-Path -LiteralPath $diagnosticRoot) { throw 'Diagnostic deja existant.' }
[void][IO.Directory]::CreateDirectory($diagnosticRoot)
$stdoutPath = Join-Path $diagnosticRoot 'stdout.json'
$stderrPath = Join-Path $diagnosticRoot 'stderr.txt'
$stdoutStream = [IO.File]::Open($stdoutPath, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
$stderrStream = [IO.File]::Open($stderrPath, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
$start = [Diagnostics.ProcessStartInfo]::new()
$start.FileName = 'C:\Users\Krn\AppData\Local\OpenAI\Codex\bin\8aaf1547b825b104\codex.exe'
# Chaine single-quoted : le dollar reste litteral, aucun shell intermediaire.
$start.Arguments = '--cd "' + $smokeRoot + '" debug prompt-input "$collectivite-territoriale:dsi-fpt"'
$start.WorkingDirectory = $smokeRoot
$start.UseShellExecute = $false
$start.CreateNoWindow = $true
$start.RedirectStandardOutput = $true
$start.RedirectStandardError = $true
$start.EnvironmentVariables['CODEX_HOME'] = $stateRoot
$start.EnvironmentVariables['CODEX_SQLITE_HOME'] = $stateRoot
foreach ($name in @($start.EnvironmentVariables.Keys)) {
    if ([string]$name -match '(?i)(TOKEN|SECRET|PASSWORD|API_KEY|ACCESS_KEY|AUTHORIZATION)') {
        $start.EnvironmentVariables.Remove([string]$name)
    }
}
$process = [Diagnostics.Process]::new()
$process.StartInfo = $start
$startedAt = [DateTime]::UtcNow.ToString('o')
$timedOut = $false
try {
    [void]$process.Start()
    $outTask = $process.StandardOutput.BaseStream.CopyToAsync($stdoutStream)
    $errTask = $process.StandardError.BaseStream.CopyToAsync($stderrStream)
    if (-not $process.WaitForExit(30000)) {
        $timedOut = $true
        $process.Kill()
        [void]$process.WaitForExit(3000)
    }
    $outTask.GetAwaiter().GetResult()
    $errTask.GetAwaiter().GetResult()
} finally {
    $stdoutStream.Dispose()
    $stderrStream.Dispose()
}
$unchanged = $true
foreach ($entry in $tracked) {
    if ((Get-FileHash -LiteralPath $entry.path -Algorithm SHA256).Hash.ToLowerInvariant() -ne $entry.sha256) { $unchanged = $false }
}
$metadata = [ordered]@{
    started_at = $startedAt
    finished_at = [DateTime]::UtcNow.ToString('o')
    executable = $start.FileName
    argv = @('--cd',$smokeRoot,'debug','prompt-input','$collectivite-territoriale:dsi-fpt')
    initial_mention = '$collectivite-territoriale:dsi-fpt'
    state_root = $stateRoot
    candidate_commit = $frozen.candidate_commit
    script_sha256 = (Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLowerInvariant()
    attempts = 1
    timeout_seconds = 30
    timed_out = $timedOut
    exit_code = $process.ExitCode
    stdout_sha256 = (Get-FileHash -LiteralPath $stdoutPath -Algorithm SHA256).Hash.ToLowerInvariant()
    stderr_sha256 = (Get-FileHash -LiteralPath $stderrPath -Algorithm SHA256).Hash.ToLowerInvariant()
    stdout_bytes = (Get-Item -LiteralPath $stdoutPath).Length
    stderr_bytes = (Get-Item -LiteralPath $stderrPath).Length
    candidate_cache_and_config_unchanged = $unchanged
    unchanged_files_checked = $tracked.Count
    model_inference_requested = $false
    login_requested = $false
    model_usage_verified = $false
    spontaneous_selection_verified = $false
    human_validation = $false
    raw_outputs_local_only = $true
    release_ready = $false
}
$json = ($metadata | ConvertTo-Json -Depth 6).Replace("`r`n", "`n") + "`n"
[IO.File]::WriteAllText((Join-Path $diagnosticRoot 'execution.json'), $json, [Text.UTF8Encoding]::new($false))
Write-Output ($metadata | Select-Object exit_code,timed_out,stdout_bytes,stderr_bytes,candidate_cache_and_config_unchanged | ConvertTo-Json)
Write-Output $diagnosticRoot
