# Diagnostic explicite du contexte Codex — dev.6

**La découverte des six skills du cache dev.6 est confirmée. L'injection complète du SKILL DSI et sa sélection effective ne sont pas établies.** Le marqueur littéral `$collectivite-territoriale:dsi-fpt` est conservé comme simple texte utilisateur dans la sortie ; il ne constitue pas à lui seul une activation.

Une seule tentative de `codex debug prompt-input` a été exécutée dans l'état Codex isolé déjà installé, du **2026-10-07T21:47:36.2006444Z** au **21:47:36.3454101Z**. Code de sortie **0**, aucun timeout, JSON complet de **17 132 octets**, stderr vide. Aucun `login`, aucune TUI, aucun `exec`, aucun `turn/start` ou appel de modèle n'a été demandé. L'authentification n'a pas été relue ; ce diagnostic ne garantit pas l'absence de trafic réseau interne.

Le processus enfant reçoit les racines d'état `CODEX_HOME`/`CODEX_SQLITE_HOME` du smoke et retire les variables d'environnement de type token/secret/password/API key. Il exécute directement le binaire, sans shell intermédiaire ni interpolation du `$`. Les 213 fichiers gelés ont été contrôlés côté candidat et côté cache, plus la configuration isolée : **427 fichiers inchangés avant/après**.

## Preuves et comparaison

| Contrôle | Observation |
| --- | --- |
| Source candidat | `3f0df285898cf1e36d1ddda8d85d0c4cd5e0903b` |
| Version du cache | `1.2.0-dev.6`, marketplace `smoke-dev6` |
| Catalogue | Six entrées `collectivite-territoriale:*` ; alias `r1` résolu au dossier `skills` du cache isolé dev.6 |
| Texte utilisateur | Un message contient exactement les 34 caractères du marqueur demandé |
| DSI source/cache | Bytes identiques ; **36 215 octets**, SHA-256 `072147c7cf481c50ba009b20324a7efaeafa5f6090d40325a7ad24697fb435de` |
| Recherche du fichier complet dans les textes JSON décodés | Aucun match contigu exact UTF-8, dans aucun contenu de message |
| Bloc de skill | Aucun wrapper `<skill>` ou `<skill ...>` observé |
| Sélection/injection explicite complète | Non attestée dans cette commande |
| Usage du modèle, sélection spontanée, validation humaine | Non testés |

La vérification recherche les bytes complets du `SKILL.md`, sans retirer le frontmatter ni normaliser les fins de ligne pour obtenir un succès. Elle vérifie aussi l'intégrité SHA-256 des sorties brutes avant de parser le JSON. Les descriptions du catalogue et le marqueur utilisateur restent distincts des instructions complètes.

Les sorties brutes sont conservées **localement uniquement** dans :

```text
smoke-dev6-isole-20261007-211629-4dc9cd90/diagnostic-explicite-20261007-214736-45f6ee78/
```

| Pièce | SHA-256 |
| --- | --- |
| Script d'exécution `diagnostic-smoke-dev6-explicite.ps1` | `7acda61cf2ff845f1d3954e4c18a8f9c4455cc3e1c963f36a0a1259db7996d27` |
| `stdout.json` | `19b9a473edfe142602df6d6d5cf3e241ed19ca5a3420c91c7dbeed02adfd8ea8` |
| `stderr.txt` vide | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

`execution.json` conserve argv, horodatages, timeout et hashes. Le reçu dérivé `smoke-dev6-explicite-diagnostic-2026-10-07.json` conserve uniquement des faits, noms/chemins de skills et empreintes ; il ne reproduit pas les instructions développeur brutes. `analyser-diagnostic-smoke-dev6-explicite.py` permet de vérifier cette comparaison localement sans relancer Codex.

## Mécanisme documenté et portée

La documentation officielle décrit l'invocation explicite par `/skills` ou `$` et la sélection implicite par description. Cela établit le mécanisme Codex disponible, sans prouver que le marqueur de ce diagnostic a été résolu en skill. [Build skills](https://learn.chatgpt.com/docs/build-skills)

L'aide locale de CLI `0.160.0` expose `codex debug prompt-input [OPTIONS] [PROMPT]`. Cette commande expérimentale rend la liste exacte des entrées visibles au modèle pour diagnostiquer la découverte, le contexte et la construction du prompt. Elle ne propose pas de paramètre structuré `skill` dans l'aide consultée. Ce diagnostic réussi vérifie donc la construction du contexte et son catalogue ; il ne remplace pas un tour de modèle utilisant les instructions. [Developer commands](https://learn.chatgpt.com/docs/developer-commands)

La documentation app-server distingue le marqueur textuel `$<skill-name>` d'un item structuré `skill`, recommandé pour injecter les instructions complètes. Sans cet item, le modèle peut devoir résoudre le nom et lire le skill. Aucun `turn/start` ni item structuré n'a été envoyé ici. Cette distinction explique la limite à tester ensuite ; elle ne permet pas de reconstruire une injection absente de notre sortie. [Codex App Server](https://learn.chatgpt.com/docs/app-server)

Aucun runtime, ancien reçu, configuration ou module gelé n'a été modifié. Aucune relance n'a été faite pour obtenir une injection. Ce résultat ne qualifie ni le comportement métier, ni la coactivation spontanée, ni l'exposition MCP réelle, ni une validation DSI/RSSI ou juridique humaine. `release_ready=false` reste inchangé.
