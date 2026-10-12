# Socle de sources - Lot 1 : droit administratif du numérique

- **Date d'évaluation (champ `as_of_date` des résultats d'outil)** : 2026-10-05 (date du jour du serveur Légifrance). Colonne « Vérifié le » = 2026-10-05 pour toutes les lignes.
- **Outil principal** : serveur MCP `Droit_Francais` (`search_articles`, `get_article`), source « Légifrance API », droit en vigueur à la date du serveur (aucune date passée en paramètre, sauf deux interrogations de versions futures signalées).
- **Repli signalé** : `search`, `get_text` et `fetch` du même serveur ne couvrent pas les textes hors codes (loi, ordonnance, décrets). Pour obtenir les identifiants JORFTEXT et les identifiants LEGIARTI de ces textes, j'ai utilisé `WebFetch` sur des pages legifrance.gouv.fr. Ce résultat est un résumé produit par un petit modèle, pas une copie littérale. Règle appliquée : **tout LEGIARTI de ce lot a été relu article par article avec `get_article`** (texte, statut et dates lus dans l'API). Les identifiants JORFTEXT (textes entiers) ne reposent que sur WebFetch, donc la colonne Statut le précise.
- **Rappel : aucune référence, aucun identifiant ni aucune date ne vient de la mémoire.** Tout ce qui figure ci-dessous a été lu dans un résultat d'outil pendant cette tâche. Ce qui n'a pas pu l'être est marqué « ⚠️ non vérifié ».
- Le serveur limite le débit (environ 10 requêtes par minute). Des erreurs « Quota individuel atteint » ont obligé à relancer des appels, sans effet sur les résultats.

## Tableau

Convention : « CRPA » = Code des relations entre le public et l'administration ; « CCP » = Code de la commande publique. Les mentions « inférence » signalent une applicabilité déduite d'un terme général du texte lu (par exemple « personnes morales de droit public ») et non d'une mention expresse des collectivités.

### 1. Définition de l'administration (CRPA)

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités (oui/non/sous conditions + fondement) |
|---|---|---|---|---|---|---|
| CRPA, art. L. 100-3 | Définit « administration » et « public » pour l'ensemble du code, sauf disposition contraire. | 2016-01-01 | LEGIARTI000031367308 | 2026-10-05 | vérifié (en vigueur) | **Oui** : « les administrations de l'Etat, les collectivités territoriales, leurs établissements publics administratifs et les organismes et personnes de droit public et de droit privé chargés d'une mission de service public administratif ». Réserve : « sauf disposition contraire » du code. |

### 2. Saisine par voie électronique (CRPA)

