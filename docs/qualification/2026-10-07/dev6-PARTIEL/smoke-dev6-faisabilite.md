# Faisabilité du smoke Codex — candidat 1.2.0-dev.6

Contrôle du 7 octobre 2026. Consultation documentaire et inspection locale uniquement : aucun plugin installé, aucune configuration modifiée, aucune authentification lancée, aucun appel juridique, aucune mesure comportementale.

## Conclusion

Une voie de smoke avec installation locale dans un **état Codex isolé** est documentée : marketplace local distinct, installation par le gestionnaire de plugins, nouvelle session Codex et vérification des fichiers réellement exposés. Elle n'a pas été exécutée. Le smoke ne peut pas être obtenu en demandant aux sous-agents de cette session de lire le worktree : leur catalogue expose actuellement le plugin 1.1.1. Aucune option `--plugin-dir` n'apparaît dans l'aide locale consultée ; aucune API de rechargement à chaud de ce catalogue n'est établie par les sources consultées.

L'entrée `.agents/plugins/marketplace.json` du candidat pointe vers **GitHub, ref `main`**. L'installer telle quelle ne prouverait pas l'activation de dev.6. Il faut un catalogue de smoke distinct pointant vers une copie locale vérifiée, sans modifier l'inventaire gelé dev.6.

Codex prend en charge l'invocation explicite par `/skills` ou mention `$`, ainsi que la sélection implicite par description. La documentation ne demande pas l'outil `Skill` de Claude Code. Le candidat contient pourtant encore l'expression « via Skill ». Un smoke Codex doit observer le mécanisme Codex réel ; il ne faut ni inventer une invocation Claude, ni convertir après coup un invariant exigeant littéralement cette invocation en succès. [Build skills](https://learn.chatgpt.com/docs/build-skills)

## Constats locaux

