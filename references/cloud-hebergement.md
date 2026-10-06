# Branche — Cloud et hébergement

> Cœur de la branche : le **test d'applicabilité**. Une grande partie des
> textes et de la doctrine sur le cloud vise l'État, pas la collectivité.
> Aucune valeur (date, seuil, version de référentiel) n'est énoncée ici :
> voir `references/references-verifiees.md` et `references/cache-valeurs.md`.

## 1. Périmètre / Exclusions

- **Périmètre** : le choix entre hébergement interne, hébergement mutualisé
  et informatique en nuage ; la qualification des offres ; la localisation et
  la souveraineté ; la réversibilité ; l'hébergement de données
  particulières. La branche formule des **exigences** et éclaire une
  **décision** qui revient à l'exécutif.
- **Exclusions** :
  - transferts de données personnelles hors de l'Union, sous-traitance au
    sens du RGPD, base légale → **`BASCULE dpo-ct`** (`SKILL.md` §5.5) ;
  - rédaction des clauses, niveaux de service, pénalités, exécution et fin du
    contrat → `references/contrats-prestataires.md` ;
  - salle serveur, réseau, interconnexions, matériel →
    `references/infrastructures-reseaux.md` ;
  - analyse de risques, homologation, attestation formelle →
    `references/securite-si.md` ;
  - PCA, PRA, reprise → `references/crise-cyber-continuite.md` ;
  - inscription budgétaire, imputation, financement → **`BASCULE dirfi-fpt`** ;
  - passation du marché (procédure, critères, publicité) → **hors
    périmètre** : le signaler, nommer le service de la commande publique,
    s'arrêter ;
  - archivage électronique → **hors périmètre de cette version** : le
    signaler.
- **Situation récurrente** : choisir, contractualiser ou quitter une solution
  en ligne → `objets/solution-saas.md`, qui agrège cette branche et
  `references/contrats-prestataires.md`.

## 2. Questions couvertes

- « Peut-on mettre la messagerie chez un fournisseur dont le siège est hors
  de l'Union ? »
- « Doit-on exiger une offre qualifiée SecNumCloud ? »
- « La loi SREN et la doctrine "cloud au centre" nous obligent-elles ? »
- « Faut-il garder une salle serveur, rejoindre l'hébergement du syndicat
  informatique, ou passer en SaaS ? »
- « Comment sortir d'un hébergeur sans perdre nos données ? »
- « L'hébergeur peut-il nous facturer le changement de fournisseur ? »
- « Où sont réellement nos données, sauvegardes comprises ? »
- « Ce logiciel métier en SaaS traite des données sociales ou de santé :
  quelles précautions ? »

## 3. Arbre de traitement

`question d'hébergement → garde-fous (incident chez l'hébergeur ? accès aux
traces de personnes ?) → mode d'exercice (§4) → nature et sensibilité des
données (§5.2) → texte invoqué : vise-t-il la collectivité ? (§5.1) →
exigences de localisation, qualification, réversibilité (§5.3 à §5.5) →
renvois de frontière (dpo-ct, contrats, dirfi-fpt) → décision de l'exécutif
(§6.1) → vérification des valeurs (§9) → livrable (§10)`

**Réflexes impératifs** :

1. **Garde-fous d'abord.** Un hébergeur compromis, une fuite chez un
   prestataire, une indisponibilité inexpliquée d'un service en ligne : STOP
   incident de `SKILL.md` §5.2, en premier. Une demande d'exploiter les
   journaux du fournisseur pour suivre l'activité d'agents : STOP
   surveillance de `SKILL.md` §5.3.
2. **Applicabilité avant « doit ».** Toute phrase « la collectivité doit
   héberger… » exige un texte qui vise la collectivité (§5.1). À défaut,
   écrire « bonne pratique » ou « exigence que la collectivité peut fixer ».
3. **Qualifier les données avant l'offre.** Le niveau d'exigence se déduit de
   la sensibilité des données et de la criticité du service, pas du discours
   commercial.