La sous-section 1 « Droit de saisine par voie électronique » regroupe, dans les résultats lus, L. 112-8, L. 112-9, L. 112-10, R. 112-9-1 et R. 112-9-2. L. 112-11 appartient à la sous-section 2 voisine (accusé de réception). Les recherches de R. 112-9, R. 112-9-3, R. 112-9-4 et R. 112-9-5 n'ont renvoyé aucun résultat.

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités |
|---|---|---|---|---|---|---|
| CRPA, art. L. 112-8 | Toute personne identifiée peut saisir une administration par voie électronique et celle-ci traite l'envoi sans exiger sa confirmation sous une autre forme. | 2016-01-01 | LEGIARTI000031367348 | 2026-10-05 | vérifié (en vigueur) | **Oui, sauf démarches exclues** : vise « une administration » (L. 100-3 inclut les collectivités). Démarches exclues pour les collectivités par le décret n° 2016-1491 (ligne ci-dessous). |
| CRPA, art. L. 112-9 | L'administration met en place un ou plusieurs téléservices ; leurs modalités d'utilisation s'imposent au public ; le téléservice dédié devient la seule voie de saisine régulière. | 2016-01-01 | LEGIARTI000031367350 | 2026-10-05 | vérifié (en vigueur) | **Oui, sauf démarches exclues** : même fondement (« L'administration »). Renvoie aux règles de sécurité et d'interopérabilité de l'ordonnance n° 2005-1516. |
| CRPA, art. L. 112-10 | Permet d'écarter L. 112-8 et L. 112-9 pour certaines démarches, par décret en Conseil d'État, pour des motifs d'ordre public, de défense et sécurité nationale, de bonne administration ou de présence personnelle nécessaire. | 2018-05-25 | LEGIARTI000033221175 | 2026-10-05 | vérifié (en vigueur) | **Oui** (base légale des décrets d'exception, dont celui qui vise les collectivités). |
| CRPA, art. R. 112-9-1 | Précise les éléments d'identification que la personne fournit pour saisir l'administration par voie électronique. | 2016-11-07 | LEGIARTI000033288123 | 2026-10-05 | vérifié (en vigueur) | **Oui** : « toute personne s'identifie auprès de cette administration » (administration au sens de L. 100-3). |
| CRPA, art. R. 112-9-2 | L'administration informe le public de ses téléservices ; à défaut, tout envoi électronique vaut saisine ; un formulaire de contact ou une adresse électronique peuvent constituer un téléservice. | 2016-11-07 | LEGIARTI000033288120 | 2026-10-05 | vérifié (en vigueur) | **Oui** : même fondement. |
| CRPA, art. L. 112-11 (voisin, sous-section 2) | Tout envoi électronique et tout paiement par téléservice font l'objet d'un accusé de réception électronique, émis selon le RGS. | 2016-10-09 | LEGIARTI000033219980 | 2026-10-05 | vérifié (en vigueur) | **Oui** : « Tout envoi à une administration par voie électronique » ; renvoi au « I de l'article 9 » de l'ordonnance n° 2005-1516. Exception pour envois abusifs ou susceptibles de porter atteinte à la sécurité du système d'information. |
| Décret n° 2016-1491 du 4 novembre 2016 (exceptions à la saisine par voie électronique : collectivités territoriales, établissements publics, EPCI), art. 1 | Écarte L. 112-8 et L. 112-9 pour les démarches listées aux annexes 1 et 2. | art. 1 : 2016-11-07 ; annexe 1 : 2016-11-07 ; annexe 2 : 2018-11-07 | JORFTEXT000033342129 (texte) ; art. 1 : LEGIARTI000033343854 ; annexe 1 : LEGIARTI000033343812 ; annexe 2 : LEGIARTI000037563558 | 2026-10-05 | vérifié pour les LEGIARTI (API) ; JORFTEXT lu via WebFetch seulement | **Sous conditions** : s'applique aux démarches de la liste. Annexe 1 (« EXCEPTIONS À TITRE DÉFINITIF », motif de bonne administration) : autorisations ERP, dérogations d'accessibilité, travaux d'IGH, remontées mécaniques. Annexe 2 : exceptions transitoires dont les échéances lues sont « 31 DÉCEMBRE 2021 » (urbanisme) et « 7 NOVEMBRE 2018 » (MDPH, RSA), donc échues au 2026-10-05. |

### 3. Algorithmes (CRPA)

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités |
|---|---|---|---|---|---|---|
| CRPA, art. L. 311-3-1 | Une décision individuelle fondée sur un traitement algorithmique comporte une mention explicite, et les règles du traitement sont communiquées à l'intéressé sur demande. | 2016-10-09 | LEGIARTI000033205535 | 2026-10-05 | vérifié (en vigueur) | **Oui** : « communiquées par l'administration » (L. 100-3). Aucun seuil d'effectif dans le texte lu. Réserve : « Sous réserve de l'application du 2° de l'article L. 311-5 » (secrets protégés). |
| CRPA, art. R. 311-3-1-1 | Contenu de la mention explicite : finalité du traitement, droit à communication des règles, modalités d'exercice et de saisine de la CADA. | 2017-09-01 | LEGIARTI000034195878 | 2026-10-05 | vérifié (en vigueur) | **Oui** : texte d'application de L. 311-3-1 (même champ). |
| CRPA, art. R. 311-3-1-2 | À la demande de la personne, l'administration communique, sous forme intelligible, le degré et le mode de contribution du traitement, les données et leurs sources, les paramètres (et pondérations) et les opérations effectuées. | 2017-09-01 | LEGIARTI000034195881 | 2026-10-05 | vérifié (en vigueur) | **Oui** : « L'administration communique ». Réserve : « sous réserve de ne pas porter atteinte à des secrets protégés par la loi ». |
| CRPA, art. L. 312-1-3 | Les administrations de L. 300-2 publient en ligne les règles des principaux traitements algorithmiques fondant des décisions individuelles. | 2016-10-09 | LEGIARTI000033205516 | 2026-10-05 | article vérifié ; **seuil d'effectif : ⚠️ non vérifié** | **Sous conditions** : vise « les administrations mentionnées au premier alinéa de l'article L. 300-2 » (qui cite « les collectivités territoriales »), « à l'exception des personnes morales dont le nombre d'agents ou de salariés est inférieur à un seuil fixé par décret ». La valeur du seuil n'est pas dans le texte de l'article ; le décret qui la fixe n'a pas été identifié (D. 312-1-3, lu, ne la contient pas). |

