# Changelog — `dsi-fpt`

Versionnage sémantique **MAJEUR.MINEUR.PATCH**.

- **MAJEUR** — changement d'architecture ou de périmètre, rupture de compatibilité.
- **MINEUR** — nouvelle branche, nouvel objet, nouveau gabarit, nouvelle frontière.
- **PATCH** — correctif de fond, précision, mise à jour de source.

Le skill reste en **0.x tant qu'il n'a pas passé le seuil de mesure** (au moins
25 réussites sur 28 cas, aucun échec sur les cas critiques). La **1.0.0** est
la première version mesurée au seuil.

---

## [0.2.0] — 2026-10-05 — rédaction achevée, non mesurée

### Ajouté

- Les 12 branches décisionnelles, les 6 objets et les 5 gabarits interactifs
  du cadrage validé, avec frontières opposables et renvois aux garde-fous.
- Adaptation des scripts de packaging et d'évaluation du patron DirFi :
  cache exclu, suite et barème figés, runtime empreinté, jugement lié à la
  réponse et seuil calculé avec blocage des échecs critiques.
- Suite de 28 cas, dont les 8 critiques du cadrage, et 12 tests de régression
  de l'outillage. Ces tests logiciels ne constituent pas la mesure du skill.
- CI Python sans dépendance tierce, métadonnées Codex et index de maintenance.
- Fiche de relecture praticien et état d'avancement traçant les prérequis.

### Limites

- Aucune campagne comportementale exécutée ; aucun score déclaré.
- Relecture DSI/RSSI à organiser par l'auteur avant la v1.0.0.
- Les textes non vérifiés restent réservés ; aucune extension juridique du
  socle ni intégration au plugin n'est présumée par cette rédaction.

## [0.1.0] — en construction — non mesurée

### Ajouté

- Cadrage validé par l'auteur (`docs/cadrage.md`) et décision d'architecture
  (`docs/adr/0001-adoption-patron-dirfi-fpt.md`).
- Socle de sources vérifié le 2026-10-05, en quatre lots (`docs/socle/`), avec
  une colonne d'applicabilité aux collectivités ; registre unique des
  identifiants (`references/references-verifiees.md`) ; cache des valeurs
  datées, hors runtime (`references/cache-valeurs.md`).
- `SKILL.md` : routeur, deux garde-fous (incident cyber, surveillance de
  personnes), frontières opposables avec `dpo-ct`, `drh-fpt`, `dpm-fpt`,
  `dirfi-fpt` et la commande publique.
- Routeur `references/analyse-situation.md`, gabarits de branche et d'objet.
- `scripts/validate_repo.py` : inventaire, structure à 12 et 6 sections,
  invariants de garde-fou, identifiants et valeurs hors registre, pointeurs
  inter-dépôts, anti-PII.

### Limites connues

- Non mesuré. Non relu par un praticien DSI ou RSSI.