## 4. Variables à lever

- **Mode d'exercice** (`SKILL.md` §2.4) — à demander s'il n'est pas donné :
  - **Internalisé** : la collectivité héberge dans ses locaux. Elle décide et
    exécute. Évaluer ce qu'elle sait réellement tenir : sécurité physique,
    alimentation, sauvegardes hors site, compétences d'astreinte →
    `references/infrastructures-reseaux.md`.
  - **Mutualisé** : hébergement par un service commun d'EPCI, un syndicat
    informatique ou un autre organisme public. Lire la **convention** :
    localisation, sécurité, réversibilité, sort des données en cas de
    retrait. La collectivité reste responsable de son SI ; la convention ne
    transfère pas cette responsabilité.
  - **Externalisé** : SaaS, hébergement ou infogérance par un prestataire.
    Lister ce que la collectivité **exige, contrôle et conserve** : accès à
    ses données, journaux, droit d'audit, plan de réversibilité.
- **Nature et sensibilité des données** : données personnelles courantes,
  données sensibles, données de personnes vulnérables, données sociales ou de
  santé, données couvertes par un secret protégé par la loi, documents
  destinés à l'archivage.
- **Criticité du service** : service public interrompu si l'hébergement
  tombe ? Durée d'interruption tolérable ? Dépendance d'autres services ?
- **Prestataire et contrat en place** : nature de l'offre (SaaS, plateforme,
  infrastructure), siège et chaîne de sous-traitance, date d'échéance,
  clauses de réversibilité existantes.
- **Usagers concernés** : un téléservice ouvert au public emporte des
  exigences propres (§5.6).
- **Date de référence** : la qualification d'une offre, le calendrier du
  règlement européen sur les données et la version du référentiel
  SecNumCloud s'apprécient **à la date de la décision**.

## 5. Règles métier

### 5.1 Applicabilité : ce qui vise la collectivité, ce qui ne la vise pas

