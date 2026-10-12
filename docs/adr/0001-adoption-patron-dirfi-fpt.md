# ADR-0001 — Adopter le patron d'architecture de `dirfi-fpt`

**Statut** : accepté (cadrage validé par l'auteur le 2026-10-05)
**Date** : 2026-10-05

## Contexte

Quatre skills métier territoriaux existent : `dpm-fpt`, `drh-fpt`, `dpo-ct` et
`dirfi-fpt`. Ils sont distribués par le plugin `collectivite-territoriale`
avec `recherche-juridique`. `dpo-ct` renvoie depuis sa création vers un
« futur skill DSI » pour la mise en œuvre technique de la sécurité, et pose le
contrat : le DPO exige, la DSI met en œuvre.

Le métier des systèmes d'information combine deux dimensions : des domaines
thématiques (sécurité, cloud, accessibilité) et des situations récurrentes qui
les traversent (un incident, un projet applicatif, un téléservice).

## Décision

Reprendre l'architecture de `dirfi-fpt`, elle-même issue de `dpm-fpt` :
routeur, branches thématiques, objets métier, gabarits d'écrit ; scripts de
validation, de packaging et d'évaluation ; CI ; `docs/adr/` ; `vault/`.

Écarts assumés par rapport à `dirfi-fpt` :

1. **Pas d'adaptateur `.claude-plugin/` ni de dossier `skills/`.** Le plugin
   agrégateur est le canal de distribution. Une seconde voie d'installation
   serait une seconde copie à maintenir.
2. **Colonne d'applicabilité dans le socle.** Une grande partie du droit et de
   la doctrine du numérique public vise l'État. Chaque référence du socle
   porte donc la mention « applicable aux collectivités : oui, non, sous
   conditions », avec sa source.
3. **Fiches de cadrage par branche avant rédaction.** Les branches seront
   rédigées par plusieurs agents. Chacun part d'une fiche commune (périmètre,
   exclusions, renvois, références autorisées), pour éviter doublons et
   contradictions.

## Conséquences

- Coût de maintenance élevé : 12 branches, 6 objets, 5 gabarits, 3 scripts,
  28 cas de test.
- Le droit du numérique évolue vite : le socle est daté et sa revue est
  périodique.
- La justesse technique ne peut pas être validée par la seule campagne de
  mesure. Une relecture par un praticien est recherchée avant la v1.0.0.

## Alternatives écartées

- **Étendre `dpo-ct`** à la sécurité technique : rompt le contrat
  « exige / met en œuvre » et rend sa description ambiguë.
- **Un skill « numérique » réduit à la cybersécurité** : laisse sans
  propriétaire l'accessibilité, la dématérialisation et l'exécution des
  contrats, qui sont des obligations quotidiennes d'une DSI de collectivité.
