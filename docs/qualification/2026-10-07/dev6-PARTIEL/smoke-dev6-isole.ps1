[CmdletBinding()]
param(
    [switch]$Prepare,
    [switch]$Install,
    [string]$SmokeDirectory
)

# Par defaut : lecture, hashes et aides CLI seulement. Aucun modele lance.
# -Prepare : copie de travail neuve + configuration isolee, sans installation.
# -Install : preparation neuve puis installation dans l'etat isole uniquement.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$workspaceRoot = [IO.Path]::GetFullPath($PSScriptRoot)
$candidateRoot = Join-Path $workspaceRoot 'Collectivite-corrections-pr5'
$frozenPath = Join-Path $candidateRoot 'docs/qualification/gel-dev6-non-mesure.json'
$frozen = Get-Content -LiteralPath $frozenPath -Raw | ConvertFrom-Json
if ($frozen.plugin_version -ne '1.2.0-dev.6') { throw 'Le gel attendu dev.6 est absent.' }
if ($frozen.candidate_commit -ne '3f0df285898cf1e36d1ddda8d85d0c4cd5e0903b') { throw 'Source du gel inattendue.' }

function Test-ChildPath([string]$Root, [string]$Path) {
    $prefix = [IO.Path]::GetFullPath($Root).TrimEnd('\', '/') + [IO.Path]::DirectorySeparatorChar
    if (-not [IO.Path]::GetFullPath($Path).StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) {
        throw 'Chemin hors de la racine prevue.'
    }
}
function Write-NewUtf8([string]$Path, [string]$Text) {
    $stream = [IO.File]::Open($Path, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
    try {
        $bytes = [Text.UTF8Encoding]::new($false).GetBytes($Text.Replace("`r`n", "`n"))
        $stream.Write($bytes, 0, $bytes.Length)
    } finally { $stream.Dispose() }
}
function ConvertTo-WindowsArgument([string]$Value) {
    $escaped = [regex]::Replace($Value, '(\\*)"', '$1$1\"')
    $escaped = [regex]::Replace($escaped, '(\\+)$', '$1$1')
    return '"' + $escaped + '"'
}
function Invoke-IsolatedCli([string[]]$Arguments, [string]$StateRoot, [string]$WorkingRoot) {
    # CODEX_HOME est uniquement la racine d'etat documentee de ce processus enfant.
    # Aucun changement de $env:CODEX_HOME, de HOME ou du profil utilisateur.
    $start = [Diagnostics.ProcessStartInfo]::new()
    $start.FileName = $script:codexPath
    $start.Arguments = (($Arguments | ForEach-Object { ConvertTo-WindowsArgument $_ }) -join ' ')
    $start.WorkingDirectory = $WorkingRoot
    $start.UseShellExecute = $false
    $start.CreateNoWindow = $true
    $start.RedirectStandardOutput = $true
    $start.RedirectStandardError = $true
    $start.EnvironmentVariables['CODEX_HOME'] = $StateRoot
    $start.EnvironmentVariables['CODEX_SQLITE_HOME'] = $StateRoot
    # Ne pas transmettre une authentification d'inference ou de service par heritage.
    foreach ($name in @($start.EnvironmentVariables.Keys)) {
        if ([string]$name -match '(?i)(TOKEN|SECRET|PASSWORD|API_KEY|ACCESS_KEY|AUTHORIZATION)') {
            $start.EnvironmentVariables.Remove([string]$name)
        }
    }
    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $start
    [void]$process.Start()
    $outTask = $process.StandardOutput.ReadToEndAsync()
    $errTask = $process.StandardError.ReadToEndAsync()
    if (-not $process.WaitForExit(60000)) {
        $process.Kill()
        throw 'Commande de gestion locale interrompue apres 60 secondes.'
    }
    $stdout = $outTask.GetAwaiter().GetResult()
    $stderr = $errTask.GetAwaiter().GetResult()
    if ($process.ExitCode -ne 0) {
        # Ne pas imprimer le stderr brut susceptible de contenir une information d'auth.
        throw "Commande de gestion echouee (code $($process.ExitCode)); installation non qualifiee."
    }
    return $stdout
}

$codexCommand = Get-Command codex -ErrorAction Stop
$script:codexPath = $codexCommand.Source
$version = (& $script:codexPath --version | Out-String).Trim()
if ($LASTEXITCODE -ne 0 -or $version -ne 'codex-cli 0.160.0') {
    throw 'CLI different de 0.160.0 : revoir le protocole et les aides avant de preparer.'
}
$helpChecks = @(
    @{ Args = @('plugin','add','--help'); Match = 'plugin add' },
    @{ Args = @('plugin','list','--help'); Match = '--json' },
    @{ Args = @('plugin','marketplace','add','--help'); Match = 'local path' },
    @{ Args = @('--help'); Match = '--no-daemon' }
)
foreach ($check in $helpChecks) {
    $arguments = $check.Args
    $helpText = (& $script:codexPath @arguments | Out-String)
    if ($LASTEXITCODE -ne 0 -or -not $helpText.Contains($check.Match)) { throw 'Aide CLI inattendue.' }
}

$verifiedFiles = [Collections.Generic.List[object]]::new()
foreach ($entry in $frozen.files.PSObject.Properties) {
    $sourcePath = [IO.Path]::GetFullPath((Join-Path $candidateRoot $entry.Name))
    Test-ChildPath $candidateRoot $sourcePath
    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) { throw "Fichier gele absent : $($entry.Name)" }
    $actualHash = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actualHash -ne $entry.Value) { throw "Fichier gele modifie : $($entry.Name)" }
    $verifiedFiles.Add([pscustomobject]@{ path = $entry.Name; sha256 = $actualHash; frozen = $true })
}
$runtimeCount = @($verifiedFiles | Where-Object { $_.path.StartsWith('skills/') }).Count
if ($runtimeCount -ne 166 -or $verifiedFiles.Count -ne 213) { throw 'Inventaire dev.6 inattendu.' }
$manifest = Get-Content -LiteralPath (Join-Path $candidateRoot '.codex-plugin/plugin.json') -Raw | ConvertFrom-Json
if ($manifest.version -ne '1.2.0-dev.6' -or $manifest.name -ne 'collectivite-territoriale') { throw 'Manifeste inattendu.' }
$mcpMetadata = Get-Content -LiteralPath (Join-Path $candidateRoot '.mcp.json') -Raw | ConvertFrom-Json
$servers = @($mcpMetadata.mcpServers.PSObject.Properties)
if ($servers.Count -ne 1 -or $servers[0].Name -ne 'droit-francais') { throw 'Configuration MCP a revoir.' }
$serverKeys = @($servers[0].Value.PSObject.Properties.Name)
if (@($serverKeys | Where-Object { $_ -notin @('type','url','oauth') }).Count -gt 0) { throw 'Metadata MCP supplementaire : revue manuelle requise.' }
$oauthKeys = @($servers[0].Value.oauth.PSObject.Properties.Name)
if (@($oauthKeys | Where-Object { $_ -notin @('clientId','callbackPort') }).Count -gt 0) {
    throw 'OAuth contient des champs non publics attendus : aucune copie.'
}
$serviceUri = [Uri]$servers[0].Value.url
if ($serviceUri.UserInfo -or $serviceUri.Query -or $serviceUri.Fragment) { throw 'URL MCP contenant des donnees non prevues.' }

