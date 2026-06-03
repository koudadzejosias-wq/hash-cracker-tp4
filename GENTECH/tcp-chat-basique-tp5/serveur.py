import socket

def demarrer_serveur():
    # 1. Création du socket (IPv4, TCP)
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host = '127.0.0.1'
    port = 9999
    
    # Permet de réutiliser le port immédiatement après la fermeture du script
    serveur_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    serveur_socket.bind((host, port))
    serveur_socket.listen(1)
    print(f"[*] Le serveur écoute sur {host}:{port}...")
    
    client_socket, client_address = serveur_socket.accept()
    print(f"[+] Connexion acceptée depuis {client_address[0]}:{client_address[1]}")
    print("[*] Chat continu activé. Tapez 'exit' pour quitter.\n")
    
    while True:
        # 1. Le serveur attend le message du client (Bloquant)
        donnees_recues = client_socket.recv(1024).decode('utf-8')
        
        # Si le client coupe proprement ou envoie 'exit'
        if not donnees_recues or donnees_recues.lower() == 'exit':
            print("[-] Le client a quitté le chat.")
            break
            
        print(f"[Client] : {donnees_recues}")
        
        # 2. Le serveur prépare sa réponse
        reponse = input("[Vous / Serveur] > ")
        client_socket.send(reponse.encode('utf-8'))
        
        if reponse.lower() == 'exit':
            print("[*] Vous avez fermé la connexion.")
            break
    
    # Nettoyage
    client_socket.close()
    serveur_socket.close()
    print("[*] Serveur éteint.")

if __name__ == "__main__":
    demarrer_serveur()