| Texte ou référentiel | Vise la collectivité ? | Usage dans la réponse |
|---|---|---|
| Loi visant à sécuriser et réguler l'espace numérique (dite SREN), article relatif à l'informatique en nuage et aux données sensibles | **Non**. Il vise les administrations de l'État, ses opérateurs et certains groupements d'intérêt public (registre §10) | Référence de **bonne pratique** seulement |
| Doctrine « cloud au centre » (circulaire du Premier ministre) | **Non**. Destinataires : membres du gouvernement ; objet : l'informatique en nuage de l'État (registre §15.2) | Référence de **bonne pratique** seulement |
| Référentiel SecNumCloud (ANSSI) | **Non** pour l'acheteur. Il s'impose aux **prestataires qui demandent la qualification** (registre §15.2) | La collectivité **peut l'exiger** par contrat |
| Catalogue des offres qualifiées (ANSSI) | Outil, pas une norme | À consulter **à la date de la décision** |
| Règlement européen sur les données (dit Data Act), changement de fournisseur de services de traitement de données | **Oui, comme bénéficiaire** : la collectivité cliente entre dans la définition du « client » (registre §10) | Argument de réversibilité et de négociation |
| Référentiel général de sécurité (ordonnance sur les échanges électroniques et décret d'application) | **Oui** : les collectivités sont des « autorités administratives » (registre §4) | Analyse de risques, homologation et attestation formelle du système hébergé → `references/securite-si.md` |

Règles à appliquer :

- **Ne jamais écrire** que la loi SREN ou la doctrine « cloud au centre »
  oblige une collectivité. Écrire : « ce texte vise l'État ; la collectivité
  peut s'en inspirer comme bonne pratique ».
- **Piège de traduction** : la traduction anglaise de la règle R5 de la
  doctrine emploie « local authorities » là où le texte français dit
  « l'administration ». Se référer au **texte français**. Ne jamais tirer de
  la traduction une obligation de collectivité (registre §15.2).
- **Groupement d'intérêt public** : si la collectivité est membre d'un
  groupement qui comprend l'État ou ses opérateurs, l'article SREN peut viser
  **le groupement**. Le vérifier sur le texte ; ne pas en déduire une
  obligation de la collectivité elle-même.
- **SecNumCloud n'est pas une obligation de l'acheteur.** La collectivité
  décide de l'exiger ou non, au regard de la sensibilité des données.
  L'ANSSI le préconise pour les données sensibles (registre §15.2).
- **Décret RGS et prestataires qualifiés.** Le décret RGS traite du recours à
  des produits et prestataires qualifiés ou conformes (registre §4). Sa portée
  exacte pour un hébergement en nuage n'est pas établie au registre. Ne pas
  en déduire une obligation de qualification SecNumCloud : **à vérifier**.
- **Applicabilité du règlement européen sur les données** : la collectivité
  cliente bénéficie des règles de changement de fournisseur. Les obligations
  détaillées du fournisseur (préavis, assistance, périmètre des données
  exportables) et leur application aux contrats en cours ne sont pas au
  registre : **à vérifier** en version consolidée.

### 5.2 Qualifier les données avant de choisir

Classer les données du service avant toute comparaison d'offres. Méthode
proposée, **non normative** (bonne pratique), en trois niveaux internes :

1. **Courantes** : informations publiques ou peu sensibles.
2. **Sensibles** : données personnelles d'usagers ou d'agents, données
   financières, documents préparatoires de décisions, données dont la
   divulgation atteindrait la collectivité.
3. **Particulières** : données sociales, de santé, de personnes vulnérables,
   données couvertes par un secret protégé par la loi, données de sécurité du
   SI lui-même.

- Le niveau commande l'exigence (§5.3, §5.4). Il ne se négocie pas avec le
  prestataire.
- La classification relève de la collectivité. Les directions métiers la
  portent ; la DSI l'instruit ; le DPO **exige** pour les données personnelles.
- **Données particulières** : des régimes d'hébergement spécifiques peuvent
  exister (données de santé notamment ; archives publiques). Ils ne sont pas
  établis au registre. Ne rien affirmer : **à vérifier**, avec `dpo-ct` pour
  les données personnelles et `recherche-juridique` pour le régime. Archivage
  électronique : hors périmètre de cette version.

### 5.3 Localisation et exposition à des droits étrangers

- **Localisation : exigence, pas constat.** Exiger par écrit la localisation
  des données, **des sauvegardes**, des copies de secours et des journaux.
  Exiger aussi la localisation des **accès d'administration** et du
  **support** : une donnée hébergée dans l'Union peut être consultée depuis
  l'étranger.
- **Chaîne de sous-traitance** : exiger la liste des sous-traitants
  techniques et l'information préalable de tout changement. La qualification
  RGPD de cette chaîne relève de `dpo-ct`.
- **Exposition à des lois étrangères à portée extraterritoriale** : c'est un
  **risque à évaluer** dans l'analyse de risques, pas une interdiction
  générale. Le siège du fournisseur et de sa maison mère est une variable.
- **Données personnelles et transfert hors de l'Union** : la DSI décrit les
  flux, les lieux et les accès ; elle ne qualifie pas le transfert.
  **`BASCULE dpo-ct`**, objet à reprendre : « licéité du transfert et
  encadrement de la sous-traitance pour [service], au vu des flux décrits ».
- « Peut-on mettre la messagerie chez un fournisseur hors Union ? » : aucune
  interdiction propre à la collectivité ne figure au registre. La réponse
  dépend de la sensibilité des contenus (§5.2), du transfert (`dpo-ct`) et de
  l'analyse de risques (`references/securite-si.md`). Ne pas répondre par
  oui ou non sans ces trois éléments.

### 5.4 Qualification des offres

- **Ce que dit la qualification** : un prestataire qualifié SecNumCloud a été
  évalué sur un référentiel d'exigences de l'ANSSI. Selon la page de l'ANSSI
  lue lors de la constitution du socle, la version courante intègre des
  critères de protection vis-à-vis du droit extra-européen
  (`docs/socle/lot-4-doctrine.md`). Doctrine, non normative.
- **Ce qu'elle ne dit pas** : qu'une offre non qualifiée est interdite ;
  qu'une offre qualifiée dispense la collectivité de son analyse de risques
  et de son homologation.
- **Vérifier le périmètre** : la qualification porte sur une **offre**
  précise, pour une période de validité. Un même fournisseur peut proposer
  des offres qualifiées et d'autres qui ne le sont pas.
- **Vérifier à la date de la décision** dans le catalogue de l'ANSSI, mis à
  jour régulièrement. Ne jamais se fier à une plaquette commerciale ni à une
  liste ancienne.
- **Exiger le maintien** de la qualification pendant le contrat, et
  l'information de la collectivité en cas de perte ou de suspension (clause →
  `references/contrats-prestataires.md`).