# Ressources d'interface necessaires, avec hashes distincts du gel.
foreach ($relativePath in @('assets/icon.png')) {
    $resourcePath = Join-Path $candidateRoot $relativePath
    if (-not (Test-Path -LiteralPath $resourcePath -PathType Leaf)) { throw 'Ressource interface absente.' }
    $verifiedFiles.Add([pscustomobject]@{ path = $relativePath; sha256 = (Get-FileHash -LiteralPath $resourcePath -Algorithm SHA256).Hash.ToLowerInvariant(); frozen = $false })
}
$createdAt = [DateTime]::UtcNow.ToString('o')
$preflight = [ordered]@{
    created_at = $createdAt
    scope = 'preflight_local_no_install_no_inference'
    codex_version = $version
    candidate_commit = $frozen.candidate_commit
    runtime_files = $runtimeCount
    frozen_files = 213
    additional_interface_files = 1
    installed = $false
    measured = $false
    actual_plugin_activation_verified = $false
    release_ready = $false
}
if (-not $Prepare -and -not $Install) {
    $preflight | ConvertTo-Json -Depth 5
    Write-Output 'Preflight termine. -Prepare cree une copie neuve ; -Install prepare puis installe seulement dans son etat isole. Aucun mode ne lance un modele.'
    return
}

