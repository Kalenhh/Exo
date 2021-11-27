#coding:utf-8

#Activité 4

from random import*
from time import sleep
import time

# Variables :______________________________________________________________________________________________________________

valeur = ""					#Input de l'utilisateur
nombre = 0					#Valeur randomisée par l'ordinateur
n = 0 						#Compteur à incrémenter
	
Lock = True					#Booléen Lock

t1 = 0 						#Variable temporelle de départ
t2 = 0 						#Variable temporelle de fin

ResponseTime = 0 			#Flottant sommes des délais de réponse de l'utilisateur
Score = 0 					#Entier  : Score = temps de réponse * le nombre de coup d'une partie : proche de 0 = bon score
Player = ""					#Nom de la sauvegarde du score
directory="game_score.txt"	#Chemin du fichier de sauvegarde

# Programme :____________________________________________________________________________________________________________________

print("Jeu du +/-")

while Lock == True :		#Boucle principal
	valeur = input("\nFaire une partie ? y/n/s :")

	if valeur == "n" :				#Quitter le jeu
		Lock = False
		continue

	if valeur == "y" :    #------------------------------------------------------------------------  Jeu \/
		
		print("Commence dans 3")
		time.sleep(1)
		print("Commence dans 2")		#Compte à rebours de 3 secondes
		time.sleep(1)
		print("Commence dans 1\n")
		time.sleep(1)

		n = 0
		nombre = randint(1,100)
		while n != 15 :					#Nombre de tour limité à 15

			t1 = time.time()
			valeur = input("Prosition de valeur : ")
			n = n+1
			t2 = time.time()
			ResponseTime = ResponseTime + t2-t1    #Temps de réponse de l'utilisateur

			if valeur.isnumeric() == False :			#Verifie que l'entré soit valide : entier positif
				print("\nCa Doit être un nombre\n")
				continue

			valeur = int(valeur)

			if valeur == nombre :				#La valeur est trouvé

				Score = int(round(ResponseTime * n,0))		#Calcul du score
				print("Gagné en ",n," tours !\nVotre score est de ",Score,"\n")
				Player = input("Enregistrez le score sous le nom : ")

				with open(directory,"a") as file :				#Enregistrez le score
					file.write(Player+";"+str(Score)+"\n")
				n = 15

			if valeur <  nombre :
				print("Trop petit -----")

			if valeur > nombre :
				print("Trop grand ----------------------------------------------")

		if valeur != nombre :
			print("Nombre de tours dépassé !\nLa valeur recherchée était ",nombre,"\n")

		else :				#Fin de la boucle
			continue

	if valeur == "s" :	#Afficher les 10 meilleurs scores

		with open(directory,"x") as verif :  #Vérifie que le fichier existe ,sinon , le créer
			pass

		print("\nListe des meilleurs scores :\n")
		with open(directory,"r") as file :
			res = file.readlines()    #res = liste des couples nom;score;\n

			norm = ("Player;999999999999999999999999")  #Affichage par défaut
			for i in range(10) :
				best = norm 		#best = meilleur score de chaque parcours dans res

				if len(res) != 0 :  #Parcours tout les éléments de res et determine le couple au plus petit score
					for o in res :
						o = o.split("\n")[0]    #enleve le \n au couple

						if int(o.split(";")[1]) < int(best.split(";")[1]) :					#Compare le score 		
							best = o
					
					res.remove(best+"\n")  #Enleve le meilleur score de res 
					print(best)
					continue

				else :
					print(norm)				
	else :
		print("Entrez 'y' , 'n' ou 's'")