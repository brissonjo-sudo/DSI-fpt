[CmdletBinding()]
param()
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$smokeRoot = Join-Path $PSScriptRoot 'smoke-dev6-isole-20261007-211629-4dc9cd90'
$stateRoot = Join-Path $smokeRoot 'codex-state'
$start = [Diagnostics.ProcessStartInfo]::new()
$start.FileName = 'C:\Users\Krn\AppData\Local\OpenAI\Codex\bin\8aaf1547b825b104\codex.exe'
$start.Arguments = '--no-daemon --cd "' + $smokeRoot + '" debug prompt-input'
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
$beganAt = [DateTime]::UtcNow.ToString('o')
[void]$process.Start()
$outTask = $process.StandardOutput.ReadToEndAsync()
$errTask = $process.StandardError.ReadToEndAsync()
$completed = $process.WaitForExit(50000)
if (-not $completed) { $process.Kill(); $process.WaitForExit() }
$stdout = $outTask.GetAwaiter().GetResult()
$stderr = $errTask.GetAwaiter().GetResult()
function Write-NewText([string]$Path, [string]$Text) {
    $stream = [IO.File]::Open($Path, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
    try {
        $bytes = [Text.UTF8Encoding]::new($false).GetBytes($Text)
        $stream.Write($bytes, 0, $bytes.Length)
    } finally { $stream.Dispose() }
}
$outPath = Join-Path $smokeRoot 'prompt-input.stdout.txt'
$errPath = Join-Path $smokeRoot 'prompt-input.stderr.txt'
Write-NewText $outPath $stdout
Write-NewText $errPath $stderr
$receipt = [ordered]@{
    began_at = $beganAt
    ended_at = [DateTime]::UtcNow.ToString('o')
    command = $start.Arguments
    completed_before_timeout = $completed
    exit_code = $process.ExitCode
    stdout_sha256 = (Get-FileHash -LiteralPath $outPath -Algorithm SHA256).Hash.ToLowerInvariant()
    stderr_sha256 = (Get-FileHash -LiteralPath $errPath -Algorithm SHA256).Hash.ToLowerInvariant()
    stdout_characters = $stdout.Length
    stderr_characters = $stderr.Length
    state_root = $stateRoot
    inference_requested = $false
    activation_observed = $false
    authentication_tested = $false
    release_ready = $false
}
Write-NewText (Join-Path $smokeRoot 'prompt-input.execution.json') (($receipt | ConvertTo-Json -Depth 5) + "`n")
$receipt | ConvertTo-Json -Depth 5
