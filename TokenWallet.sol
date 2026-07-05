// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TokenWallet {

    // 1. INFORMATIONS DU TOKEN
    string public name = "DecodeLabs Token";
    string public symbol = "DLT";
    uint8 public decimals = 18; // Standard ERC-20 (18 zéros pour gérer les fractions)
    uint256 public totalSupply;

    // 2. LA BASE DE DONNÉES (Le Registre)

    // Stockage de solde de chaque utilisateur
    mapping(address => uint256) public balanceOf;

    
    // 3. LES ÉVÉNEMENTS (OUTPUT)
    event Transfer(address indexed from, address indexed to, uint256 value);

    // 4. LE CONSTRUCTEUR (Création de la monnaie)
    constructor(uint256 initialSupply) {
        // Création de la quantité initiale de tokens et envoie de token au créateur du contrat
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
    }

    // 5. LA FONCTION DE TRANSFERT (IPO Architecture)
    // ==========================================
    function transfer(address to, uint256 amount) public returns (bool) {
        
        // --- ETAPE 1 : INPUT & CHECKS (Sécurité) ---
        // Vérification de l'adresse de destination (pas d'envoi dans le vide)
        require(to != address(0), "Adresse de destination invalide.");
        
        // C'est le "Gatekeeper" qui bloque les transactions illégales.
        require(balanceOf[msg.sender] >= amount, "Fonds insuffisants.");

        // --- ETAPE 2 : PROCESS (Manipulation de l'état) ---
        // On soustrait l'argent de l'expéditeur (le compilateur 0.8.0+ gère l'anti-underflow natif)
        balanceOf[msg.sender] -= amount;
        
        // On ajoute l'argent au destinataire
        balanceOf[to] += amount;

        // --- ETAPE 3 : OUTPUT (Synchronisation) ---
        // On émet l'événement pour la blockchain et l'interface utilisateur
        emit Transfer(msg.sender, to, amount);

        return true;
    }
}