- **Ne recommander aucun fournisseur ni aucune marque.** Donner la méthode de
  vérification, jamais une liste de prestataires.
- Arbitrage proportionné, **bonne pratique** à soumettre à l'exécutif :
  - données courantes : qualification utile, rarement déterminante ;
  - données sensibles : exigence de qualification à envisager sérieusement ;
  - données particulières : exigence forte, sauf analyse de risques
    contraire, motivée et écrite.

### 5.5 Réversibilité

La réversibilité est une **exigence**, fixée avant la signature. Elle se
prouve par un essai, pas par une clause.

- **Contenu à exiger** :
  - export **complet** : données, pièces jointes, métadonnées, paramétrages,
    historiques, journaux ;
  - **formats** documentés et réutilisables, avec leur description ;
  - **assistance** du sortant et délai de mise à disposition ;
  - **double fonctionnement** possible pendant la bascule ;
  - **suppression** des données chez le sortant, attestée, après
    récupération complète ;
  - **plan de réversibilité** écrit, mis à jour, et **testé** pendant le
    contrat.
- **Frais de changement** : le règlement européen sur les données organise
  la **suppression progressive** des frais de changement de fournisseur,
  dont la collectivité cliente bénéficie (registre §10). Les étapes de ce
  calendrier sont datées : **à vérifier** à la source (`cache-valeurs.md`,
  `references-verifiees.md`) à la date de la sortie envisagée.
- **Mode mutualisé** : la convention doit prévoir le sort des données en cas
  de retrait de la collectivité. À défaut, le signaler comme risque majeur.
  L'application du règlement européen sur les données à un hébergeur public
  mutualisé n'est pas établie : **à vérifier**.
- **Accès aux documents** : la collectivité doit rester en mesure de
  retrouver et de communiquer ses documents administratifs, y compris ceux
  hébergés chez un tiers (codes sources compris, registre §2). Exiger un
  accès qui le permette à tout moment.
- **Éditeur qui refuse de restituer** → `references/contrats-prestataires.md`.

### 5.6 Sécurité de l'hébergement

- **Changement d'hébergement = changement du système.** Le décret RGS prévoit
  une analyse de risques et son réexamen, et une **attestation formelle** de
  sécurité par l'autorité administrative elle-même (registre §4 ;
  applicabilité aux collectivités par l'ordonnance, l'analyse de risques
  étant marquée « inférence » au registre). Relancer la
  démarche d'homologation → `references/securite-si.md` et
  `references/templates/note-homologation.md`.
- **Téléservice hébergé** : l'attestation de sécurité est rendue accessible
  aux usagers (registre §4) → `references/dematerialisation-teleservices.md`.
- **Exigences de sécurité** à poser, sans détail d'architecture : contrôle
  des accès d'administration, authentification renforcée, chiffrement des
  données et maîtrise des clés, séparation des environnements des clients,
  journalisation accessible à la collectivité, notification des incidents
  par le prestataire, droit d'audit.
