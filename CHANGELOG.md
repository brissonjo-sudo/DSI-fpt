# Changelog — `dsi-fpt`

Versionnage sémantique **MAJEUR.MINEUR.PATCH**.

- **MAJEUR** — changement d'architecture ou de périmètre, rupture de compatibilité.
- **MINEUR** — nouvelle branche, nouvel objet, nouveau gabarit, nouvelle frontière.
- **PATCH** — correctif de fond, précision, mise à jour de source.

Le skill reste en **0.x tant qu'il n'a pas passé le seuil de mesure** (au moins
25 réussites sur 28 cas, aucun échec sur les cas critiques). La **1.0.0** est
la première version mesurée au seuil.

---

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
