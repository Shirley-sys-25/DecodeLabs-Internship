import hashlib
import time


# 1. LA STRUCTURE DU BLOC (Le Moule)

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index                  # Position du bloc dans la chaîne
        self.timestamp = time.time()        # Date et heure exactes de la création
        self.data = data                    # Les informations à sécuriser (ex: transaction)
        self.prev_hash = prev_hash          # L'empreinte du bloc précédent (le lien)
        self.nonce = 0                      # Compteur utilisé pour la Preuve de Travail (Minage)
        self.hash = self.calculate_hash()   # Calcule l'empreinte dès la création du bloc

    
    # 2. LA CRYPTOGRAPHIE (Le Cadenas)
    
    def calculate_hash(self):
        # On regroupe toutes les infos du bloc en une seule chaîne de texte
        texte_a_hacher = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_hash) + str(self.nonce)
        # On utilise l'algorithme SHA-256 pour générer l'empreinte unique de 256 bits
        return hashlib.sha256(texte_a_hacher.encode()).hexdigest()

    
    # 3. LA PREUVE DE TRAVAIL (Le Minage)
    
    def mine_block(self, difficulty):
        cible = "0" * difficulty  # Ex: si difficulty = 4, la cible est "0000"
        
        # Tant que le hash ne commence pas par "0000", la machine cherche
        while not self.hash.startswith(cible):
            self.nonce += 1                     # On essaie le nombre suivant
            self.hash = self.calculate_hash()   # On recalcule le hash avec ce nouveau nombre
            
        print(f"Bloc {self.index} miné ! Nonce : {self.nonce} | Hash : {self.hash}")


# 4. LE REGISTRE (La Blockchain)

class Blockchain:
    def __init__(self):
        self.chain = []               # La liste Python qui contient tous nos blocs
        self.create_genesis_block()   # Crée le 1er bloc automatiquement au lancement

    def create_genesis_block(self):
        print("--- Initialisation de la Blockchain ---")
        # Le bloc Genesis a l'index 0 et un prev_hash codé à "0" car il n'a pas de parent
        genesis_block = Block(0, "Bloc Genesis (Origine)", "0")
        genesis_block.mine_block(4)
        self.chain.append(genesis_block)

    def add_block(self, nouveau_bloc):
        # On récupère le dernier bloc de la liste (index -1) pour créer le lien
        dernier_bloc = self.chain[-1]
        nouveau_bloc.prev_hash = dernier_bloc.hash
        
        # On met à jour le hash du nouveau bloc car son prev_hash a changé
        nouveau_bloc.hash = nouveau_bloc.calculate_hash() 
        
        # On mine le nouveau bloc avant de l'accepter définitivement
        print(f"Minage du bloc {nouveau_bloc.index} en cours...")
        nouveau_bloc.mine_block(4)
        self.chain.append(nouveau_bloc)


    # 5. LA SÉCURITÉ ET L'IMMUTABILITÉ (La Validation)

    def validate_chain(self):
        # On vérifie chaque bloc un par un, en commençant par le bloc 1
        for i in range(1, len(self.chain)):
            bloc_actuel = self.chain[i]
            bloc_precedent = self.chain[i-1]

            # Vérification 1 : Les données ont-elles été modifiées (falsification) ?
            if bloc_actuel.hash != bloc_actuel.calculate_hash():
                print(f"🚨 ALERTE : Falsification détectée sur le bloc {bloc_actuel.index} !")
                return False

            # Vérification 2 : Le lien avec le bloc précédent est-il cassé ?
            if bloc_actuel.prev_hash != bloc_precedent.hash:
                print(f"🚨 ALERTE : Lien cryptographique brisé au niveau du bloc {bloc_actuel.index} !")
                return False

        print("✅ SUCCÈS : La blockchain est 100% sécurisée et intègre.")
        return True


# TESTS ET SIMULATION

if __name__ == "__main__":
    # 1. Lancement de la blockchain (crée le Genesis)
    ma_blockchain = Blockchain()

    # 2. Création et ajout de deux blocs de transactions
    bloc1 = Block(1, "Paiement de 50 EUR", "")
    ma_blockchain.add_block(bloc1)

    bloc2 = Block(2, "Contrat de stage signé", "")
    ma_blockchain.add_block(bloc2)

    # 3. Vérification de la chaîne (devrait indiquer un succès)
    print("\n--- Vérification Initiale ---")
    ma_blockchain.validate_chain()

    # 4. Simulation de piratage (On falsifie la donnée du bloc 1)
    print("\n[PIRATAGE] Un hacker modifie le bloc 1 (50 EUR -> 5000 EUR)...")
    ma_blockchain.chain[1].data = "Paiement de 5000 EUR"

    # 5. Seconde vérification (L'alerte doit se déclencher immédiatement)
    print("\n--- Vérification après piratage ---")
    ma_blockchain.validate_chain()

    