### 4. Documents communicables (CRPA)

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités |
|---|---|---|---|---|---|---|
| CRPA, art. L. 300-2 | Définit les documents administratifs communicables, dont les « codes sources », produits ou reçus dans le cadre d'une mission de service public. | 2016-10-09 | LEGIARTI000033218936 | 2026-10-05 | vérifié (en vigueur) | **Oui** : « produits ou reçus, dans le cadre de leur mission de service public, par l'Etat, les collectivités territoriales » ; liste « notamment » incluant « codes sources ». Champ limité aux titres Ier, III et IV du livre III. |

### 5. Échanges de données entre administrations (CRPA)

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités |
|---|---|---|---|---|---|---|
| CRPA, art. L. 114-8 | Les administrations échangent entre elles les données strictement nécessaires pour traiter une demande ou une déclaration du public (principe « dites-le-nous une fois »). | 2022-02-23 | LEGIARTI000045213315 | 2026-10-05 | vérifié (en vigueur) | **Oui, avec dérogation technique** : « les collectivités territoriales et les groupements de collectivités territoriales » ne sont pas tenus de transmettre en cas d'« impossibilité technique » (art. L. 114-10). |
| CRPA, art. L. 114-9 (voisin) | Renvoie à un décret en Conseil d'État (avis CNIL) les modalités des échanges (sécurité, traçabilité, données exclues, durée de conservation). | 2022-02-23 | LEGIARTI000045213308 | 2026-10-05 | vérifié (en vigueur) | **Oui** : vise les échanges entre « administrations » de L. 114-8. |
| CRPA, art. L. 114-10 (voisin) | Si les données ne peuvent être obtenues entre administrations (nature ou impossibilité technique), la personne les fournit. | 2018-08-12 | LEGIARTI000037313148 | 2026-10-05 | vérifié (en vigueur) | **Oui** : base de la dérogation visée à L. 114-8 I. |

### 6. Accessibilité numérique : loi du 11 février 2005

Texte : « Loi n° 2005-102 du 11 février 2005 pour l'égalité des droits et des chances, la participation et la citoyenneté des personnes handicapées » (JORFTEXT000000809647, lu via WebFetch, « En vigueur au 05/10/2026 »).

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités |
|---|---|---|---|---|---|---|
| Loi n° 2005-102, art. 47 | Rend accessibles aux personnes handicapées les services de communication au public en ligne (sites, intranet, extranet, applications mobiles, progiciels, mobilier urbain numérique) ; impose déclaration d'accessibilité, schéma pluriannuel (durée maximale 3 ans, décliné en plans d'actions annuels) et mention en page d'accueil. | 2023-09-08 | LEGIARTI000048050213 (texte : JORFTEXT000000809647) | 2026-10-05 | vérifié (art. en vigueur) ; JORFTEXT via WebFetch | **Oui (inférence)** : le I, 1°, vise « Les personnes morales de droit public », catégorie qui couvre les collectivités ; l'article ne nomme pas expressément les collectivités. Le 2° vise aussi les personnes morales de droit privé délégataires de mission de service public et certaines structures qu'elles financent ou contrôlent. Charge disproportionnée : exception prévue au II (définie par décret). |
| Loi n° 2005-102, art. 47-1 | Confie à l'Arcom le contrôle des manquements à l'art. 47 (procès-verbaux, mise en demeure rendue publique) et prévoit, à défaut de mise en conformité, une sanction pécuniaire (plus sanction complémentaire de publicité) ; nouvelle sanction possible si le manquement perdure six mois. | 2023-09-08 | LEGIARTI000048050174 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : la sanction vise les « personnes mentionnées aux 1° à 3° du I de l'article 47 » (dont personnes morales de droit public). **Montant à reporter dans le cache des valeurs.** |

