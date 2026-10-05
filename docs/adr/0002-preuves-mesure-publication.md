# ADR-0002 — Rattacher la mesure au runtime et séparer les prérequis

Statut : adopté dans le cadre de l'exécution du cadrage validé.
Date : 2026-10-05.

## Contexte

Le patron DirFi prépare une suite figée et deux rôles isolés. Le titre de
version seul ne garantit pas que deux répondants ont lu les mêmes branches.
Une synthèse de verdicts ne constitue pas une relecture technique humaine.

## Décision

Conserver le protocole en aveugle, empreinter tous les fichiers distribués,
figer barème et prompts, lier chaque jugement à l'empreinte de la réponse et
faire calculer le seuil (25 réussites et aucun échec des huit cas critiques).
Ne pas attribuer de score aux dossiers préparés sans réponses et jugements.
Préparer les dossiers répondants avec le seul runtime et les prompts ; les
juges reçoivent uniquement prompt, réponse, attendus et barème.

La montée à la v1.0.0 requiert aussi la revue du praticien prévue au cadrage.
L'intégration au plugin vient ensuite, avec synchronisation figée et mesure
de coactivation. La version de travail achevée est v0.2.0.

## Conséquences

Une correction runtime invalide l'usage du score antérieur pour la nouvelle
version. Les preuves anciennes restent historiques et ne sont pas réécrites.
Le packaging de test sert au portage ; il n'ajoute pas de canal d'installation
concurrent au plugin agrégateur.
