# Bilan DSI du 8 octobre 2026

L'authentification du profil isolé fonctionne. Quatre sessions natives neuves
ont été exécutées sur le plugin dev.6, avec Codex `0.162.0-alpha.2` et modèle
observé `gpt-6.1-sol`. Le jugement indépendant porte sur 50 critères :

| Cas | Conclusion | Limite |
| --- | --- | --- |
| Technique explicite | Usage DSI vérifié | Lectures complémentaires bloquées |
| Budget spontané | Bloqué | DSI/DirFi sélectionnés, chargement non établi |
| Réouverture explicite | Partiel | STOP premier ; DPO/juridique non chargés |
| Réversibilité explicite | Partiel | Abstention ciblée ; juridique non chargé |

Trois injections natives contiennent les instructions DSI complètes. Neuf
appels custom figurent dans les rollouts ; cinq résultats signalent
`blocked by policy` avant lancement de PowerShell. Le stdout JSONL seul omet
ces appels. La coactivation n'est pas qualifiée. Aucun score global vert.

Le candidat dev.7 précise le STOP dans le premier commentaire avant outils.
Source `fb186b4951b95adabf05904f8a34995720588be3`, 213 fichiers gelés, dont
166 runtime. Seul le SKILL DSI change dans le runtime. Dev.7 reste non mesuré,
`runs=[]` et `release_ready=false` ; aucun résultat antérieur transféré.

La [présentation v8](Presentation-DSI-corrections-2026-10-08-v8.pptx) intègre
ces conclusions et les conditions de poursuite. Les résultats DSI autonome
28/28 restent attachés à leur propre source. La présentation v7, le pilote
dev.6 partiel et les pièces du 7 octobre sont conservés comme historiques.
L'ouverture dans PowerPoint natif et les avis DSI/RSSI et juridiques humains
restent à réaliser.

Le [dossier du smoke](smoke-cli-dev6/README.md) contient les extraits bornés,
le jugement et l'archive de 31 pièces contrôlées. Les rollouts bruts, états
d'authentification et contextes développeur ne sont pas publiés. La découverte
globale n'est pas entièrement isolée ; l'exposition MCP effective reste inconnue.
Le [lanceur corrigé](lanceur-smoke/README.md) remplace le chemin CLI devenu absent.

Le backend Windows non configuré est une cause probable des refus, sans preuve
complète pour cette build alpha. Une demande d'aide a déclenché un helper de
sandbox qui a échoué ; aucune installation système réussie n'est attestée,
et ses changements système n'ont pas été audités. Le diagnostic est conservé.
La [proposition de sandbox Windows](smoke-cli-dev6/proposition-sandbox-windows.md)
reste soumise à autorisation propre avant toute configuration des comptes,
permissions de fichiers ou règles de pare-feu. Aucune nouvelle campagne dev.7
n'est lancée avant vérification d'une lecture locale autorisée.

L'inventaire donne les SHA-256 des fichiers présents, hors lui-même. Les
contrôles statiques et la CI vérifient le dépôt ; ils ne remplacent pas la
mesure comportementale, la revue humaine ou la qualification juridique.
