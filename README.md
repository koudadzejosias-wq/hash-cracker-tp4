# TP4 - Outil de Hachage et Cracking (SHA-256)

Ce projet contient un script Python permettant de réaliser une attaque par dictionnaire sur un hash inconnu, illustrant les concepts de sécurité liés au stockage des mots de passe.

## Pourquoi utiliser SHA-256 plutôt que MD5 ?

Dans le cadre de la sécurité informatique, le choix de l'algorithme de hachage est crucial. **SHA-256** est aujourd'hui la norme, tandis que **MD5** est totalement obsolète pour plusieurs raisons majeures :

1. **Résistance aux collisions (Faiblesse de MD5) :** MD5 est victime de failles structurelles qui permettent de générer facilement des collisions (deux mots de passe différents qui produisent le même hash). Un attaquant pourrait donc contourner une authentification sans connaître le mot de passe d'origine. SHA-256 est, à ce jour, mathématiquement exempt de collisions applicables.
2. **Espace de recherche (Taille de l'empreinte) :** 
   - MD5 génère une empreinte de **128 bits** (chaîne de 32 caractères hexadécimaux).
   - SHA-256 génère une empreinte de **256 bits** (chaîne de 64 caractères hexadécimaux).
   L'espace des clés de SHA-256 est infiniment plus grand, ce qui rend les attaques par force brute impossibles avec les technologies actuelles.
3. **Vitesse de calcul :** MD5 est un algorithme conçu pour être très rapide. Paradoxalement, en cybersécurité, **la rapidité est un défaut pour le hachage de mots de passe**. Plus un algorithme est rapide, plus un attaquant peut tester de combinaisons par seconde (via des cartes graphiques/GPU). SHA-256 est plus complexe et donc plus lourd à calculer que MD5, ce qui ralentit les tentatives de cracking.

*Note : Pour une sécurité maximale en production, on préférera aujourd'hui des algorithmes encore plus lents et gourmands en mémoire comme Bcrypt, Argon2 ou PBKDF2.*