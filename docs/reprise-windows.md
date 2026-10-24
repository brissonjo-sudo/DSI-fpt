# Reprise locale Windows — 2026-10-06

Session reprise : `01a10cdc-e46c-7686-a104-bd3f4802206b`.
Source : PR #3, commit `e4a2439f59b61d44befa3a4f473791a38aa86f7b`.
Branche locale : `codex/reprise-campagne-windows`.

La décision antérieure était de préparer la campagne pour le poste Claude/Codex.
Le dépôt a été cloné dans le workspace de cette session, sans modifier les
checkouts existants. Aucun appel modèle, push ou fusion réalisé.

## Correctif de portabilité

Sur Windows, deux des 26 tests échouaient avec `Preuve modifiée` lors de la
reprise ou du contrôle final d'une campagne simulée. L'écriture texte traduisait
les LF en CRLF alors que les empreintes étaient calculées sur les octets LF.
Le lanceur impose désormais `newline="\n"` à son écriture atomique UTF-8.
Le runtime du skill et les attendus restent ceux du manifeste préparé.

## Vérifications locales

- 26 tests logiciels réussis avec CLI simulées.
- 1 048 contrôles statiques réussis, aucun avertissement.
- Packaging : 30 fichiers runtime.
- Archive extraite : contrôles `--dry-run` Claude et Codex réussis ;
  28 cas et 56 appels prévus chacun, aucun appel effectué.
- `git diff --check` réussi.
- CLI présentes : Codex 0.160.0 et Claude Code 2.1.288.
  Leurs aides exposent les options nécessaires ; leur connexion et leur
  comportement réel n'ont pas été testés par ces contrôles.

Python utilisé :
`C:\Users\Krn\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.

Archive : `dist/campagne-dsi-v0.2.0-windows.zip`.
SHA-256 : `fb615c6a7e1fb7700cb3536004433ab522062dba552e11c14bb6a2faabccdabf`.

## Suite

Choisir le moteur et les identifiants de modèles répondant/juge, puis lancer
le cas pilote `cas-21` selon `campagne-locale.md`. Garder les mêmes paramètres
pour les 28 cas. Utiliser une copie neuve du kit pour chaque configuration.
La v0.2.0 reste non mesurée. Le contrôle des traces, la relecture DSI/RSSI et
les contrôles d'intégration au plugin restent à réaliser avant publication.
