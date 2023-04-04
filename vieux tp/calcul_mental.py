#coding:utf-8

#Activité 5 : Calcul Mental

from random import*
from time import time

# Variable :----------------------------------

Valeur = ""
Calcul = ""
Calcul_component = ["*","-","+"]

Lock = True

Score = 0

T1 = 0
T2 = 0

# Programme :--------------------------------

while Lock == True :   #Boucle principal
	Valeur = input("\nFaire une partie ? y/n :")

	if Valeur == "n" :		#Quitter le jeu
		Lock = False
		continue

	if Valeur == "y" :		#Lancer une série de questions
		Score = 0
		for i in range(10) :		#Boucle de 10 fois 1 question
			Calcul = str(randint(0,10)) + Calcul_component[randint(0,2)] + str(randint(1,10))	#Défini le calcul mental , format : (entier entre 0 et 10) + (* ou + ou -) + (entier entre 0 et 10)
			print(Calcul)
			Calcul = eval(Calcul)

			T1 = time()			
			Valeur = input("=")
			T2 = time() - T1			#Temps de réponse de l'utilisateur

			if Valeur[0] == "-" :			#----------------------------------
				if Valeur[1:].isdigit() == False  :
					print("Entrez une valeur numérique!")
					continue											#Vérifie que l'utilisateur a entrer une valeur valide : entier positif/négatif 
			if Valeur[0] != "-" :	
				if Valeur.isdigit() == False  :
						print("Entrez une valeur numérique !")
						continue	  	#------------------------------------

			if int(Valeur) == Calcul :  #Compare la valeur donné avec le résultat attendu
				print("Exact !")

				if T2 <= 3 :
					Score = Score + 3
				if T2 > 3 and T2 <= 5 :
					Score = Score + 2		#Assigne le score obtenu à la question
				if T2 > 5 :
					Score = Score + 1

				continue

			else :
				print("Faux , la réponse était",Calcul)	#Si la réponse n'est pas égale à la réponse attendu
				Score = Score - 1

		print("Votre score est de :",Score)		#Fin de la série de question

	else :
		print("Entrez 'y' pour oui ou 'n' pour non")	