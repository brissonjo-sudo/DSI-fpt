# Corrections et preuves du 6 octobre 2026

La source DSI `704e5dd6a3d15994ed431b23585aabd72086ca75` réussit les 28 cas
du barème inchangé, dont huit critiques. 56 rôles frais retenus, quatre rôles
préprotocole exclus et conservés, un lancement refusé sans rôle créé.
Les 28 lectures de questions, 56 écritures et 870 empreintes runtime ont été
contrôlées. Le message initial chiffré du fournisseur n'est pas attesté en clair.
Les questions sont fictives ; aucune récupération extérieure de droit n'a eu
lieu dans la campagne autonome. La revue humaine reste ouverte.

- `rapport-28-cas.md` et `summary.json` : résultats et périmètre exact.
- `Presentation-DSI-corrections-2026-10-06-v5.pptx` : 11 diapositives, tableaux
  et graphique natifs ; package, géométrie, données et réimport contrôlés.
  Les 11 rendus ont été relus ; aucune ouverture PowerPoint native n'est attestée.
- `Preuves-corrections-DSI-coactivation-2026-10-06.zip` : archive portable des
  28 cas DSI et de la tentative plugin r6 dev.3 sur `f002356`.
  Elle contient les sources réellement mesurées, les traces filtrées et le
  vérificateur hors ligne. Son extraction relocalisée passe ; une altération
  réelle de réponse est rejetée.
- `dsi-fpt-0.2.1-704e5dd.zip` : paquet autonome de 30 fichiers conformes au runtime.

La coactivation est séparée : dev.3 a produit un APJA échoué sur une catégorie
restaurée à tort malgré le texte reçu, et quinze refus de quota non jugés.
Le dernier correctif plugin dev.4 `36cbbd67fa02240cb723f4236c25d4340bcd85ee`
renforce la concordance mot à mot, les BASCULE et le cadrage technique.
Il reste entièrement non mesuré ; aucun résultat de dev.3 ne lui est transféré.
Les mesures historiques restent dans le dépôt plugin.

Pour contrôler l'archive : extraire dans un dossier neuf, puis exécuter
`python verifier_archive_corrigee.py` à sa racine. Aucun Git, réseau ou modèle
n'est appelé par ce contrôle. Les contrôles d'intégrité n'établissent pas
une qualification complète de coactivation.

`release_ready=false`. Revue DSI/RSSI, revue juridique, smoke Codex et nouvelle
campagne plugin restent requis. Les PR demeurent brouillons.