| Élément | Constat |
| --- | --- |
| Exécutable | `C:\Users\Krn\AppData\Local\OpenAI\Codex\bin\8aaf1547b825b104\codex.exe` |
| Version exécutée | `codex-cli 0.160.0` |
| Candidat | `Collectivite-corrections-pr5/.codex-plugin/plugin.json` : `1.2.0-dev.6` |
| Source du gel | `3f0df285898cf1e36d1ddda8d85d0c4cd5e0903b`, fichier `docs/qualification/gel-dev6-non-mesure.json` |
| Qualification du candidat | `measurement_status=not_measured`, `release_ready=false`, `codex_smoke.status=not_established` |
| Cache existant | `C:\Users\Krn\.codex\plugins\cache\collectivite-territoriale\collectivite-territoriale\1.1.1\` ; manifeste `1.1.1` |
| Configuration utilisateur | `plugins."collectivite-territoriale@collectivite-territoriale".enabled=true` ; aucune politique MCP spécifique à cette entrée relevée |
| Serveur distribué | Nom `droit-francais` dans `.mcp.json` ; configuration et secrets non reproduits |
| État courant | `CODEX_HOME` absent des variables d'environnement ; existence de `~/.codex/auth.json` constatée, **contenu non lu et validité non testée** |

Commandes réellement exécutées, toutes terminées avec code 0 :

```powershell
& 'C:/Users/Krn/AppData/Local/OpenAI/Codex/bin/8aaf1547b825b104/codex.exe' --version
& 'C:/Users/Krn/AppData/Local/OpenAI/Codex/bin/8aaf1547b825b104/codex.exe' --help
& 'C:/Users/Krn/AppData/Local/OpenAI/Codex/bin/8aaf1547b825b104/codex.exe' plugin --help
& 'C:/Users/Krn/AppData/Local/OpenAI/Codex/bin/8aaf1547b825b104/codex.exe' plugin add --help
& 'C:/Users/Krn/AppData/Local/OpenAI/Codex/bin/8aaf1547b825b104/codex.exe' plugin list --help
& 'C:/Users/Krn/AppData/Local/OpenAI/Codex/bin/8aaf1547b825b104/codex.exe' plugin marketplace list --help
& 'C:/Users/Krn/AppData/Local/OpenAI/Codex/bin/8aaf1547b825b104/codex.exe' exec --help
```

Des lectures JSON/TOML ciblées ont fourni le tableau. L'intégralité de `config.toml`, les URL MCP et les credentials n'ont pas été affichés. Les commandes `plugin list`, `plugin add` et `marketplace add` n'ont pas été lancées ; seules leurs aides l'ont été.

## Voie de smoke à préparer

1. Créer un dossier de smoke neuf sous le workspace, avec un répertoire d'état Codex neuf et préexistant. Copier le candidat et contrôler les SHA-256 contre le gel dev.6. Ne pas ajouter le catalogue de smoke dans cette copie gelée.
2. Créer, à la racine du dossier de smoke, `.agents/plugins/marketplace.json`, avec un nom distinct tel que `smoke-dev6` et une source locale `./plugin-dev6`. Une marketplace de dépôt rend le plugin découvrable ; l'activation peut être limitée au projet. Le gestionnaire utilise une copie installée en cache : il faut en vérifier les bytes, pas seulement le chemin source. [Package your plugin](https://developers.openai.com/plugins/build/plugins)
3. Lancer chaque commande dans un processus enfant dont `CODEX_HOME` désigne le répertoire d'état de smoke, sans changer le profil PowerShell ni l'état utilisateur courant. Cette variable est la racine documentée de configuration, authentification, logs et sessions. Employer `--no-daemon` pour le futur lancement de session afin d'éviter le serveur partagé existant. L'isolation des états doit être vérifiée ; elle ne supprime pas les politiques système ou gérées. [Environment variables](https://learn.chatgpt.com/docs/config-file/environment-variables)
4. Avant toute installation, configurer le MCP distribué `droit-francais` comme désactivé dans cette configuration isolée. La clé documentée est `plugins.<plugin>.mcp_servers.<server>.enabled=false` ; utiliser l'identifiant résolu du plugin de smoke et vérifier ensuite son exposition effective. L'activation de plugin utilise le sélecteur `plugin-name@marketplace-name`. [Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference)
5. Installer uniquement dans cet état isolé avec les commandes ci-dessous. Capturer le résultat JSON et contrôler version, source, `installedPath`, état enabled et tous les SHA-256 runtime du cache installé. Ce sont des commandes futures **non exécutées** ; chaque processus doit recevoir l'environnement isolé défini à l'étape 3. [Developer commands](https://learn.chatgpt.com/docs/developer-commands)

```powershell
codex plugin marketplace add '<DOSSIER_SMOKE_ABSOLU>' --json
codex plugin add collectivite-territoriale@smoke-dev6 --json
codex plugin list --marketplace smoke-dev6 --json
codex --no-daemon --cd '<DOSSIER_SMOKE_ABSOLU>' --sandbox read-only
```

Catalogue proposé, non créé :

```json
{
  "name": "smoke-dev6",
  "plugins": [{
    "name": "collectivite-territoriale",
    "source": {"source": "local", "path": "./plugin-dev6"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_USE"},
    "category": "Productivity"
  }]
}
```

6. Démarrer une **nouvelle** session avec le plugin activé, inspecter `/skills` puis les skills effectivement chargés. L'authentification OpenAI de cet état isolé reste une condition non satisfaite : l'existence d'une authentification dans l'état utilisateur ne prouve pas sa disponibilité dans cet autre état. Ne pas copier `auth.json`, lire ou exporter ses tokens pour contourner cette condition. Aucune auth n'a été testée ou transmise pendant ce contrôle. [Authentication](https://learn.chatgpt.com/docs/auth)
7. Exécuter des requêtes directes, indirectes, négatives et de frontière, avec un transcript neuf par cas. Un smoke technique et un cas dégradé sans sources suffisent d'abord pour éprouver la découverte, le chargement, l'ordre STOP et l'abstention. Cette étape ne qualifie pas le fonctionnement nominal du MCP désactivé. Un futur test nominal et une authentification juridique forment une étape distincte. [Connect and test your plugin](https://developers.openai.com/plugins/deploy/connect-chatgpt)

## Critères mesurables

| Contrôle | Succès attendu | Preuve |
| --- | --- | --- |
| Identité | Sélecteur de smoke, manifeste dev.6 et runtime identiques au gel | Résultat `plugin add/list`, chemin du cache, SHA-256 |
| Isolation | Aucun fichier ajouté/modifié dans l'état utilisateur ; état de smoke distinct | Inventaires avant/après, racines résolues |
| Catalogue de session | Les six skills proviennent du cache dev.6 ; aucune substitution 1.1.1 | Catalogue de la nouvelle session, chemins et hashes |
| Invocation explicite | Skill choisi via la surface Codex `/skills` ou `$` et instructions réellement chargées | Transcript natif et bytes chargés |
| Invocation implicite | Requête métier sélectionne le bon skill sans indication du nom | Transcript distinct ; ordre et resources observés |
| Cas purement technique | DSI sélectionné sans activation juridique superflue | Transcript et liste des appels |
| Dégradé | Serveur juridique absent/désactivé, abstention au lieu d'une règle non vérifiée | Catalogue outils et réponse |
| STOP | Premier texte substantiel affiche STOP dans un cas nécessitant ce garde-fou | Chronologie native ; pas uniquement la réponse finale |
| Portée | Aucun score antérieur transféré ; barème et mécanisme d'activation non réécrits après exécution | Protocole daté, preuves brutes, juge séparé |

Cette préparation ne constitue pas un smoke réussi et ne change pas `release_ready=false`. La voie isolée est supportée par les mécanismes documentés, mais l'installation, l'exposition effective, l'authentification de la nouvelle session et les réponses demeurent à observer.

## Script révisable fourni

`smoke-dev6-isole.ps1` est fourni à la racine du workspace. Il n'a pas été exécuté.

```powershell
# Lecture du gel, hashes et aides CLI uniquement ; aucun dossier créé.
.\smoke-dev6-isole.ps1

# Prépare un dossier neuf, un état Codex isolé et un catalogue local, sans installer.
.\smoke-dev6-isole.ps1 -Prepare

# Prépare un AUTRE dossier neuf puis installe dans cet état isolé uniquement.
# Cette commande n'a pas été exécutée.
.\smoke-dev6-isole.ps1 -Install
```

Les modes de préparation copient les **213 fichiers du gel, dont 166 runtime**, plus l'icône d'interface avec un hash complémentaire distinct du gel. Ils conservent les bytes du candidat, mettent le catalogue de smoke à l'extérieur de cette copie et refusent tout écrasement. Le mode d'installation vérifie le cache installé contre ces hashes et capture un reçu séparant installation et activation. Chaque processus enfant reçoit son propre `CODEX_HOME` et `CODEX_SQLITE_HOME` ; le profil utilisateur et les variables du processus parent restent intacts. Aucun secret d'inférence transmis par variable d'environnement, aucun `auth.json` ou `config.toml` global copié, aucun modèle choisi, aucune session de modèle lancée.

Le script n'est pas un lanceur de campagne. Après l'installation, l'authentification d'une nouvelle session et son catalogue devront être observés séparément. La commande de démarrage manuel fournie plus haut doit recevoir le même état isolé ; la lancer dans le terminal utilisateur ordinaire réutiliserait l'état utilisateur courant et invaliderait cette isolation.
