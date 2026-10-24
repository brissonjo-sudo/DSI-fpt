# ADR-0003 — Campagne locale Claude/Codex

- Date : 2026-10-06
- Statut : adopté pour l'outillage v0.2.0 ; aucune mesure revendiquée

## Contexte

La CLI connectée de l'environnement de préparation échoue avant appel
modèle sur un système de fichiers en lecture seule. L'auteur demande de
préparer la campagne pour son environnement Claude/Codex. Les 28 cas, le
barème et les 30 fichiers du runtime sont déjà figés ; la revue DSI/RSSI
reste un prérequis distinct de publication.

## Décision

Exporter un kit autonome sans configuration personnelle. Réaliser un
processus et un dossier temporaire neufs par rôle et cas, avec fourniture
explicite de SKILL.md et installation native du runtime au répondant.
Le juge reçoit les attendus et le barème sans runtime. Les appels sont
séquentiels et leurs sorties brutes sont conservées. Le script transporte
le verdict du juge, contrôle son format et le lie à la réponse ; il ne
juge pas lui-même.

La reprise refuse un changement de moteur, modèles, outils ou version CLI,
ainsi que l'altération des sorties, entrées ou traces terminées. Seuls les
28 cas complets avec leurs preuves permettent une synthèse. L'activation
automatique native et la provenance des sources ne sont pas déduites des
seules empreintes ; les traces doivent être examinées.

## Conséquences

La mesure peut être exécutée sur le poste de l'auteur sans dépendance
Python tierce. Les tests utilisent exclusivement des CLI simulées et ne
constituent pas une mesure comportementale. Les options d'isolation des
CLI exigent une version compatible. La séparation des contextes et des
répertoires ne garantit pas l'absence d'instructions administrées ou de
lectures extérieures permises par le système. Le mode web est consigné et
ne change pas à mi-campagne. Aucun changement du runtime ni montée de
version ne résulte du seul ajout de ce lanceur.
