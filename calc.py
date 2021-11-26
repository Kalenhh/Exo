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

while Lock == True :
	Valeur = input("\nFaire une partie ? y/n :")

	if Valeur == "n" :
		Lock = False
		continue

	if Valeur == "y" :
		Score = 0
		for i in range(10) :
			Calcul = str(randint(0,10)) + Calcul_component[randint(0,2)] + str(randint(1,10))
			print(Calcul)
			Calcul = eval(Calcul)

			T1 = time()
			Valeur = input("=")
			T2 = time() - T1

			if Valeur.isnumeric() == False :
				print("Entrez une valeur numérique !")
				continue

			if int(Valeur) == Calcul :
				print("Exact !")

				if T2 <= 3 :
					Score = Score + 3
				if T2 > 3 and T2 <= 5 :
					Score = Score + 2
				if T2 > 5 :
					Score = Score + 1

				continue

			else :
				print("Faux , la réponse était",Calcul)				
		print("Votre score est de :",Score)		

	else :
		print("Entrez 'y' pour oui ou 'n' pour non")	