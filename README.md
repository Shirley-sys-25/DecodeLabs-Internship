** DecodeLabs Internship - Blockchain Development Portfolio**

Bienvenue sur mon dépôt GitHub ! Ce portfolio regroupe l'ensemble des projets techniques réalisés lors de mon stage intensif en ingénierie Blockchain chez DecodeLabs (Batch 2026).

L'objectif de ce stage était de maîtriser les fondations cryptographiques des registres distribués (Ledgers) et le développement de Smart Contracts sécurisés.

📁 Projets Réalisés

 - Projet 1 : Mini-Blockchain de A à Z (Python)

Fichier : blockchain.py
Création de l'infrastructure logicielle d'une blockchain privée pour comprendre le consensus décentralisé.

Compétences clés : Python, Hachage Cryptographique (SHA-256), Effet d'Avalanche.

Fonctionnalités : * Création de la structure des blocs (Index, Timestamp, Data, Prev_Hash).

Implémentation d'un algorithme de minage (Proof of Work).

Système de validation strict pour garantir l'immutabilité et détecter les falsifications de données.


- Projet 2 : Système de Vote Décentralisé (Solidity)

Fichier : VotingProtocol.sol
Développement d'un Smart Contract agissant comme un "videur numérique" pour garantir une élection inviolable sur la blockchain Ethereum.

Compétences clés : Solidity, EVM (Ethereum Virtual Machine), State Management, Remix IDE.

Fonctionnalités :

Architecture basée sur le modèle Checks-Effects-Interactions pour contrer les attaques.

Verrou anti-double-vote (Double-Voting Lockout) via l'utilisation stricte de la fonction require().

Comptage dynamique et sécurisé des voix (Dynamic Tallying).


- Projet 3 : Portefeuille ERC-20 & Transfert de Valeur (Solidity)

Fichier : TokenWallet.sol
Conception d'une cryptomonnaie standardisée (ERC-20) et d'un système de transfert de valeur hautement sécurisé.

Compétences clés : Standard ERC-20, Architecture IPO (Input-Process-Output), Logique Financière.

Fonctionnalités :

Création du "DecodeLabs Token" (DLT) avec une gestion de la double précision (18 décimales).

Mapping des soldes utilisateurs (balanceOf).

Sécurisation des transferts avec une protection stricte contre les découverts (Anti-Overdraft/Underflow).


* Comment tester ces projets ?

- Python (Projet 1) : Exécutez le fichier blockchain.py dans n'importe quel terminal local pour voir la simulation de minage et de détection de piratage.

- Solidity (Projets 2 & 3) : Copiez le code des fichiers .sol et collez-les dans Remix IDE. Compilez avec la version 0.8.0 (ou supérieure) et déployez sur la machine virtuelle de test (Remix VM) pour interagir avec les Smart Contracts.

Ce dépôt a été créé dans le cadre de la certification technique DecodeLabs.
