[CmdletBinding()]
param([switch]$Login, [switch]$Session)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($Login -and $Session) { throw 'Choisir -Login ou -Session, pas les deux.' }
$smokeRoot = Join-Path $PSScriptRoot 'smoke-dev6-isole-20261007-211629-4dc9cd90'
$stateRoot = Join-Path $smokeRoot 'codex-state'
if (-not (Test-Path -LiteralPath (Join-Path $smokeRoot 'installation.json'))) { throw 'Installation isolee absente.' }

function Find-CodexExecutable {
    # Les mises a jour de l'application changent le sous-dossier du binaire.
    $command = Get-Command codex.exe -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if ($command -and (Test-Path -LiteralPath $command.Source -PathType Leaf)) {
        return $command.Source
    }
    $binRoot = Join-Path $env:LOCALAPPDATA 'OpenAI\Codex\bin'
    if (Test-Path -LiteralPath $binRoot -PathType Container) {
        $folders = Get-ChildItem -LiteralPath $binRoot -Directory |
            Sort-Object LastWriteTimeUtc -Descending
        foreach ($folder in $folders) {
            $candidatePath = Join-Path $folder.FullName 'codex.exe'
            if (Test-Path -LiteralPath $candidatePath -PathType Leaf) {
                return $candidatePath
            }
        }
    }
    throw 'codex.exe introuvable dans PATH et dans le dossier local de Codex.'
}

$start = [Diagnostics.ProcessStartInfo]::new()
$start.FileName = Find-CodexExecutable
$start.WorkingDirectory = $smokeRoot
$start.UseShellExecute = $false
$start.EnvironmentVariables['CODEX_HOME'] = $stateRoot
$start.EnvironmentVariables['CODEX_SQLITE_HOME'] = $stateRoot
foreach ($name in @($start.EnvironmentVariables.Keys)) {
    if ([string]$name -match '(?i)(TOKEN|SECRET|PASSWORD|API_KEY|ACCESS_KEY|AUTHORIZATION)') {
        $start.EnvironmentVariables.Remove([string]$name)
    }
}
if ($Login) {
    # Action interactive de l'utilisateur ; aucune lecture/copie d'auth global.
    $start.Arguments = 'login'
} elseif ($Session) {
    # Aucun prompt initial, aucun choix de modele. MCP de smoke configure desactive.
    $start.Arguments = '--no-daemon --cd "' + $smokeRoot + '" --sandbox read-only'
} else {
    $start.Arguments = 'login status'
    $start.CreateNoWindow = $true
    $start.RedirectStandardOutput = $true
    $start.RedirectStandardError = $true
}
$process = [Diagnostics.Process]::new()
$process.StartInfo = $start
[void]$process.Start()
if ($Login -or $Session) {
    $process.WaitForExit()
    exit $process.ExitCode
}
$outTask = $process.StandardOutput.ReadToEndAsync()
$errTask = $process.StandardError.ReadToEndAsync()
if (-not $process.WaitForExit(30000)) { $process.Kill(); throw 'Controle de statut interrompu apres 30 secondes.' }
$stdout = $outTask.GetAwaiter().GetResult()
$stderr = $errTask.GetAwaiter().GetResult()
$safeStatus = if (($stdout + $stderr).Trim() -eq 'Not logged in') { 'not_logged_in' } else { 'other_status_not_disclosed' }
[ordered]@{ checked_at = [DateTime]::UtcNow.ToString('o'); codex_executable = $start.FileName; state_root = $stateRoot; exit_code = $process.ExitCode; status = $safeStatus; upstream_authentication_verified = $false; inference_requested = $false } | ConvertTo-Json
