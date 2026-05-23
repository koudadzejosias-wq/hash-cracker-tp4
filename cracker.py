import hashlib
import time
# ==========================================
# 1. FONCTION DE HACHAGE
# ==========================================
def hash_password(password):
    """Prend un mot de passe en clair et retourne son hash SHA-256."""
    # L'algorithme a besoin d'octets (bytes), on utilise donc encode()
    encoded_pass = password.encode('utf-8')
    hash_obj = hashlib.sha256(encoded_pass)
    return hash_obj.hexdigest()
# ==========================================
# 2. ATTAQUE PAR DICTIONNAIRE
# ==========================================
def crack_hash(target_hash, dictionary_file):
    """Tente de trouver le mot de passe correspondant au hash donné."""
    print(f"[*] Début de l'attaque sur le hash : {target_hash[:10]}...")
    
    try:
        with open(dictionary_file, 'r') as file:
            # On lit chaque mot de passe dans le fichier
            for word in file:
                # On retire les retours à la ligne cachés (\n)
                clean_word = word.strip()
                
                # On hache le mot du dictionnaire
                word_hash = hash_password(clean_word)
                
                # On compare avec notre cible
                if word_hash == target_hash:
                    print(f"\n[+] SUCCÈS ! Mot de passe trouvé : '{clean_word}'")
                    return True
                    
        print("\n[-] Échec. Le mot de passe n'est pas dans le dictionnaire.")
        return False
        
    except FileNotFoundError:
        print("[-] Erreur : Fichier dictionnaire introuvable.")
# --- BLOC D'EXÉCUTION PRINCIPAL ---
if __name__ == "__main__":
    # Scénario : On a volé ce hash dans une base de données
    # (C'est le hash SHA-256 du mot "hacker2026")
    stolen_hash = "f11a4f02a9ebf5cc43e3ef7ff3deef2c56a7de7e5cfa5bd1adfb836e5cc18c64"
    
    print("--- OUTIL DE CRACKING ---")
    start_time = time.time()
    
    # On lance l'attaque avec notre fichier créé précédemment
    crack_hash(stolen_hash, "dico.txt")
    
    end_time = time.time()
    print(f"[*] Durée de l'opération : {round(end_time - start_time, 4)} secondes.")