- **Ne jamais écrire** dans un livrable diffusable une adresse, un nom de
  serveur, un compte ou une configuration exploitable.
- **Continuité** : la défaillance de l'hébergeur est un scénario du PRA →
  `references/crise-cyber-continuite.md`.

### 5.7 Qui décide, qui exécute, qui exige

| Rôle | Acteur | Contenu |
|---|---|---|
| **Décide** | Exécutif (assemblée si la convention ou l'engagement le requiert : à vérifier) | Choix du mode d'hébergement, acceptation du risque résiduel, homologation |
| **Instruit et exécute** | DSI, service mutualisé ou prestataire | Qualification des données, analyse de risques, exigences, migration, réversibilité |
| **Exige** | DPO | Conformité RGPD, transferts, sous-traitance (`dpo-ct`) |
| **Finance** | Direction des finances | Coût complet traduit en budget (`dirfi-fpt`) |

La DSI exprime le **coût complet en besoins** (abonnements, migration,
réversibilité, double fonctionnement, compétences). L'imputation et le
financement relèvent de `dirfi-fpt`.

## 6. Procédures

### 6.1 Décider d'un mode d'hébergement

| Étape | Acteur | Contenu | Point de contrôle |
|---|---|---|---|
| 1. Cadrage | DSI, direction métier | Besoin, criticité, usagers | Mode d'exercice levé |
| 2. Qualification des données | Direction métier, DSI ; DPO consulté | Niveau §5.2 | Données particulières identifiées |
| 3. Analyse de risques | DSI, RSSI | Scénarios : indisponibilité, fuite, droit étranger, défaillance, verrouillage | `references/securite-si.md` |
| 4. Exigences | DSI | Localisation, qualification, réversibilité, sécurité, journaux, audit | Cahier des charges technique |
| 5. Frontières | DSI | `BASCULE dpo-ct` (transferts, sous-traitance) ; `BASCULE dirfi-fpt` (financement) ; passation : hors périmètre | Blocs affichés avant le contenu concerné |
| 6. Note de décision | DSI → DGS → exécutif | Options, risques, coût complet en besoins, recommandation | Décision par l'autorité compétente |
| 7. Homologation | Autorité administrative | Attestation formelle du système hébergé | Avant mise en service |
| 8. Revue | DSI | Qualification maintenue, réversibilité testée, contrat suivi | Calendrier de revue fixé |

Hypothèses à annoncer : sensibilité supposée des données, mode d'exercice
supposé. Demander les données manquantes plutôt que de les inventer.

### 6.2 Sortir d'un hébergeur

1. **Relire** le contrat ou la convention : clauses de réversibilité, préavis,
   échéance → `references/contrats-prestataires.md`.
2. **Inventorier** ce qui doit sortir : données, documents, paramétrages,
   journaux, comptes, interfaces → `references/applications-interoperabilite.md`.
3. **Demander** par écrit le plan de réversibilité et un export d'essai.
4. **Vérifier** l'export d'essai : complétude, lisibilité, formats.
5. **Vérifier** à la source les règles du règlement européen sur les données
   applicables à la date de la sortie, dont les frais.
6. **Organiser** le double fonctionnement et la bascule ; prévoir le retour
   arrière.
7. **Obtenir** l'attestation de suppression chez le sortant après
   récupération complète et contrôlée.
8. **Mettre à jour** l'homologation du nouveau système.

Délais de préavis et d'assistance : **à vérifier** dans le contrat et, le cas
échéant, dans le règlement européen sur les données.

## 7. Déclencheurs de vérification

Appliquer le socle-sources (`SKILL.md` §5.4,
`references/socle-sources-verification.md`) et la matrice `SKILL.md` §2.2 dès
que la réponse porte sur :

- l'**applicabilité** d'un texte sur le cloud à une collectivité (SREN,
  doctrine de l'État, texte européen) ;
- la **qualification** d'une offre : catalogue de l'ANSSI à la date de la
  décision ;
- la **version** du référentiel SecNumCloud ;
- les **étapes et dates** du règlement européen sur les données (frais de
  changement, obligations du fournisseur) ;
- un **régime d'hébergement spécifique** (données de santé, archives
  publiques, autre secret) ;
- la **compétence** pour décider : exécutif ou assemblée ;
- toute **obligation** que l'on s'apprête à écrire avec « doit ».

Vigueur, conflit de normes, jurisprudence → `recherche-juridique`.

## 8. Pièges et confusions fréquentes

1. **Présenter la loi SREN comme une obligation de la collectivité.** Elle
   vise l'État, ses opérateurs et certains groupements (registre §10).
2. **Présenter la doctrine « cloud au centre » comme du droit applicable.**
   C'est une circulaire adressée aux membres du gouvernement, pour l'État.
3. **Citer la traduction anglaise de la règle R5** (« local authorities »)
   pour en faire une obligation des collectivités. Le texte français dit
   « l'administration ».
4. **Dire « SecNumCloud est obligatoire ».** Le référentiel s'impose aux
   prestataires qui demandent la qualification ; l'acheteur peut l'exiger.
5. **Confondre fournisseur qualifié et offre qualifiée.** La qualification
   porte sur une offre, pour une période.
6. **Se fier à une liste d'offres qualifiées ancienne.** Le catalogue change :
   le consulter à la date de la décision.
7. **Croire qu'un hébergement dans l'Union règle tout.** Les accès
   d'administration, le support et la maison mère comptent aussi.
8. **Traiter le transfert hors Union dans `dsi-fpt`.** C'est `dpo-ct`.
9. **Croire que le mode mutualisé transfère la responsabilité.** La
   collectivité reste responsable de son SI.
10. **Réversibilité « contractuelle » jamais testée.** Exiger un essai.
11. **Oublier l'homologation** lors d'une migration : le système change.
12. **Nommer ou recommander un fournisseur.** Interdit : donner la méthode.
13. **Glisser vers la passation** (critère de sélection, pondération,
    procédure). Formuler l'exigence technique, puis s'arrêter : hors
    périmètre.
14. **Donner une date de mémoire** pour les frais de changement ou une
    version de référentiel. Aucune exception de notoriété.

## 9. Données et valeurs à vérifier

Aucune de ces valeurs n'est chiffrée ici. Chacune se vérifie à la source, en
session, à la date de référence : voir `cache-valeurs.md` (quoi et où) et
`references-verifiees.md` (identifiants et applicabilité).

- **Loi SREN, article sur l'informatique en nuage** : champ exact des
  entités visées, décret d'application, délais et dérogations (registre §10 ;
  décret d'application non vérifié).
- **Doctrine « cloud au centre »** : référence et date de la circulaire en
  vigueur (registre §15.2).
- **Référentiel SecNumCloud** : version en vigueur (registre §15.2).
- **Catalogue des offres qualifiées** : édition consultée, périmètre et
  dates de validité de la qualification de l'offre visée.
- **Règlement européen sur les données** : étapes de la suppression des frais
  de changement, obligations du fournisseur, application aux contrats en
  cours (registre §10 ; « à confirmer en version consolidée »).
- **Décret RGS** : portée de l'obligation de recourir à des produits et
  prestataires qualifiés ou conformes (registre §4).
- **Régimes d'hébergement spécifiques** (santé, archives publiques, autres
  secrets) : non établis au registre.