### 7. Décret n° 2019-768 du 24 juillet 2019

Texte : « Décret n° 2019-768 du 24 juillet 2019 relatif à l'accessibilité aux personnes handicapées des services de communication au public en ligne », JORFTEXT000038811937 (lu via WebFetch ; statut « En vigueur » ; dernière version consolidée annoncée au 2026-08-27, ⚠️ résumé WebFetch).

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités |
|---|---|---|---|---|---|---|
| Décret n° 2019-768, art. 1 | Les services en ligne des personnes de l'art. 47 I 1° à 4° doivent être accessibles conformément aux normes harmonisées publiées au JOUE (directive (UE) 2016/2102, art. 6). | **2026-08-27** | LEGIARTI000054748661 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : « personnes mentionnées aux 1° à 4° du I de l'article 47 de la loi du 11 février 2005 » (donc 1° personnes morales de droit public). |
| Décret n° 2019-768, art. 2 | Fixe le seuil de chiffre d'affaires applicable aux entreprises du 4° du I de l'art. 47 (valeur : à reporter dans le cache des valeurs). | 2019-07-26 | LEGIARTI000038956842 | 2026-10-05 | vérifié (en vigueur) | **Non** : ne vise que « les entreprises mentionnées au 4° du I » ; sans objet pour une collectivité. |
| Décret n° 2019-768, art. 5 | Un référentiel d'accessibilité, arrêté conjointement par le ministre chargé des personnes handicapées et celui chargé du numérique, fixe les modalités techniques, le format des documents de l'art. 47 III-IV et la méthode de vérification. | **2026-08-27** | LEGIARTI000054748666 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : le référentiel s'applique aux services des personnes de l'art. 47. |
| Décret n° 2019-768, art. 6 | Impose la publication en ligne de la déclaration d'accessibilité, son contenu minimal et sa communication à l'administration par téléservice. | 2019-07-26 | LEGIARTI000038956852 | 2026-10-05 | vérifié (en vigueur) | **Oui** : « Les personnes mentionnées aux 1° à 4° du I de l'article 47 ». |

Autres articles du décret signalés par WebFetch mais non relus : 3 (LEGIARTI000038956844), 4 (LEGIARTI000038956846), 7, 9 à 13. Statut : ⚠️ non vérifié.

### 8. Ordonnance n° 2005-1516 du 8 décembre 2005

Texte : « Ordonnance n° 2005-1516 du 8 décembre 2005 relative aux échanges électroniques entre les usagers et les autorités administratives et entre les autorités administratives », JORFTEXT000000636232 (lu via WebFetch, « En vigueur au 05/10/2026 »). L'identifiant LEGITEXT000000636232 indiqué par WebFetch n'a pas pu être confirmé : `get_text` a renvoyé une erreur « Source officielle non vérifiée (code 4) ». ⚠️ non vérifié.

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités |
|---|---|---|---|---|---|---|
| Ordonnance n° 2005-1516, art. 1 | Définit les « autorités administratives » et les notions de système d'information, prestataire de services de confiance, produit de sécurité et téléservice. | 2017-01-29 | LEGIARTI000033974978 | 2026-10-05 | vérifié (en vigueur) | **Oui** : « Sont considérés comme autorités administratives au sens de la présente ordonnance les administrations de l'Etat, les collectivités territoriales, les établissements publics à caractère administratif [...] ». |
| Ordonnance n° 2005-1516, art. 9 | I : crée le référentiel général de sécurité (RGS). II : lorsqu'une autorité administrative met en place un système d'information, elle détermine les fonctions de sécurité nécessaires, fixe le niveau de sécurité requis et respecte les règles du RGS. III : qualification des produits de sécurité et prestataires de services de confiance. | 2005-12-09 | LEGIARTI000006317203 | 2026-10-05 | vérifié (en vigueur) | **Oui** : « Lorsqu'une autorité administrative met en place un système d'information, elle détermine les fonctions de sécurité nécessaires pour protéger ce système » ; « autorité administrative » inclut les collectivités (art. 1). |

### 9. Décret n° 2010-112 du 2 février 2010 (RGS)

