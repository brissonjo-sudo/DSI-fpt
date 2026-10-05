# dsi-fpt — Direction des systèmes d'information en collectivité territoriale

> **Statut : en construction (v0.1.0, non mesuré).** Le skill n'est pas encore
> utilisable. Le cadrage est dans `docs/cadrage.md`, la décision
> d'architecture dans `docs/adr/0001-adoption-patron-dirfi-fpt.md`.

Système expert d'aide à la décision pour la fonction **systèmes
d'information** d'une collectivité territoriale française : gouvernance du
SI, sécurité et crise cyber, infrastructures, cloud et hébergement,
applications métiers et interopérabilité, dématérialisation, accessibilité
numérique, IA et données, exécution des contrats informatiques.

Il est le cinquième skill métier de la famille `collectivite-territoriale`,
aux côtés de `dpm-fpt` (police municipale), `drh-fpt` (ressources humaines),
`dpo-ct` (protection des données) et `dirfi-fpt` (finances), avec
`recherche-juridique` comme validateur de fond. Il est le miroir technique du
contrat posé par `dpo-ct` : **le DPO exige, la DSI met en œuvre**.

## Ce que le skill ne fait pas

- Il ne qualifie pas le droit des données personnelles : c'est `dpo-ct`.
- Il ne traite pas la passation des marchés publics.
- Il ne se substitue ni à un RSSI, ni à un prestataire de réponse à incident,
  ni aux autorités compétentes en cas d'attaque.

## Feuille de route

1. Cadrage et décisions d'architecture.
2. Socle de sources vérifiées, avec applicabilité aux collectivités.
3. Rédaction : `SKILL.md`, puis branches, objets et gabarits.
4. Outillage de validation et de mesure.
5. Campagne de mesure de 28 cas ; v1.0.0 au premier passage du seuil.
6. Intégration au plugin `collectivite-territoriale`.

## Licence

CC-BY-SA-4.0, comme le plugin `collectivite-territoriale` et les skills qu'il
embarque. Voir `LICENSE`.
