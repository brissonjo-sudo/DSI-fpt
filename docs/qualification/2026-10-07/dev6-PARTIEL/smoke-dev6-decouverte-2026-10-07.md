# Découverte native dev.6 — 7 octobre 2026

Après l'installation isolée, le diagnostic officiel `codex debug prompt-input` a été exécuté une fois dans cet état, sans prompt utilisateur ni demande de réponse. Il a terminé avec code 0 en moins d'une seconde ; stderr vide. Aucun appel de modèle n'a été demandé. L'authentification n'a pas été testée ; aucune mesure réseau n'a été réalisée.

Le contexte réellement assemblé contient les **six skills du plugin 1.2.0-dev.6**, avec leurs **six descriptions complètes** et la racine du cache isolé. Chaque SKILL installé et chaque description ont été comparés au candidat gelé. Les quatre skills système Codex figurent également dans le catalogue, soit dix entrées au total. Aucune racine 1.1.1 n'y figure.

Source runtime : `3f0df285898cf1e36d1ddda8d85d0c4cd5e0903b`. SHA-256 du JSON brut : `4ebce008ecc8ce337310f65fdc7cb6729ce426634b3d057fdfdd2161f1dd4681`.

Les preuves locales sont `prompt-input.stdout.txt`, `prompt-input.stderr.txt`, `prompt-input.execution.json` et `discovery-verification.json`, dans `smoke-dev6-isole-20261007-211629-4dc9cd90`. Les scripts `observer-contexte-smoke-dev6.ps1` et `controler-decouverte-smoke-dev6.py` relient la commande, ses sorties et le catalogue aux octets du candidat ; ils refusent d'écraser les reçus.

Ce résultat établit la **découverte dans le contexte natif construit**. La sélection et le chargement par un modèle, la réponse métier, l'exposition effective du MCP configuré désactivé, l'accès aux sources, la validation humaine et juridique restent non établis. `release_ready=false`. Ce contrôle distinct ne modifie ni les entrées, ni le barème, ni les résultats de la campagne par lecture de fichiers.

La documentation décrit ce diagnostic comme un rendu des entrées visibles au modèle : [Developer commands](https://learn.chatgpt.com/docs/developer-commands). Le reçu réel, et non cette seule documentation, établit le résultat local ci-dessus.