Texte : « Décret n° 2010-112 du 2 février 2010 pris pour l'application des articles 9, 10 et 12 de l'ordonnance n° 2005-1516 du 8 décembre 2005 [...] », JORFTEXT000021779444 (lu via WebFetch, statut « En vigueur »).

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités |
|---|---|---|---|---|---|---|
| Décret n° 2010-112, art. 1 | Le RGS fixe les règles auxquelles les systèmes d'information mis en place par les autorités administratives doivent se conformer (confidentialité, intégrité, disponibilité, identification). | 2010-02-05 | LEGIARTI000021780146 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : « autorités administratives » ; le décret renvoie à l'ordonnance, dont l'art. 1 inclut les collectivités. |
| Décret n° 2010-112, art. 2 | Le RGS et ses mises à jour sont approuvés par arrêté du Premier ministre publié au JO ; l'ANSSI concourt à son élaboration. | 2019-10-28 | LEGIARTI000039286010 | 2026-10-05 | vérifié (en vigueur) | Sans objet direct (norme d'élaboration), RGS opposable aux autorités administratives. |
| Décret n° 2010-112, art. 3 | L'autorité administrative identifie les risques, fixe les objectifs de sécurité, en déduit les fonctions de sécurité et leur niveau, et réexamine régulièrement la sécurité. | 2010-02-05 | LEGIARTI000021780150 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : obligation portée par « l'autorité administrative ». |
| Décret n° 2010-112, art. 4 | Pour mettre en œuvre les fonctions de sécurité, l'autorité recourt à des produits et prestataires qualifiés, ou à d'autres dont elle s'est assurée de la conformité au RGS. | 2010-02-05 | LEGIARTI000021780154 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : même sujet. |
| Décret n° 2010-112, art. 5 (**attestation formelle** ; mécanisme d'« homologation » du RGS, voir Points d'attention) | « L'autorité administrative atteste formellement auprès des utilisateurs de son système d'information que celui-ci est protégé conformément aux objectifs de sécurité » ; pour un téléservice, l'attestation est rendue accessible aux usagers. | 2016-03-19 | LEGIARTI000033232490 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : c'est l'autorité administrative elle-même, donc la collectivité pour ses systèmes, qui atteste. Aucune autorité extérieure ne délivre cet acte dans le texte lu. |
| Décret n° 2010-112, art. 6 | La demande de qualification d'un produit de sécurité est adressée à l'ANSSI. | 2010-02-05 | LEGIARTI000021780156 | 2026-10-05 | vérifié (en vigueur) | Sans objet direct (qualification de produits, pas de systèmes). |
| Décret n° 2010-112, art. 9 | Le directeur général de l'ANSSI délivre la qualification du produit à un niveau du référentiel, avec durée de validité, conditions et réserves possibles ; suspension ou retrait possibles. | 2019-11-09 | LEGIARTI000039353401 | 2026-10-05 | vérifié (en vigueur) | Sans objet direct (qualification de produits). |

Articles 7, 8, 10 à 24 du décret : identifiants listés par WebFetch, texte non relu. Statut : ⚠️ non vérifié.

### 10. Facturation électronique (Code de la commande publique)

