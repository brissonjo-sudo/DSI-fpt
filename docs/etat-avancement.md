# État de reprise — DSI-fpt v0.2.1

## 2026-10-06 — candidat corrigé et nouvelle mesure

Le runtime source `704e5dd6a3d15994ed431b23585aabd72086ca75` a reçu une nouvelle
campagne native r2 : **28 réussites sur 28**, dont les huit cas critiques.
Les 56 rôles retenus sont frais et leurs écritures sont liées aux traces natives.
Quatre tentatives préprotocole sont conservées et exclues ; un lancement refusé
n'a créé aucun rôle. Les 28 questions ont été lues intégralement et les 870
comparaisons d'empreintes runtime sont conformes. Le message initial chiffré du
fournisseur n'est pas déclaré vérifié en clair.

Le seuil autonome est atteint sur cette source. La mesure s'est déroulée sans
récupération extérieure de texte primaire ; elle ne certifie pas le droit.
Le plugin à six variantes locales reste une qualification séparée : la nouvelle
tentative r6 a achevé une réponse, puis quinze cas ont rencontré le quota.
La revue DSI/RSSI, la revue juridique et le smoke Codex restent ouverts.
`release_ready=false` ; le candidat et les PR restent en brouillon.

Le seul cas de coactivation achevé, APJA sur dev.3, échoue sur la concordance
d'une catégorie restituée avec le texte reçu. Un dernier correctif dev.4 est
isolé dans le plugin ; il reste non mesuré et ne reçoit aucun score de dev.3.

Rapport, support de présentation et archive portable sont conservés dans
`docs/qualification/2026-10-06/`. Le commit documentaire final ne remplace pas
le pin du runtime effectivement mesuré. Aucun résultat ancien n'est transféré.

## État antérieur conservé — v0.2.0

Mise à jour : 2026-10-06. Reprise de `claude/redaction-dsi-fpt`, commit `ad3e4ee`,
après cadrage validé et socle de sources. Aucun plan DSI n'a été trouvé dans
le plan historique du plugin ; le cadrage et les ADR gouvernent cette reprise.

| Phase | État | Preuves / suite |
|---|---|---|
| 1. Cadrage | Validé, PR #1 encore ouverte | `cadrage.md`, ADR-0001 |
| 2. Socle | Écrit, PR #2 encore ouverte et empilée sur #1 | Registre et lots historiques ; limites réservées |
| 3. Rédaction | Achevée en v0.2.0 | SKILL, routeur, 12 branches, 6 objets, 5 gabarits |
| 4. Outillage | Achevé et contrôlé | Validation, packaging, évaluation, CI, index, suite de 28 cas |
| 5. Mesure | Préparée, non exécutée | Aucun response.md/judgment.json ni score de campagne |
| 5. Relecture DSI/RSSI | À organiser par l'auteur | Disponibilité confirmée, aucun avis reçu ; fiche dédiée |
| 6. Plugin | En attente des prérequis | Intégration après mesure et revue, puis contrôle de coactivation |

## Contrôles réalisés

Validation statique complète sans mode partiel ni avertissement. Les 26 tests
de l'outillage exercent refus d'une campagne incomplète, altérations de suite,
barème, prompt ou réponse, blocage d'un échec critique, séparation du seuil et
de la publication, packaging sans cache et déterminisme. Ces artefacts
factices restent dans les tests logiciels et ne sont pas une mesure du skill.
Les tests du lanceur local simulent les deux CLI et contrôlent la séparation
des entrées/dossiers, la reprise, les changements de configuration, les
traces altérées et la portabilité de l'archive sans appel modèle.
Packaging : 30 fichiers runtime, aucun cache, test ou document de conception.
Contrôle d'espaces et de conflits : `git diff --check`.

## Limite d'exécution observée

Le clonage par le réseau shell n'a pas abouti ; l'état a été reconstitué via
l'accès GitHub connecté. Le Codex CLI annonce une connexion ChatGPT, mais
`codex --no-daemon exec` échoue avant tout appel de modèle :
« failed to initialize in-process app-server client: Read-only file system ».
Le fichier système en cause n'est pas identifié par ce diagnostic ; aucune
authentification n'a été modifiée et aucune mesure n'est revendiquée.

La campagne doit être lancée dans un environnement où un moteur peut créer
des contextes frais et charger ce runtime. Elle exige deux contextes par
cas, répondant sans attendus et juge sans runtime, selon
`../tests/bareme-cas-de-test.md`. Le dossier préparé conserve les empreintes ;
il ne suffit pas à satisfaire le seuil.

L'auteur a choisi la préparation d'un kit pour son environnement Claude/Codex,
sans campagne de sous-agents ici. Le lanceur et les commandes figurent dans
[`campagne-locale.md`](campagne-locale.md) et l'ADR-0003. Le runtime reste
v0.2.0 avec les mêmes empreintes. Aucune réponse réelle n'a été produite.

Les exécutions GitHub Actions du commit `bcd834e` ont été annulées avant
toute étape de test. Le motif n'a pas pu être récupéré ; ces exécutions
ne démontrent ni succès ni défaut des contrôles locaux.

## Reprendre après la revue

1. Consigner le retour anonymisé dans `relecture-praticien.md`, corriger les
   écarts bloquants et monter la version si le runtime évolue.
2. Préparer une nouvelle campagne pour le runtime corrigé. Ne pas utiliser
   les empreintes d'un dossier antérieur ; ne pas changer les attendus pour
   faire passer les réponses.
3. Exécuter les 28 réponses et jugements isolés, puis la synthèse. Au moins
   25 réussites et aucun échec critique sont requis.
4. Rejouer validation et packaging ; verser les preuves et actualiser les
   métadonnées avant montée à v1.0.0.
5. Intégrer au plugin depuis un commit amont figé, contrôler la synchronisation,
   les manifestes et les frontières de coactivation avec les cinq autres skills.

## Préparation de l'intégration

`dsi-fpt` est le sixième skill distribué (cinquième métier) ; le plugin
conserve son serveur MCP juridique unique. Ajouter au manifeste amont un
commit effectivement mesuré/relu, copier le runtime avec exclusion du cache,
et compléter la couverture de frontières DSI/DPO, DSI/DRH, DSI/DPM et
DSI/DirFi. Ne pas assimiler la fusion des PR de construction à une publication
validée. La version de travail n'est pas annoncée comme une v1 opérationnelle.

## Traçabilité du socle

Les identifiants officiels des lots de travail sont désormais centralisés
au registre conformément à AGENTS.md ; les traces d'origine restent dans
l'historique `ad3e4ee`. Les identifiants non confirmés ou non retenus ont été
retirés des notes de travail. Les lignes et réserves du registre ne sont pas
réétiquetées comme revérifiées dans cette session.
