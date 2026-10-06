# dsi-fpt — Direction des systèmes d'information en collectivité territoriale

> **Statut : version de travail v0.2.0, non mesurée.** Rédaction et outillage
> achevés ; publication suspendue à la mesure et à la relecture DSI/RSSI.
> Le cadrage est dans `docs/cadrage.md`, la décision
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

État détaillé et limites d'exécution : [docs/etat-avancement.md](docs/etat-avancement.md).
Relecture praticien : [docs/relecture-praticien.md](docs/relecture-praticien.md).

## Vérifier et préparer la mesure

```
python scripts/validate_repo.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/package_skill.py
python scripts/mesure_locale.py export --run-dir tests/runs/codex-v0.2.0-r1 --output dist/campagne-dsi-v0.2.0
```

L'archive du skill reste dans `dist/` ; elle exclut le cache des valeurs,
les tests et les documents de conception. Le kit de campagne contient en
plus les cas et le lanceur, avec séparation des entrées et des contextes.
Le dossier de run est déjà préparé et l'export exige une destination neuve.
La préparation et l'export n'appellent aucun modèle ; un dossier préparé
n'a aucun score. Le lanceur local appelle ensuite la CLI choisie sur votre
poste et conserve les réponses et jugements réellement produits.

Commandes Claude/Codex, contrôle sans appel et reprise :
[docs/campagne-locale.md](docs/campagne-locale.md).

## Licence

CC-BY-SA-4.0, comme le plugin `collectivite-territoriale` et les skills qu'il
embarque. Voir `LICENSE`.