if (-not $SmokeDirectory) {
    $SmokeDirectory = Join-Path $workspaceRoot ('smoke-dev6-isole-' + [DateTime]::UtcNow.ToString('yyyyMMdd-HHmmss') + '-' + [Guid]::NewGuid().ToString('N').Substring(0,8))
}
$smokeRoot = [IO.Path]::GetFullPath($SmokeDirectory)
Test-ChildPath $workspaceRoot $smokeRoot
if (Test-Path -LiteralPath $smokeRoot) { throw 'Dossier de smoke deja existant : aucune reutilisation ni ecrasement.' }
[void][IO.Directory]::CreateDirectory($smokeRoot)
$stateRoot = Join-Path $smokeRoot 'codex-state'
$pluginRoot = Join-Path $smokeRoot 'plugin-dev6'
$marketplaceFolder = Join-Path $smokeRoot '.agents/plugins'
[void][IO.Directory]::CreateDirectory($stateRoot)
[void][IO.Directory]::CreateDirectory($marketplaceFolder)
foreach ($entry in $verifiedFiles) {
    $destination = [IO.Path]::GetFullPath((Join-Path $pluginRoot $entry.path))
    Test-ChildPath $pluginRoot $destination
    [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($destination))
    [IO.File]::Copy((Join-Path $candidateRoot $entry.path), $destination, $false)
    if ((Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash.ToLowerInvariant() -ne $entry.sha256) { throw 'Copie non identique.' }
}
$marketplace = [ordered]@{
    name = 'smoke-dev6'
    plugins = @([ordered]@{
        name = 'collectivite-territoriale'
        source = @{ source = 'local'; path = './plugin-dev6' }
        policy = @{ installation = 'AVAILABLE'; authentication = 'ON_USE' }
        category = 'Productivity'
    })
}
Write-NewUtf8 (Join-Path $marketplaceFolder 'marketplace.json') (($marketplace | ConvertTo-Json -Depth 8) + "`n")
$isolatedConfig = @'
approval_policy = "on-request"
sandbox_mode = "read-only"
web_search = "disabled"

[plugins."collectivite-territoriale@smoke-dev6"]
enabled = true

[plugins."collectivite-territoriale@smoke-dev6".mcp_servers."droit-francais"]
enabled = false
'@
Write-NewUtf8 (Join-Path $stateRoot 'config.toml') ($isolatedConfig + "`n")
$preflight.scope = 'prepared_local_no_inference'
$preflight['smoke_root'] = $smokeRoot
$preflight['state_root'] = $stateRoot
$preflight['files'] = @($verifiedFiles)
$preflight['authentication'] = 'not_established_no_credentials_copied'
Write-NewUtf8 (Join-Path $smokeRoot 'preparation.json') (($preflight | ConvertTo-Json -Depth 8) + "`n")
if (-not $Install) {
    Write-Output "Preparation terminee : $smokeRoot. Aucun plugin installe, aucune authentification ou inference lancee."
    return
}

$marketplaceResult = Invoke-IsolatedCli @('plugin','marketplace','add',$smokeRoot,'--json') $stateRoot $smokeRoot | ConvertFrom-Json
if ($marketplaceResult.marketplaceName -ne 'smoke-dev6') { throw 'Marketplace resolue inattendue.' }
$installResult = Invoke-IsolatedCli @('plugin','add','collectivite-territoriale@smoke-dev6','--json') $stateRoot $smokeRoot | ConvertFrom-Json
if ($installResult.name -ne 'collectivite-territoriale' -or $installResult.marketplaceName -ne 'smoke-dev6') { throw 'Identite installee inattendue.' }
$installedPath = [IO.Path]::GetFullPath([string]$installResult.installedPath)
Test-ChildPath $stateRoot $installedPath
$installedManifest = Get-Content -LiteralPath (Join-Path $installedPath '.codex-plugin/plugin.json') -Raw | ConvertFrom-Json
if ($installedManifest.version -ne '1.2.0-dev.6') { throw 'Version installee differente.' }
foreach ($entry in $verifiedFiles) {
    $installedFile = Join-Path $installedPath $entry.path
    if (-not (Test-Path -LiteralPath $installedFile -PathType Leaf)) { throw "Fichier installe absent : $($entry.path)" }
    if ((Get-FileHash -LiteralPath $installedFile -Algorithm SHA256).Hash.ToLowerInvariant() -ne $entry.sha256) { throw "Fichier installe different : $($entry.path)" }
}
$listing = Invoke-IsolatedCli @('plugin','list','--marketplace','smoke-dev6','--json') $stateRoot $smokeRoot | ConvertFrom-Json
$installedEntries = @($listing.installed | Where-Object { $_.name -eq 'collectivite-territoriale' -and $_.marketplaceName -eq 'smoke-dev6' })
if ($installedEntries.Count -ne 1 -or -not $installedEntries[0].installed -or -not $installedEntries[0].enabled) {
    throw 'Plugin isole non confirme installe et enabled par la liste effective.'
}
$receipt = [ordered]@{
    created_at = [DateTime]::UtcNow.ToString('o')
    candidate_commit = $frozen.candidate_commit
    installed_manifest_version = $installedManifest.version
    installed_path = $installedPath
    installed_files_verified = $verifiedFiles.Count
    runtime_files_verified = $runtimeCount
    installed = $true
    mcp_configured_disabled = $true
    mcp_actual_exposure_verified = $false
    actual_plugin_activation_verified = $false
    inference_launched = $false
    authentication = 'not_established_no_credentials_copied'
    measured = $false
    release_ready = $false
}
Write-NewUtf8 (Join-Path $smokeRoot 'installation.json') (($receipt | ConvertTo-Json -Depth 6) + "`n")
Write-Output "Installation locale isolee terminee : $smokeRoot. Le chargement dans une nouvelle session et l'authentification restent a observer ; aucun modele lance."
