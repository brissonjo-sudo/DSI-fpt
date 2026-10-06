# Candidat correctif de la PR 5 — 2026-10-06

Les brouillons de Claude sont réconciliés avec le socle complet de la branche
de reprise. Leurs apports retenus portent sur les responsabilités, les preuves
à exiger d'un service mutualisé ou externe et les contrôles de réversibilité.
Les conclusions figées sur NIS2 ne sont pas reprises.

Le runtime devient **0.2.1 candidat** : STOP dès le premier message visible,
activation effective de recherche-juridique sur déclencheur, retrait intégral
des assertions sans preuve primaire, attribution explicite du fond juridique,
exigences DPO reçues avant validation, reprise métier et retour arrière avant
clôture de la source. Le titre de journalisation ne provoque plus de faux délai.
Les écarts autonomes de restitution et clôture sont aussi traités : absence
de développement juridique après une bascule sans rôle chargé, objet incident
nommé et réouverture des garde-fous prévue si l'expertise est contredite.
La première mesure native corrigée a aussi révélé une tentative de lecture
du cache de maintenance non distribué : les renvois d'exécution vers ce cache
sont retirés, et sa frontière avec le paquet runtime est désormais explicite.

Les mesures anciennes restent historiques et ne qualifient pas ce candidat.
La campagne de coactivation doit figer ce nouveau runtime, ses sources et ses
overlays avant tout appel, puis utiliser des jugements indépendants nouveaux.
Les tests logiciels ne remplacent ni cette campagne, ni la relecture DSI/RSSI,
ni les validations juridique et métier. Aucune publication de version n'est
autorisée par ce document.