- **Compétence** de l'assemblée pour une convention de mutualisation : selon
  la forme du montage (registre §9 pour les services communs ; autres formes
  à vérifier).

## 10. Écrits et livrables

- **Note de décision d'hébergement** (DSI → DGS → exécutif) : besoin,
  niveau des données, options comparées, risques, exigences, coût complet en
  besoins, recommandation, renvois `dpo-ct` et `dirfi-fpt`. Piloté par
  `references/ecrits-numerique.md` ; base : `references/templates/fiche-projet-si.md`.
- **Grille de qualification des données** du service (§5.2), datée et
  validée par la direction métier.
- **Cahier des charges technique** : localisation, qualification exigée ou
  non, réversibilité, sécurité, journaux, audit, sous-traitants →
  `references/templates/cahier-des-charges-technique.md`. Exigences
  techniques seulement ; la passation reste hors périmètre.
- **Plan de réversibilité** : contenu §5.5, calendrier d'essai, responsables.
- **Note d'homologation** mise à jour → `references/templates/note-homologation.md`.
- Tout écrit incomplet : brouillon marqué `[INCOMPLET]` listant les champs
  manquants. Ne jamais inventer un prestataire, une localisation ni un niveau
  de service.
- Aucun écrit ne contient de secret ni de détail d'architecture exploitable.

