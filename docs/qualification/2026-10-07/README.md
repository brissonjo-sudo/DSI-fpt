# Bilan DSI et coactivation au 7 octobre 2026

La campagne native Codex R2 est achevée : seize réponses et seize juges frais,
soit 32 rôles distincts ; 4 réussites, 6 échecs et 6 cas bloqués. Les 124 exigences atomiques
donnent 107 vraies, 6 fausses et 11 indéterminées.
Onze cas imposent les rôles et cinq permettent leur sélection spontanée.

Cette mesure porte exclusivement sur dev.5 au commit candidat
`3f0d34bd068e3427edc9335a4f1415aaf1c7c98d`, runtime `ebeee944e878b11177d5ccb85d9043c4c97260a9`. L'audit indépendant rejoue les appels
natifs, les lectures par fragments, les réponses et les jugements ; il contrôle
les 211 fichiers gelés, dont 166 fichiers de runtime. Les messages initiaux
opaques et l'isolation complète du système partagé ne sont pas vérifiés.
Les séquences imposées et le rappel initial de STOP ne démontrent pas,
à eux seuls, un déclenchement autonome par le plugin.

Les agents ont chargé les fichiers candidats. L'activation réelle du plugin
n'est pas démontrée ; une exigence littérale « via Skill » ne peut donc pas
être validée par cette seule lecture. Les sources retrouvées, leur pertinence
pour chaque affirmation et leur vigueur sont des contrôles distincts.
Certains retours de sources sont tronqués ; leur transport réel est conservé,
sans prétendre que leur contenu complet a été disponible au répondant.
La tentative d'écriture hors périmètre du cas spontané RSSI/RH a été refusée
par Windows, conservée et classée comme échec technique. Aucune réponse
n'a été réécrite ni relancée pour améliorer le score.

Le candidat courant `1.2.0-dev.6` est distinct et **non mesuré**. La campagne dev.5 reste historique et aucun de ses scores ne lui est transféré. Un nouveau gel, une mesure propre à ses octets et son smoke Codex restent nécessaires.

Cette campagne a été exécutée ici avec les sous-agents natifs Codex, sans
lancer Claude Code ni exiger son authentification. Les avis humains DSI/RSSI
et juridiques, le smoke du candidat et la qualification de release restent
ouverts ; `release_ready=false`. Ni fusion, ni publication n'est autorisée
par la mesure ou par une CI seule.

Les copies byte-identiques du rapport, de la synthèse, de l'audit final et du
contrôle ZIP sont dans [coactivation-codex-r2](coactivation-codex-r2/rapport.md).
Le reçu `Controle-copie-documentaire.json` donne leurs empreintes SHA-256 et
les empreintes avant/après des README actualisés.

La mesure DSI autonome reste 28/28 sur
`704e5dd6a3d15994ed431b23585aabd72086ca75`, distincte des variantes du plugin.
La mesure partielle dev.4 r7 reste six réponses jugées : une réussite et
cinq échecs, trois nominaux `needs-auth`, un cas interrompu et neuf non exécutés.
Les rapports précédents, le dossier du 6 octobre, les contrôles v6 et
les anciennes archives restent conservés. L'archive DSI/r6 ne contient pas r7.

La présentation v6 et ses contrôles restent historiques : onze diapositives,
quatre tableaux natifs, graphique DSI éditable, six diapositives modifiées
inspectées et cinq rendus identiques à v5. Son SHA-256 est
`0195672e0a664ec3baecbc89e6cf4d80b03a5814464182bfd591a4b1c5d9f123`.
L'ouverture PowerPoint native et les revues humaines restent non établies.
La présentation finale et son contrôle doivent être identifiés par leurs
propres fichiers et empreintes après génération ; aucun contrôle v6 ne leur
est transféré.

Les preuves sont dans la
[PR plugin #11](https://github.com/brissonjo-sudo/collectivite-territoriale/pull/11).
Le présent bilan et la présentation sont dans la
[PR DSI #5](https://github.com/brissonjo-sudo/DSI-fpt/pull/5).
Les deux PR restent brouillon. La CI doit être vérifiée pour les nouveaux SHA
après push ; aucun ancien résultat de CI n'est attribué au prochain commit.

La [présentation finale v7](Presentation-DSI-corrections-2026-10-07-v7.pptx) contient onze diapositives, quatre tableaux natifs et le graphique éditable DSI 28/28. Son fichier, ses polices Arial, sa géométrie et son import ont passé leurs contrôles propres. Six rendus modifiés ont été inspectés ; les cinq autres sont identiques pixel par pixel à v6. Les contrôles v7 sont joints. Son SHA-256 est `9d5d672e68376b67064d197aae147b6724bfeb8e44461788dfbe0e57b70c369a`. L’ouverture PowerPoint native et les avis humains restent ouverts.

Le gel et le contrôle statique dev.6, ainsi que le triage hors mesure, sont copiés dans `coactivation-codex-r2`. Le contrôle statique est un snapshot précommit ; le gel indique le commit source réel. L’inventaire v6 historique est conservé séparément. Le reçu documentaire antérieur décrit son instant de copie, avant cette mise à jour finale du README.

L’[archive complète Codex R2](coactivation-codex-r2/Preuves-coactivation-Codex-dev5-r2-2026-10-07.zip) est jointe : 1112 entrées contrôlées, journaux parent privés exclus, SHA-256 `d40b8dbb3513085c0e2eb645547a227d47b1648133ca528b797495b4b3337e13`. Les résultats dev.5 restent inchangés.
