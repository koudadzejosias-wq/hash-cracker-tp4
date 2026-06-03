import socket

def demarrer_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host = '127.0.0.1'
    port = 9999
    
    try:
        print(f"[*] Tentative de connexion à {host}:{port}...")
        client_socket.connect((host, port))
        print("[+] Connecté au serveur !")
        print("[*] Chat continu activé. Tapez 'exit' pour quitter.\n")
        
        while True:
            # 1. Le client initie l'envoi
            message = input("[Vous / Client] > ")
            
            # Gestion du cas où l'utilisateur appuie juste sur Entrée (évite le blocage)
            if not message.strip():
                message = "(message vide)"
                
            client_socket.send(message.encode('utf-8'))
            
            if message.lower() == 'exit':
                print("[*] Vous avez fermé la connexion.")
                break
            
            # 2. Le client attend la réponse du serveur (Bloquant)
            reponse = client_socket.recv(1024).decode('utf-8')
            
            if not reponse or reponse.lower() == 'exit':
                print("[-] Le serveur a quitté le chat.")
                break
                
            print(f"[Serveur] : {reponse}")
            
    except ConnectionRefusedError:
        print("[-] Erreur : Le serveur est introuvable. Est-il bien lancé ?")
    finally:
        client_socket.close()
        print("[*] Connexion fermée.")

if __name__ == "__main__":
    demarrer_client()