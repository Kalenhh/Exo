#coding:utf-8

from random import*
from time import sleep
import time

# Variables :______________________________________________________________________________________________________________

valeur = ""				#Input de l'utilisateur
nombre = 0				#Valeur randomisée par l'ordinateur
n = 0 					#Compteur à incrémenter

Lock = True				#Booléen Lock

t1 = 0 					#Variable temporelle de départ
t2 = 0 					#Variable temporelle de fin

ResponseTime = 0 		#Flottant sommes des délais de réponse de l'utilisateur
Score = 0 				#Entier  : Score = temps de réponse * le nombre de coup d'une partie : proche de 0 = bon score
Player = ""				#Nom de la sauvegarde du score

# Programme :____________________________________________________________________________________________________________________

print("Jeu du +/-")

while Lock == True :
	valeur = input("\nFaire une partie ? y/n/s :")

	if valeur == "n" :				#Quitter le jeu
		Lock = False
		continue

	if valeur == "y" :    #------------------------------------------------------------------------  Jeu \/
		
		print("Commence dans 3")
		time.sleep(1)
		print("Commence dans 2")
		time.sleep(1)
		print("Commence dans 1\n")
		time.sleep(1)

		n = 0
		nombre = randint(1,100)
		while n != 15 :

			t1 = time.time()
			valeur = input("Prosition de valeur : ")
			n = n+1
			t2 = time.time()
			ResponseTime = ResponseTime + t2-t1

			if valeur.isnumeric() == False :
				print("\nCa Doit être un nombre\n")
				continue

			valeur = int(valeur)

			if valeur == nombre :

				Score = int(round(ResponseTime * n,0))
				print("Gagné en ",n," tours !\nVotre score est de ",Score,"\n")
				Player = input("Enregistrez le score sous le nom : ")

				with open("game_score.txt","a") as file :
					file.write(Player+";"+str(Score)+"\n")
				n = 15

			if valeur <  nombre :
				print("Trop petit -----")

			if valeur > nombre :
				print("Trop grand ----------------------------------------------")

		if valeur != nombre :
			print("Nombre de tours dépassé !\nLa valeur recherchée était ",nombre,"\n")

		else :
			continue	

	if valeur == "s" :	#Afficher les best scores

		with open("game_score.txt","a") as verif :
			pass

		print("\nListe des meilleurs scores :\n")
		with open("game_score.txt","r") as file :
			res = file.readlines()    #liste des couples nom;score

			norm = ("Player;999999999999999999999999")
			for i in range(10) :
				best = norm

				if len(res) != 0 :
					for o in res :
						o = o.split("\n")[0]

						if int(o.split(";")[1]) < int(best.split(";")[1]) :							
							best = o
					
					res.remove(best+"\n")
					print(best)
					continue

				else :
					print(norm)				
	else :
		print("Entrez 'y' , 'n' ou 's'")