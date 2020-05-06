#!/usr/bin/env python  
# --*-- coding: UTF-8 --*--  

from ftplib import FTP
from getpass import getpass

domain =input("Quel est le nom de domaine du serveur FTP ? :")

# on démarre une connexion ftp à la machine "debian02" en créant une instance ftp
ftp=FTP(domain)				

user = input("Username:")
#mdp = input("Password:")
mdp = getpass()
# authentification au serveur ftp avec un login et mot de passe
ftp.login(user=user, passwd=mdp, acct='')

# renvoie le message de bienvenue du serveur ftp
ftp.getwelcome()	 

while 1:
    print("Voici les différentes options : \n 0 : Changer de répertoire \n 1 : Afficher le répertoire courant \n 2 : Lister les fichiers du répertoire \n 3 : Créer un répertoire \n 4 : Supprimer un fichier \n 5 : Supprimer un dossier \n 6 : Renommer un fichier \n 7 : Transférer un fichier \n 8 : Déplacer un fichier \n 9 : Quitter")
    choix = int(input("Quel choix faites vous ?\n "))

    if choix == 0:
        # change de repertoire
        repertoire = input("Dans quel répertoire voulez vous aller ?: ")
        ftp.cwd(repertoire)
        print("\n")
    elif choix == 1:
        print(ftp.pwd())
        print("\n")
    elif choix == 2: 
        ftp.retrlines('LIST', callback=None) 
    elif choix == 3:
        nom_rep = input(print("Nommer le répertoire à créer (rép courant): "))
        ftp.mkd(nom_rep)
    elif choix == 4:
        nom_fic = input(print("Indiquer le nom du fichier à supprimer: "))
        ftp.delete(nom_fic)
    elif choix == 5:
        # supprime le repertoire
        nom_dos = input(print("Indiquer le répertoire à supprimer : "))
        ftp.rmd(nom_dos)
    elif choix == 6:
        # renome le fichier
        name = input(print("Indiquer le nom du fichier à renommer : "))
        new_name = input(print("Indiquer le nouveau nom : "))
        ftp.rename(name, new_name)
    elif choix == 7:
        # Envoie un fichier
        nom_fic = input(print("Entrer le nom du fichier à transférer : "))
        ftp.storlines('STOR', nom_fic)
    elif choix == 8:
        nom_fic = input(print("Indiquer le fichier à déplacer : "))
        dest_fic = input(print("Indiquer l'emplacement : "))
        ftp.rename(nom_fic, dest_fic)
    elif choix == 9:
        break

ftp.quit()