| Référence | Objet (une phrase) | Version en vigueur depuis | Identifiant | Vérifié le | Statut | Applicable aux collectivités |
|---|---|---|---|---|---|---|
| CCP, art. L. 2192-1 | Les titulaires de marchés conclus avec des personnes morales de droit public, et leurs sous-traitants admis au paiement direct, **transmettent** leurs factures sous forme électronique. | 2024-07-01 | LEGIARTI000046195587 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : l'obligation d'émission pèse sur les fournisseurs, vis-à-vis des « personnes morales de droit public » (donc les collectivités comme clientes). |
| CCP, art. L. 2192-2 | Les personnes morales de droit public **acceptent** les factures électroniques transmises par les titulaires de marchés et sous-traitants admis au paiement direct. | 2024-07-01 | LEGIARTI000046195584 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : l'obligation de réception pèse sur les personnes morales de droit public. |
| CCP, art. L. 2192-3 | Les acheteurs acceptent les factures conformes à la norme de facturation électronique définie par voie réglementaire. | 2019-07-22 | LEGIARTI000038541739 | 2026-10-05 | vérifié (en vigueur) | **Oui (inférence)** : « les acheteurs » (hors champ précis de ce texte, à croiser avec L. 1210-1 non lu). |
| CCP, art. L. 2192-4 | Renvoie au pouvoir réglementaire les modalités d'application de la sous-section, dont les mentions obligatoires. | 2019-07-22 | LEGIARTI000038540575 | 2026-10-05 | vérifié (en vigueur) | Sans objet direct. |
| CCP, art. L. 2192-5 (version en vigueur) | Crée le « portail public de facturation » (solution mutualisée de l'État) que doivent utiliser l'État, les collectivités territoriales, les établissements publics et leurs fournisseurs. | 2026-02-21 (jusqu'au 2027-01-01, statut API « ABROGE_DIFF ») | LEGIARTI000053546705 | 2026-10-05 | vérifié (en vigueur, version à échéance) | **Oui, expressément** : « 1° L'Etat, les collectivités territoriales et les établissements publics ». |
| CCP, art. L. 2192-5 (**version future**) | Même dispositif, la référence aux mentions de facture passant à l'article L. 216-36 du code des impositions sur les biens et services. | **2027-01-01** (statut API « VIGUEUR_DIFF ») | LEGIARTI000054567709 | 2026-10-05 | vérifié (version future, non applicable au 2026-10-05) | **Oui, expressément** : même liste. |
| CCP, art. L. 2192-6 | Exclut de la sous-section 1 les factures de marchés de l'État et ses EP en cas d'impératif de défense ou de sécurité nationale, de la CDC, de l'établissement public de l'art. L. 2142-1 du code des transports et de la SNCF (SNCF Réseau, SNCF Voyageurs). | 2020-01-01 | LEGIARTI000038960975 | 2026-10-05 | vérifié (en vigueur) | **Non applicable aux collectivités** : aucune des exclusions listées ne vise une collectivité territoriale. |
| CCP, art. L. 2192-7 | Renvoie au pouvoir réglementaire les modalités d'application de la sous-section 2 (portail public de facturation). | 2019-07-22 | LEGIARTI000038540563 | 2026-10-05 | vérifié (en vigueur) | Sans objet direct. |

## Points d'attention

### Erreurs ou présupposés de l'énoncé du lot

1. **« Homologation de sécurité » dans le décret n° 2010-112** : les articles lus (1 à 6 et 9) n'emploient pas le mot. L'article 5 ne prévoit pas qu'un tiers homologue : « L'autorité administrative atteste formellement auprès des utilisateurs de son système d'information » que celui-ci est protégé. Donc c'est la collectivité elle-même (l'autorité administrative) qui atteste. Le directeur général de l'ANSSI ne délivre que la **qualification de produits** (art. 9), pas l'homologation de systèmes. Une recherche WebFetch du mot « homologation » dans l'ensemble du décret est restée sans résultat (⚠️ résultat de résumé, articles 7, 8, 10 à 24 non relus). Ne pas écrire dans le skill « l'ANSSI homologue » ni « l'autorité de homologation = le maire » sans autre source.
2. **Sanction d'accessibilité** : elle n'est pas à l'art. 47 de la loi de 2005 mais à l'**art. 47-1** (LEGIARTI000048050174) ; l'art. 47 lu ne contient aucune sanction. Autorité de contrôle et de sanction : Arcom (« Autorité de régulation de la communication audiovisuelle et numérique »). Nature : sanction pécuniaire après mise en demeure rendue publique, plus sanction de publicité.
3. **Seuil d'effectif de L. 312-1-3** : il n'est pas dans l'article, qui renvoie à « un seuil fixé par décret ». Le décret n'a pas été identifié ; l'article D. 312-1-3 (testé car son numéro semblait proche) traite d'une autre matière (catégories de documents publiables sans anonymisation). ⚠️ seuil non vérifié, à ne pas affirmer dans le skill avant relecture de l'article réglementaire exact.
4. **Facturation électronique, « qui est tenu d'émettre ou de recevoir »** : L. 2192-1 impose l'**émission** aux titulaires de marchés (fournisseurs). Les collectivités ne sont pas visées par une obligation d'émettre dans les articles lus : elles doivent **accepter** (L. 2192-2) et **utiliser le portail public de facturation** (L. 2192-5).
5. Les numéros d'articles de l'énoncé (L. 100-3, L. 112-8, L. 311-3-1, R. 311-3-1-1, R. 311-3-1-2, L. 312-1-3, L. 300-2, L. 114-8, art. 47 loi 2005, art. 9 ordonnance, L. 2192-1) existent tous et sont en vigueur à la date lue.

### Versions futures, modifications récentes, renvois douteux

6. **CCP L. 2192-5** : version en vigueur valable jusqu'au 2027-01-01 (statut API « ABROGE_DIFF »), remplacée à cette date par LEGIARTI000054567709, qui renvoie à l'art. L. 216-36 du code des impositions sur les biens et services au lieu de l'art. 289 E du CGI. À réévaluer au 2027-01-01.
7. **Décret n° 2019-768** : les articles 1 et 5 ont une version en vigueur depuis le **2026-08-27**, soit une modification récente. Les autres articles lus (2, 6) datent de 2019-07-26. Les textes d'application (référentiel d'accessibilité) sont susceptibles d'avoir changé : à vérifier avant de citer le RGAA.
8. **Annexe 2 du décret n° 2016-1491** : le statut API est « VIGUEUR », mais les échéances écrites dans le texte (2018-11-07 et 2021-12-31) sont dépassées. Seule l'annexe 1 (exceptions définitives) reste utile pour une collectivité.
9. **Renvoi apparemment périmé** : l'art. 5 du décret n° 2010-112 (version 2016-03-19) renvoie à « l'article L. 112-10 du code des relations entre le public et l'administration pour la décision de création du téléservice ». Or L. 112-10 (version 2018-05-25) traite des exclusions par décret, sans mention de la décision de création de téléservice. À ne pas relayer sans vérification complémentaire.
10. L. 112-9 et L. 112-11 du CRPA renvoient à l'ordonnance n° 2005-1516 (chapitres IV et V pour L. 112-9 ; « I de l'article 9 » pour L. 112-11). Seul l'art. 9 a été lu ; les chapitres IV et V ne sont pas vérifiés.
11. La mention d'un LEGITEXT pour l'ordonnance (LEGITEXT000000636232) provient de WebFetch seulement ; `get_text` a échoué. ⚠️ non vérifié.

### Valeurs chiffrées rencontrées (à reporter dans un cache daté, pas dans le socle)

| Valeur | Source (article lu) | Observation |
|---|---|---|
| Sanction pécuniaire maximale : 50 000 € (non-respect de l'obligation d'accessibilité, art. 47 I) et 25 000 € (obligations des III et IV de l'art. 47) | Loi 2005-102, art. 47-1, II | Montants lus le 2026-10-05, à reporter dans le cache des valeurs. |
| Nouvelle sanction possible si le manquement perdure 6 mois après une sanction | Loi 2005-102, art. 47-1, III | Délai. |
| Durée maximale du schéma pluriannuel : 3 ans ; délais de mise en conformité fixés par décret : 3 ans maximum | Loi 2005-102, art. 47 III et V | Durées. |
| Seuil de chiffre d'affaires : 250 millions d'euros, moyenne sur 3 exercices | Décret 2019-768, art. 2 | Concerne les entreprises (4° du I), pas les collectivités. |
| Seuil d'effectif de L. 312-1-3 | Non lu | ⚠️ valeur inconnue, à trouver dans le décret d'application. |
| Dates charnières CCP L. 2192-5 : 2026-02-21 et 2027-01-01 | CCP L. 2192-5 (deux versions) | Échéances de version. |
| Échéances échues de l'annexe 2 du décret 2016-1491 : 2021-12-31 et 2018-11-07 | Décret 2016-1491, annexe 2 | Informatif. |

### Synthèse des statuts

- **Vérifié (texte lu via `get_article`, en vigueur au 2026-10-05)** : 41 identifiants LEGIARTI (dont une version future de L. 2192-5).
- **JORFTEXT** (loi 2005-102, ordonnance 2005-1516, décrets 2019-768, 2010-112, 2016-1491) : lus via WebFetch sur Légifrance, titres concordants ; non recoupés par l'API.
- **⚠️ non vérifié** : seuil d'effectif de L. 312-1-3 ; LEGITEXT de l'ordonnance ; articles du décret 2019-768 (3, 4, 7, 9 à 13) et du décret 2010-112 (7, 8, 10 à 24) non relus ; absence du mot « homologation » dans le décret 2010-112 (résumé WebFetch) ; chapitres IV et V de l'ordonnance.
