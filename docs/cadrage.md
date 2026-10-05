# Cadrage du skill `dsi-fpt` (v0.1.0)

> **Statut** : proposé le 2026-10-05, **à valider par l'auteur** avant toute
> rédaction (point d'étape de la Phase 1).
> **Usage** : document de conception, hors runtime. Les agents de rédaction de
> la Phase 3 reçoivent chacun le `SKILL.md` figé et **la fiche de leur
> branche** (§6). Toute référence juridique citée ici est un **candidat**, à
> vérifier en Phase 2 : rien de ce document n'est une source.

## 1. Utilisateur cible

**Persona** : la personne qui porte la fonction systèmes d'information d'une
collectivité territoriale ou d'un groupement : DSI, RSSI, responsable
informatique, chef de projet numérique, ou DGS d'une petite collectivité sans
DSI.

**Seuil proposé : aucun seuil d'effectif.** Une petite commune n'a pas de DSI,
mais elle a un SI, des obligations et des incidents. Le skill s'adapte au
**mode d'exercice** de la fonction, à lever en ouverture :

| Mode | Situation | Conséquence pour la réponse |
|---|---|---|
| Internalisé | DSI ou service informatique propre | Décision et exécution dans la collectivité |
| Mutualisé | Service commun d'EPCI, syndicat informatique, centre de gestion | Distinguer ce que décide la collectivité et ce que fait le service mutualisé ; convention de mutualisation à lire |
| Externalisé | Prestataire ou éditeur, sans compétence interne | Ce que la collectivité doit exiger, contrôler et conserver (réversibilité, accès, journaux) |

*Écart avec `drh-fpt`, qui vise plus de 350 agents* : en RH, la petite
collectivité relève d'un autre circuit (centre de gestion). En SI, la
responsabilité reste à la collectivité quel que soit le mode d'exercice.
**Question ouverte n° 1 à l'auteur.**

## 2. Périmètre

**Couvert** : gouvernance et stratégie du SI ; sécurité du SI ; crise cyber et
continuité ; infrastructures, réseaux et télécoms ; cloud et hébergement ;
applications métiers et interopérabilité, dont les interfaces avec les SI de
l'État ; dématérialisation et téléservices ; accessibilité numérique ; IA et
données (gouvernance, transparence des algorithmes publics) ; exécution des
contrats informatiques ; écrits de la fonction SI.

**Hors périmètre (signalé, jamais illustré)** :
- passation des marchés publics (procédure, critères, publicité) ;
- archivage électronique et ouverture des données publiques (reportés à une
  version ultérieure) ;
- fond du droit des données personnelles → `dpo-ct` ;
- inclusion numérique des publics (médiation, conseillers numériques) ;
- droit étranger.

## 3. Garde-fous (hard stops, avant tout contenu métier)

### 3.1 Garde-fou « incident cyber »

**Déclencheur** : un incident de sécurité est en cours ou vient d'être
découvert (rançongiciel, compromission, fuite, indisponibilité suspecte).

**Bloc imposé, avant toute aide technique** :
1. **Rien d'irréversible avant la préservation des preuves** : ne pas
   réinstaller, effacer, restaurer ou rallumer avant d'avoir isolé et
   conservé ce qui doit l'être.
2. **Rien de caché** : l'incident se signale dans les circuits prévus.
   Plainte, assurance, autorités et notifications se vérifient à la source :
   le skill nomme les questions, jamais un délai de mémoire.
3. **Rien de ce qui revient à l'exécutif** : la DSI ne décide pas seule du
   paiement d'une rançon, de la communication publique, ni de l'arrêt d'un
   service public.
4. **Aucune contre-mesure offensive**, aucun accès à un système tiers.
5. **Bascule `dpo-ct`** dès que des données personnelles peuvent être
   concernées.

### 3.2 Garde-fou « surveillance de personnes »

**Déclencheur** : demande d'accéder aux contenus ou aux traces d'une personne,
ou de déployer un dispositif qui surveille des personnes. Exemples : lire la
messagerie ou les fichiers d'un agent, extraire des journaux nominatifs,
géolocaliser des véhicules ou des agents, biométrie, vidéoprotection
algorithmique, reconnaissance faciale.

**Bloc imposé** : aucune commande, extraction ni paramétrage avant que la base
et les conditions soient établies par le skill compétent : `dpo-ct` (base
légale, information, AIPD) ; `drh-fpt` si un agent est visé (cadre statutaire,
suites disciplinaires) ; `dpm-fpt` pour la voie publique (vidéoprotection).
Le skill peut décrire **ce qu'il faudra exiger et tracer**, jamais **comment
le faire** tant que la base n'est pas établie.

## 4. Frontières opposables

| Sujet | `dsi-fpt` traite | Renvoi |
|---|---|---|
| Sécurité des traitements | Mesures techniques, architecture, PSSI, mise en œuvre | `dpo-ct` : exigences de conformité, niveau de risque pour les personnes |
| Violation de données | Confinement technique, preuves, éléments factuels pour la qualification | `dpo-ct` : qualification, notification, information des personnes |
| AIPD | Description technique et mesures | `dpo-ct` : conduite de l'AIPD |
| Charte informatique | Contenu technique, règles d'usage, moyens de contrôle | `drh-fpt` : adoption, opposabilité, consultation des instances, sanction |
| Télétravail | Équipement, accès distants, sécurité | `drh-fpt` : cadre statutaire et organisation du travail |
| SIRH | Hébergement, sécurité, interfaces | `drh-fpt` : paie, données sociales, pilotage RH |
| Vidéoprotection | Réseau, stockage, sécurité des équipements | `dpm-fpt` : autorisation, doctrine d'emploi, CSU, vidéoprotection algorithmique |
| Budget du numérique | Besoin, coût complet, plan pluriannuel exprimé en besoins | `dirfi-fpt` : inscription budgétaire, imputation, amortissement, financement |
| Achat informatique | Spécifications, exigences techniques, exécution du contrat | Passation : hors périmètre |
| Validité et vigueur d'un texte | Analyse métier | `recherche-juridique` |

Formule de bascule commune à la famille : un bloc `BASCULE` nommant le skill
par son nom (`dpo-ct`, pas « le DPO » ; `drh-fpt`, pas « les RH »), puis arrêt
du volet concerné.

## 5. Architecture des fichiers

```
SKILL.md
references/
  analyse-situation.md            routeur de couche 1
  _gabarit-branche.md             méta-gabarit (12 sections, à adapter de dirfi-fpt)
  socle-sources-verification.md   méthode de vérification
  references-verifiees.md         seul registre d'identifiants, daté
  cache-valeurs.md                valeurs volatiles, datées (exclu du runtime du plugin)
  gouvernance-strategie.md        ┐
  securite-si.md                  │
  crise-cyber-continuite.md       │
  infrastructures-reseaux.md      │
  cloud-hebergement.md            │
  applications-interoperabilite.md│ 12 branches
  dematerialisation-teleservices.md
  accessibilite-numerique.md      │
  ia-donnees.md                   │
  contrats-prestataires.md        │
  ecrits-numerique.md             │
  retex.md                        ┘
  templates/                      5 gabarits d'écrit (§8)
objets/
  _gabarit-objet.md
  6 objets (§7)
```

## 6. Fiches de cadrage des branches

Chaque fiche fixe ce que la branche couvre, ce qu'elle renvoie, et les
références qu'elle **peut** utiliser une fois vérifiées. Une branche ne cite
rien qui ne figure pas au socle vérifié.

### 6.1 `gouvernance-strategie`
- **Couvre** : schéma directeur du SI, gouvernance (comités, arbitrages),
  rôles DSI / RSSI / DPO / DGS, mutualisation (service commun, syndicat,
  convention), stratégie de numérique responsable, pilotage (indicateurs,
  portefeuille de projets).
- **Renvoie** : budget et financement → `dirfi-fpt` ; organisation des
  services et emplois → `drh-fpt` ; désignation et missions du DPO → `dpo-ct`.
- **Questions types** : faut-il un RSSI, et qui peut l'être ? Comment
  mutualiser avec l'EPCI ? Que doit contenir un schéma directeur ?
- **Références candidates** : CGCT (services communs, délégations) ; loi
  relative à la réduction de l'empreinte environnementale du numérique et
  obligations de stratégie numérique responsable (applicabilité par strate à
  vérifier).

### 6.2 `securite-si`
- **Couvre** : PSSI, analyse de risques, gestion des comptes et des droits,
  authentification, sauvegardes, mises à jour, sensibilisation, homologation
  de sécurité, sécurité des postes et des usages, journalisation.
- **Renvoie** : exigences de conformité RGPD → `dpo-ct` ; incident en cours →
  `crise-cyber-continuite` (et garde-fou §3.1) ; accès aux traces d'un agent →
  garde-fou §3.2.
- **Questions types** : par quoi commencer une PSSI ? Qui homologue, et
  quand ? Que faire des comptes d'un agent qui part ?
- **Références candidates** : RGS (ordonnance de 2005 sur les échanges
  électroniques, décret d'application) ; code pénal, atteintes aux systèmes de
  traitement automatisé de données ; transposition de la directive NIS2
  (entités visées : **applicabilité aux collectivités à vérifier par
  catégorie**) ; doctrine d'appui ANSSI (guide d'hygiène, EBIOS RM) — non
  normative.

### 6.3 `crise-cyber-continuite`
- **Couvre** : gestion de crise cyber, cellule de crise, décisions et
  traçabilité, communication interne, reprise, PCA et PRA, exercices.
- **Renvoie** : notification et information des personnes → `dpo-ct` ;
  communication publique et décisions politiques → exécutif (nommé, pas
  traité) ; plainte et procédure pénale : nommer, ne pas dérouler.
- **Garde-fou** : §3.1, systématique.
- **Questions types** : nous sommes chiffrés, que fait-on dans la première
  heure ? Faut-il payer ? Comment préparer un PRA réaliste ?
- **Références candidates** : code des assurances (conditions d'indemnisation
  du risque cyber, **à vérifier**) ; obligations de signalement selon le
  régime applicable (NIS2 transposée si l'entité est visée) ; dispositifs
  publics d'assistance (doctrine d'appui).

### 6.4 `infrastructures-reseaux`
- **Couvre** : réseaux, sites distants, écoles, téléphonie, interconnexions,
  postes et parc, salle serveur, alimentation, sobriété matérielle et fin de
  vie des équipements.
- **Renvoie** : choix d'hébergement externe → `cloud-hebergement` ;
  équipements de vidéoprotection, côté doctrine → `dpm-fpt`.
- **Questions types** : comment sécuriser le réseau des écoles ? Quelle
  architecture pour des sites distants ? Que faire des postes en fin de vie ?
- **Références candidates** : réglementation des déchets d'équipements
  électriques et électroniques et obligations de réemploi des achats publics
  (à vérifier).

### 6.5 `cloud-hebergement`
- **Couvre** : choix entre hébergement interne, mutualisé et cloud ;
  qualification des offres ; localisation et souveraineté ; réversibilité ;
  hébergement de données particulières.
- **Renvoie** : transferts hors Union européenne et sous-traitance au sens du
  RGPD → `dpo-ct` ; clauses et exécution du contrat → `contrats-prestataires`.
- **Point d'applicabilité critique** : la doctrine « cloud au centre » et
  les exigences de qualification visent d'abord l'État. Ne jamais les
  présenter comme obligatoires pour une collectivité sans la source qui
  l'établit.
- **Questions types** : peut-on mettre la messagerie dans un cloud
  américain ? Doit-on exiger SecNumCloud ? Comment sortir d'un hébergeur ?
- **Références candidates** : loi visant à sécuriser et réguler l'espace
  numérique (dispositions relatives au cloud, applicabilité à vérifier) ;
  référentiel SecNumCloud (doctrine) ; hébergement des données de santé (cas
  particuliers, à vérifier).

### 6.6 `applications-interoperabilite`
- **Couvre** : cartographie applicative, SI métiers, éditeurs, référentiels
  et données de référence, interopérabilité ; interfaces avec les SI de
  l'État : état civil, élections, transmission au contrôle de légalité,
  chaîne comptable et financière, facturation électronique.
- **Renvoie** : fond comptable → `dirfi-fpt` ; fond état civil et élections :
  hors périmètre, nommer le service compétent ; données personnelles →
  `dpo-ct`.
- **Questions types** : comment changer d'éditeur sans rupture ? Quels
  échanges obligatoires avec l'État ? Comment fiabiliser un référentiel ?
- **Références candidates** : référentiel général d'interopérabilité ; CRPA,
  échanges de données entre administrations ; obligations de facturation
  électronique et de transmission dématérialisée (calendriers **à vérifier**).

### 6.7 `dematerialisation-teleservices`
- **Couvre** : téléservices, saisine par voie électronique, identification
  et authentification des usagers, signature électronique, parapheur,
  circuits dématérialisés.
- **Renvoie** : mentions d'information et données → `dpo-ct` ;
  accessibilité → `accessibilite-numerique` ; archivage : hors périmètre.
- **Questions types** : un usager peut-il nous saisir par mail ? Quelle
  signature électronique pour un arrêté ? Faut-il homologuer un téléservice ?
- **Références candidates** : CRPA (saisine par voie électronique,
  téléservices) ; RGS ; règlement européen sur l'identification électronique
  et les services de confiance.

### 6.8 `accessibilite-numerique`
- **Couvre** : obligations d'accessibilité des sites, applications et
  documents ; référentiel ; déclaration d'accessibilité ; schéma pluriannuel ;
  achats accessibles ; sanctions.
- **Renvoie** : contenus éditoriaux et communication : nommer, ne pas traiter.
- **Questions types** : sommes-nous obligés de publier une déclaration ?
  Que risque-t-on ? Comment l'exiger d'un prestataire ?
- **Références candidates** : loi de 2005 pour l'égalité des droits et des
  chances (article sur l'accessibilité des services de communication au
  public en ligne) ; décret d'application ; RGAA (référentiel) ; montants des
  sanctions **jamais de mémoire**.

### 6.9 `ia-donnees`
- **Couvre** : gouvernance des données ; usage de l'IA, y compris générative ;
  obligations du règlement européen sur l'IA pour un déployeur public ;
  transparence des algorithmes publics et des décisions individuelles
  fondées sur un traitement algorithmique ; charte d'usage de l'IA.
- **Renvoie** : AIPD et base légale → `dpo-ct` ; vidéoprotection
  algorithmique → garde-fou §3.2 et `dpm-fpt` ; ouverture des données : hors
  périmètre.
- **Questions types** : les agents peuvent-ils utiliser un assistant d'IA
  générative ? Notre outil de tri des demandes est-il un système à haut
  risque ? Que doit-on publier sur nos algorithmes ?
- **Références candidates** : règlement européen sur l'intelligence
  artificielle (catégories, calendrier d'application **à vérifier**) ; CRPA
  (mention et information sur les traitements algorithmiques) ; loi pour une
  République numérique.

### 6.10 `contrats-prestataires`
- **Couvre** : exécution des contrats informatiques : niveaux de service,
  pénalités, réversibilité, propriété et restitution des données, licences,
  maintenance, infogérance, gestion d'un éditeur défaillant, fin de contrat.
- **Renvoie** : passation, choix de procédure, critères : **hors
  périmètre** ; clauses RGPD → `dpo-ct` ; aspects financiers → `dirfi-fpt`.
- **Questions types** : l'éditeur refuse de nous rendre nos données. Comment
  écrire une clause de réversibilité ? Le prestataire ne tient pas ses
  engagements.
- **Références candidates** : cahier des clauses administratives générales
  applicable aux marchés de techniques de l'information et de la
  communication ; code de la commande publique (exécution et modification des
  contrats uniquement).

### 6.11 `ecrits-numerique`
- **Couvre** : note de décision, rapport d'incident, cahier des charges
  technique, charte d'usage, note d'homologation, communication interne de la
  DSI.
- **Renvoie** : délibérations et budgets → `dirfi-fpt` ; actes RH →
  `drh-fpt`.
- **Pointeurs** : gabarits de `references/templates/` (§8).

### 6.12 `retex`
- **Couvre** : retours d'expérience, après incident ou après projet ; méthode,
  traçabilité, plan d'action ; alimentation du `JOURNAL.md` sans donnée
  identifiante.

## 7. Objets métier

| Objet | Situation type | Branches mobilisées |
|---|---|---|
| `projet-si` | Lancer et conduire un projet applicatif | gouvernance, applications, contrats, sécurité |
| `incident-securite` | Gérer un incident de sécurité du début à la clôture | crise, sécurité, retex (+ `dpo-ct`) |
| `teleservice` | Ouvrir un téléservice aux usagers | dématérialisation, accessibilité, sécurité (+ `dpo-ct`) |
| `solution-saas` | Choisir, contractualiser et sortir d'une solution en ligne | cloud, contrats, sécurité |
| `site-reseau` | Équiper ou sécuriser un site (mairie annexe, école) | infrastructures, sécurité |
| `compte-poste-agent` | Arrivée, mobilité et départ d'un agent : comptes, accès, poste | sécurité, infrastructures (+ `drh-fpt`, garde-fou §3.2) |

## 8. Gabarits d'écrit

`fiche-projet-si` · `rapport-incident` · `cahier-des-charges-technique` ·
`charte-usage-si` (contenu technique ; adoption → `drh-fpt`) ·
`note-homologation` (précise quand l'homologation s'impose, selon le socle).

## 9. Plan des 28 cas de test

| # | Cible | Intention du cas | Critique |
|---|---|---|---|
| 1 | gouvernance-strategie | Désigner un RSSI dans une commune moyenne | |
| 2 | securite-si | Bâtir une première PSSI | |
| 3 | crise-cyber-continuite | Préparer un PRA réaliste | |
| 4 | infrastructures-reseaux | Sécuriser le réseau des écoles | |
| 5 | cloud-hebergement | Messagerie chez un fournisseur hors UE | |
| 6 | applications-interoperabilite | Changer d'éditeur de logiciel métier | |
| 7 | dematerialisation-teleservices | Saisine d'un usager par voie électronique | |
| 8 | accessibilite-numerique | Obligations de déclaration d'accessibilité | |
| 9 | ia-donnees | Usage d'une IA générative par les agents | |
| 10 | contrats-prestataires | Éditeur qui refuse de restituer les données | |
| 11 | ecrits-numerique | Note au DGS pour arbitrer un projet | |
| 12 | retex | RETEX après une panne majeure | |
| 13 | objets/projet-si | Conduite d'un projet applicatif | |
| 14 | objets/incident-securite | Clôture d'un incident sans données touchées | |
| 15 | objets/teleservice | Ouverture d'un téléservice | |
| 16 | objets/solution-saas | Sortie d'une solution en ligne | |
| 17 | objets/site-reseau | Équiper une mairie annexe | |
| 18 | objets/compte-poste-agent | Départ d'un agent | |
| 19 | templates/cahier-des-charges-technique | Rédiger le cahier des charges technique | |
| 20 | templates/charte-usage-si | Rédiger une charte d'usage | |
| 21 | garde-fou incident cyber | Rançongiciel en cours, restauration et rançon | ✅ |
| 22 | garde-fou surveillance | Lire la messagerie d'un agent soupçonné | ✅ |
| 23 | frontière `dpo-ct` | Fuite de données : qui notifie, quand | ✅ |
| 24 | frontière `drh-fpt` | Sanctionner un agent pour usage abusif | ✅ |
| 25 | frontière `dpm-fpt` | Reconnaissance faciale demandée sur les caméras | ✅ |
| 26 | applicabilité | Obligation de l'État présentée comme applicable à une commune | ✅ |
| 27 | hors périmètre | Choisir la procédure de passation d'un logiciel | ✅ |
| 28 | sourcing | Question qui appelle un seuil ou un délai précis | ✅ |

Règle : un attendu juridique ne peut citer qu'une référence du socle vérifié.

## 10. Socle : format retenu

`references/references-verifiees.md` reprend le format de `dirfi-fpt`, avec
une colonne ajoutée :

| Référence | Objet | En vigueur depuis | Identifiant | Vérifié le | **Applicable aux collectivités** |
|---|---|---|---|---|---|

Valeurs de la dernière colonne : `oui` · `non` · `sous conditions (…)`, avec la
source de cette appréciation. La doctrine (ANSSI, référentiels de l'État) est
tenue dans une section séparée et marquée **non normative**.

## 11. Questions ouvertes pour le point d'étape

1. **Seuil** : valider l'absence de seuil d'effectif et le traitement par
   mode d'exercice (§1).
2. **Branches** : valider les 12 fiches (§6), ou en retirer pour revenir à
   un périmètre plus étroit.
3. **Relecture praticien** : existe-t-il un DSI ou un RSSI de collectivité
   partenaire qui pourrait relire les branches sécurité, crise et cloud avant
   la v1.0.0 ?
4. **Garde-fous** : valider les formulations du §3, notamment le point 3 du
   garde-fou incident (décisions réservées à l'exécutif).
