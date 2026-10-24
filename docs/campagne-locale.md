# Campagne locale DSI-fpt v0.2.0 — Claude ou Codex

Le kit est préparé, sans réponse, jugement ni score. Il contient les 28 cas
figés, leur barème et les 30 fichiers du runtime v0.2.0. Le lanceur réalise
56 appels successifs : un répondant et un juge par cas, chacun dans un
processus et un dossier temporaire neufs. Il reprend les étapes terminées
après contrôle de leurs preuves.

## Préparer le poste

Python 3.11 ou ultérieur suffit, sans bibliothèque tierce. Installer et
connecter normalement la CLI choisie ; son état local doit être inscriptible.
Le lanceur utilise cette connexion sans copier ni modifier ses identifiants.
Les commandes réelles consomment les appels du compte ; `--dry-run` n'en fait
aucun. Ne lancer qu'une commande de campagne à la fois dans un même kit.

Les réponses, jugements et traces sont écrits en UTF-8 avec fins de ligne LF,
y compris sous Windows : les octets conservés correspondent aux empreintes
contrôlées à la reprise. Utiliser un kit régénéré avec ce correctif ; ne pas
modifier les anciennes preuves pour rendre leurs empreintes compatibles.

Claude Code doit prendre en charge `--restricted` (à partir de v2.1.248),
`--no-session-persistence` et `--output-format stream-json`. La CLI Codex doit
prendre en charge `exec --ephemeral --ignore-user-config --json` et
`--output-last-message` ; vérifier `codex exec --help`. Une option inconnue
arrête le cas sans verdict. Les arguments Claude suivent la
[référence officielle](https://code.claude.com/docs/en/cli-reference) ; les
arguments Codex ont été contrôlés sur la CLI de l'environnement de préparation.

Extraire l'archive, puis ouvrir un terminal **dans le dossier extrait**,
celui qui contient `kit.json`, `runtime/`, `scripts/` et `resultats/`.
Choisir les modèles accessibles sur le compte, de préférence leurs
identifiants complets. Remplacer les valeurs entre guillemets ci-dessous :
ce sont des paramètres à renseigner, pas des identifiants de modèle.

## Contrôler sans appeler de modèle

Pour Claude :

```sh
python scripts/mesure_locale.py run --kit . --engine claude --responder-model "MODELE_CLAUDE" --judge-model "MODELE_JUGE" --web --dry-run
```

Pour Codex :

```sh
python scripts/mesure_locale.py run --kit . --engine codex --responder-model "MODELE_CODEX" --judge-model "MODELE_JUGE" --web --dry-run
```

Cette commande contrôle runtime, suite, barème, prompts et scripts, puis
affiche les 28 cas et les 56 appels prévus. Elle n'exige pas la CLI installée
et ne crée aucune réponse. Les empreintes détectent les modifications
accidentelles ; elles ne constituent pas une signature de l'archive.

## Lancer puis reprendre

Commencer par le cas critique incident cyber, pour vérifier la connexion,
l'accès aux fichiers et les traces avant la campagne complète :

```sh
python scripts/mesure_locale.py run --kit . --engine claude --responder-model "MODELE_CLAUDE" --judge-model "MODELE_JUGE" --web --cases cas-21
```

Puis lancer l'ensemble en gardant exactement les mêmes paramètres :

```sh
python scripts/mesure_locale.py run --kit . --engine claude --responder-model "MODELE_CLAUDE" --judge-model "MODELE_JUGE" --web
```

Pour Codex, remplacer `--engine claude` par `--engine codex` et renseigner
les modèles Codex. Utiliser **une copie neuve de l'archive par moteur ou
configuration**. Changer de moteur, modèle, accès web ou version CLI pendant
une reprise est refusé. Une CLI mise à jour impose donc une nouvelle campagne.

`--web` demande les outils web au répondant ; le juge n'en reçoit pas.
Sans cette option, le répondant applique le mode dégradé du skill et Codex
désactive explicitement sa recherche web. Les deux modes doivent être
signalés séparément. Un outil configuré ne prouve pas qu'une source a été
consultée : vérifier les appels et résultats dans les traces.

Un appel a un délai par défaut de 900 secondes, ajustable avec `--timeout`.
Après échec, limite de compte ou interruption, relancer la même commande.
Les réponses et jugements terminés et intacts sont conservés ; seul un rôle
inachevé est rappelé. Une reprise peut ainsi porter le nombre total d'appels
au-delà de 56. Un jugement invalide reste dans la sortie brute, sans verdict
attribué par le script. Ne pas corriger manuellement une réponse ou un
jugement pour poursuivre : les preuves ne correspondraient plus.

## Séparation des contextes et limites

Le répondant reçoit `SKILL.md` complet dans son entrée et les fichiers
runtime dans `.claude/skills/dsi-fpt/` ou `.agents/skills/dsi-fpt/`. Il ne
reçoit ni attendus, ni barème, ni autres cas, ni documents de conception.
L'entrée du skill est donc fournie explicitement même si sa découverte
automatique par la CLI n'est pas disponible. Le juge reçoit uniquement
question, réponse, attendus du cas et barème ; son dossier est vide.
Le lanceur ne réutilise aucune conversation.

Claude utilise le mode restreint, les outils de lecture et, si demandé,
les outils web, sans serveur MCP personnel. Codex ignore la configuration
utilisateur et utilise son sandbox en lecture seule. Cette séparation des
entrées et des dossiers **n'est pas une isolation complète du système** :
le sandbox Codex n'interdit pas toutes les lectures extérieures. Les
politiques administrées, instructions globales ou paramètres imposés par
le poste peuvent encore affecter les CLI. Exécuter depuis un environnement
de mesure propre et contrôler les traces avant de retenir le score.

Les preuves établissent la livraison du skill au répondant ; elles ne
prétendent pas attester une invocation automatique de l'outil Skill.
Les sorties brutes permettent d'examiner les fichiers lus, outils utilisés
et modèle effectif lorsqu'ils sont exposés par la CLI. Les aliases demandés
sont conservés, sans être présentés comme une identité effective vérifiée.
Le juge sans web ne vérifie pas indépendamment les sources citées : le
contrôle de provenance passe aussi par cette revue des traces.

## Récupérer les preuves

Chaque dossier `resultats/cas-XX/` contient le prompt, puis `response.md`,
`judgment.json`, les sorties stdout/stderr et une preuve d'exécution par
rôle. Les empreintes relient le jugement à la réponse, et chaque sortie
aux entrées et traces brutes. `resultats/execution.json` conserve moteur,
modèles demandés, version CLI et mode web. Les durées sont mesurées ; les
tokens ne sont jamais estimés et restent dans les sorties CLI disponibles.

Après les 28 cas complets, le lanceur contrôle les 56 preuves et produit
`resultats/summary.json`. Le seuil est au moins 25 réussites et aucun échec
critique. Le résultat reste à examiner avec les traces ; la publication
reste conditionnée à la relecture DSI/RSSI et aux contrôles du plugin.
Un sous-ensemble ne produit pas de score global.

Pour transmettre la campagne, zipper **le dossier extrait complet** après
exécution, incluant `kit.json`, runtime, scripts et résultats. Conserver les
sorties brutes ; vérifier qu'aucune configuration personnelle ou donnée
réelle n'y a été ajoutée. Cette archive permet de contrôler les empreintes
et de reprendre la synthèse. Ne pas remplacer le dossier préparé du dépôt
par des résultats d'une autre version du runtime.

## Regénérer le kit depuis le dépôt

Le dossier préparé existant peut être exporté une seule fois vers une
destination neuve :

```sh
python scripts/mesure_locale.py export --run-dir tests/runs/codex-v0.2.0-r1 --output dist/campagne-dsi-v0.2.0
```

L'export vérifie le runtime courant contre le manifeste puis produit le
dossier autonome et son `.zip`. Il n'effectue aucun appel. Si le runtime
change, préparer d'abord un nouveau run avec `eval_suite.py prepare`, puis
exporter vers une nouvelle destination. La licence CC-BY-SA-4.0 du skill
est incluse dans le kit.