## 11. Double échelle [risque / confiance]

| Sous-cas | Risque | Confiance |
|---|---|---|
| Applicabilité de la loi SREN ou de la doctrine de l'État à une collectivité | Élevé (erreur de droit dans une note) | Stable : ne vise pas la collectivité (registre §10, §15.2) |
| Exiger ou non SecNumCloud | Moyen à élevé selon les données | Stable sur le principe ; à vérifier sur la version et le catalogue |
| Messagerie ou outils collaboratifs hors Union | Élevé | À vérifier : dépend de `dpo-ct` et de l'analyse de risques |
| Données sociales, de santé ou de personnes vulnérables | Élevé à critique | Abstention sur le régime spécifique tant qu'il n'est pas vérifié |
| Réversibilité et frais de changement | Moyen à élevé | Stable sur le principe (registre §10) ; à vérifier sur les dates |
| Choix interne / mutualisé / SaaS pour un service courant | Moyen | Stable sur la méthode |
| Sortie d'un hébergeur en cours | Élevé (continuité du service public) | À vérifier sur le contrat et les dates |

## 12. Checklist de branche

1. **Garde-fou incident** (`SKILL.md` §5.2) : un incident chez l'hébergeur
   est-il en cours ou récent ? Si oui, le STOP est-il en premier ?
2. **Garde-fou surveillance** (`SKILL.md` §5.3) : la demande vise-t-elle les
   journaux ou contenus d'une personne ? Si oui, STOP et bascule avant tout
   contenu technique.
3. **Mode d'exercice** levé ou demandé (§4) ?
4. **Données qualifiées** (§5.2) avant toute comparaison d'offres ?
5. **Applicabilité** : SREN et doctrine « cloud au centre » présentées comme
   bonnes pratiques, jamais comme obligations ? Traduction anglaise écartée ?
6. **SecNumCloud** présenté comme exigence possible de l'acheteur, pas comme
   obligation ? Catalogue renvoyé à la date de la décision ?
7. **Réversibilité** et **localisation** formulées comme exigences, avec
   essai prévu ?
8. **`BASCULE dpo-ct`** affichée, avec `dpo-ct` nommé, avant tout contenu sur
   les transferts ou la sous-traitance au sens du RGPD ?
9. **Contrats** renvoyés à `references/contrats-prestataires.md` ; budget à
   `dirfi-fpt` ; passation signalée hors périmètre, sans esquisse ?
10. **Aucun fournisseur ni marque** nommé ou recommandé ?
11. **Aucune valeur** (date, version, délai) énoncée sans vérification en
    session et sans provenance ?
12. **Homologation** relancée pour le système hébergé ?
13. **Décision** renvoyée à l'exécutif, pas prise par la DSI ?
14. **Aucun secret** ni détail d'architecture exploitable ?
15. Chemins des fichiers mobilisés cités ; couple **[risque / confiance]**
    donné ; cas journalisable proposé pour `JOURNAL.md` ?
