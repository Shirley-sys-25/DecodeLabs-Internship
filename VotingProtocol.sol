// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VotingProtocol {
    // 1. STRUCTURES DE DONNÉES (Les "Moules")
    
    // Structure d'un électeur
    struct Voter {
        uint weight;       // Poids du vote (1 s'il est autorisé)
        bool voted;        // true si l'électeur a déjà voté
        address delegate;  // Adresse déléguée (optionnel)
        uint vote;         // Index du candidat choisi
    }

    // Structure d'un candidat (Proposition)
    struct Proposal {
        bytes32 name;      // Nom du candidat
        uint voteCount;    // Nombre total de votes reçus
    }

    // 2. VARIABLES D'ÉTAT (La Base de Données)
    
    // Adresse du président (celui qui déploie le contrat)
    address public chairperson;
    
    // Base de données des électeurs (Adresse => Électeur)
    mapping(address => Voter) public voters;
    
    // Tableau contenant tous les candidats
    Proposal[] public proposals;

    
    // 3. INITIALISATION (Le Constructeur)
    
    constructor(bytes32[] memory proposalNames) {
        chairperson = msg.sender;
        voters[chairperson].weight = 1;

        // Création des candidats initiaux
        for (uint i = 0; i < proposalNames.length; i++) {
            proposals.push(Proposal({
                name: proposalNames[i],
                voteCount: 0
            }));
        }
    }

    // 4. AUTORISATION (Le "Digital Bouncer")
    
    function giveRightToVote(address voter) public {
        require(msg.sender == chairperson, "Seul le president peut autoriser.");
        require(!voters[voter].voted, "Cet electeur a deja vote.");
        require(voters[voter].weight == 0, "Cet electeur a deja le droit de voter.");

        voters[voter].weight = 1;
    }

    // 5. LE VOTE (Checks, Effects, Interactions)
    
    function vote(uint proposal) public {
        Voter storage sender = voters[msg.sender];

        // Checks (Vérifications)
        require(sender.weight != 0, "Vous n'avez pas le droit de voter.");
        require(!sender.voted, "Vous avez deja vote.");

        // Effects (Mise à jour de l'état)
        sender.voted = true;
        sender.vote = proposal;

        // Interactions (Comptage des voix)
        proposals[proposal].voteCount += sender.weight;
    }

    // 6. RÉSULTATS (Tallying)
    
    function winningProposal() public view returns (uint winningProposal_) {
        uint winningVoteCount = 0;
        for (uint p = 0; p < proposals.length; p++) {
            if (proposals[p].voteCount > winningVoteCount) {
                winningVoteCount = proposals[p].voteCount;
                winningProposal_ = p;
            }
        }
    }

    function winnerName() public view returns (bytes32 winnerName_) {
        winnerName_ = proposals[winningProposal()].name;
    }
}