# Installation isolée dev.6 — addendum d'exécution

Cet addendum du 7 octobre 2026 complète `smoke-dev6-faisabilite.md` et conserve les reçus initiaux sans modification.

L'agent racine a exécuté `-Prepare`, puis `-Install` dans deux dossiers neufs. Le reçu d'installation est daté **2026-10-07T21:16:32.0054687Z**. Une vérification indépendante en lecture seule à **21:17:50 UTC** a retrouvé les **214 fichiers identiques à l'inventaire de préparation, dont 166 runtime**. Le manifeste installé est `1.2.0-dev.6`, source gelée `3f0df285898cf1e36d1ddda8d85d0c4cd5e0903b`.

| Élément | SHA-256 |
| --- | --- |
| Script `smoke-dev6-isole.ps1` | `6d403f29e984b8e0f74a5f3b925df3b8a50587f97027c4e72d46528743d1b696` |
| Reçu installation | `a3745bb385dae50b6f131a5ad3adafbd7200dc30568f5df011c8ad723ed8d8a3` |
| Configuration isolée après installation | `b4ab3a160d50df5792f937403a4cfde881a1929f2c3d2c0f3216a6ad0cf9a3b6` |
| Catalogue local de smoke | `a00a8af01320077b7fc921d04f80f84e78ffed0c2ae486fc234a9d6a4a334c96` |

Les chemins exacts et les autres empreintes sont conservés dans `smoke-dev6-installation-addendum-2026-10-07.json`. Dossier installé :

```text
C:\Users\Krn\Documents\Codex\2026-10-06\reprends-le-travail-de-cette-session\smoke-dev6-isole-20261007-211629-4dc9cd90
```

La configuration isolée active `collectivite-territoriale@smoke-dev6` et désactive son MCP `droit-francais`. L'exécution racine a vérifié l'entrée effective installée/enabled via `plugin list`. Le script ne conserve pas ce JSON de liste dans `installation.json` ; cet addendum distingue donc ce constat d'exécution de la relecture indépendante du cache et de la configuration. Aucun auth global ni token n'a été lu ou copié par ce contrôle.

**Installation ≠ activation observée.** L'authentification du nouvel état, l'exposition effective des outils MCP, la découverte de skills dans une nouvelle session et leur utilisation par un modèle restent non établies. Aucune inférence n'a été lancée ; `release_ready=false` reste inchangé.

## Diagnostic du contexte disponible, non exécuté

L'aide locale de Codex CLI `0.160.0`, réellement consultée, donne :

```text
Usage: codex debug prompt-input [OPTIONS] [PROMPT]
--image, -i <FILE>...
-c, --config <key=value>
--enable <FEATURE>
--disable <FEATURE>
```

La commande expérimentale `codex debug prompt-input` rend en JSON la liste exacte des entrées visibles au modèle. Elle vise le diagnostic de découverte d'instructions, de contexte et de construction du prompt ; le prompt optionnel est ajouté après le contexte. Elle permettrait d'observer si les descriptions et chemins des skills du cache dev.6 sont présents. Ce rendu serait une preuve de découverte/construction du contexte, sans démontrer que le modèle choisit ou suit un skill. La documentation ne garantit explicitement ni l'absence d'authentification nécessaire, ni l'absence d'accès réseau de cette commande. [Developer commands](https://learn.chatgpt.com/docs/developer-commands)

**Seule l'aide a été exécutée.** Aucun diagnostic de contexte, app-server, session TUI ou appel de modèle n'a été lancé pendant cet addendum. L'aide ne propose pas de drapeau « sans auth » ou « offline » pour `debug prompt-input`. Il n'y a donc pas de résultat réel à qualifier comme découverte réussie sans authentification.

Commande de diagnostic envisagée, à exécuter dans un **processus enfant recevant le même état isolé** :

```text
codex --cd "C:\Users\Krn\Documents\Codex\2026-10-06\reprends-le-travail-de-cette-session\smoke-dev6-isole-20261007-211629-4dc9cd90" debug prompt-input
```

L'agent racine doit décider séparément de ce diagnostic et conserver sa sortie locale brute, sa date, son code de sortie et son hash. Une sortie tronquée ou un besoin d'authentification doit être conservé comme limitation, sans reconstruction ni nouvelle conclusion d'activation.

## Commande exacte après authentification isolée

Le bloc ci-dessous est destiné à l'utilisateur **après authentification de cet état isolé**. Il n'a pas été exécuté. Il lance une nouvelle TUI sans prompt initial, sans choix de modèle et sans serveur partagé. Les variables du terminal parent restent intactes ; aucune lecture de fichier d'authentification n'est nécessaire.

```powershell
$smokeRoot = 'C:\Users\Krn\Documents\Codex\2026-10-06\reprends-le-travail-de-cette-session\smoke-dev6-isole-20261007-211629-4dc9cd90'
$smokeStart = [System.Diagnostics.ProcessStartInfo]::new()
$smokeStart.FileName = 'C:\Users\Krn\AppData\Local\OpenAI\Codex\bin\8aaf1547b825b104\codex.exe'
$smokeStart.Arguments = '--no-daemon --cd "' + $smokeRoot + '" --sandbox read-only'
$smokeStart.WorkingDirectory = $smokeRoot
$smokeStart.UseShellExecute = $false
$smokeStart.EnvironmentVariables['CODEX_HOME'] = Join-Path $smokeRoot 'codex-state'
$smokeStart.EnvironmentVariables['CODEX_SQLITE_HOME'] = Join-Path $smokeRoot 'codex-state'
foreach ($name in @($smokeStart.EnvironmentVariables.Keys)) {
    if ([string]$name -match '(?i)(TOKEN|SECRET|PASSWORD|API_KEY|ACCESS_KEY|AUTHORIZATION)') {
        $smokeStart.EnvironmentVariables.Remove([string]$name)
    }
}
$smokeProcess = [System.Diagnostics.Process]::Start($smokeStart)
$smokeProcess.WaitForExit()
```

L'aide `codex login --help`, consultée sans lancer d'authentification, expose `login`, `status`, `--device-auth`, `--with-api-key` et `--with-access-token`. Une authentification par navigateur de ce même état se prépare avec le même bloc de processus enfant en remplaçant seulement `Arguments` par `login`, sans passer ni copier de token. Cette action est distincte de l'installation et n'a pas été faite ici. Le démarrage interactif Codex demande une connexion lorsqu'aucune session valide n'est disponible. [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

Dans la nouvelle TUI, utiliser `/skills`, sélectionner le skill DSI de ce plugin et contrôler le catalogue avant d'envoyer une requête. Une requête explicite par sélection `$` et une requête implicite dans une autre session donneront deux observations distinctes. Codex documente ces deux mécanismes ; cela ne valide pas rétroactivement l'exigence littérale « via Skill » du barème existant. [Build skills](https://learn.chatgpt.com/docs/build-skills)

La réussite du smoke exige ensuite des traces de chargement/usage rattachées à cette version et à ces hashes. La présence des six fichiers, l'installation et `enabled=true` ne remplacent pas ces traces ni une validation DSI/RSSI ou juridique humaine.
