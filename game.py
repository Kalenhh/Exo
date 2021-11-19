#coding:utf-8

from random import*
from time import*

# Variables :______________________________________________________________________________________________________________

valeur = ""
nombre = 0
n = 0
Lock = True
t1 = 0
t2 = 0
ResponseTime = 0
Score = 0
Player = ""


# Prog :____________________________________________________________________________________________________________________

print("Jeu du +/-\n")
while Lock == True :
	valeur = input("\nFaire une partie ? y/n/h :")

	if valeur == "n" :
		Lock = False
		continue

	if valeur == "y" :    #------------------------------------------------------------------------  Jeu \/
		
		n = 0
		nombre = randint(1,100)
		while n != 15 :

			t1 = time()
			valeur = input("Prosition de valeur : ")
			n = n+1
			t2 = time()

			ResponseTime = ResponseTime + t2-t1


			valeur = int(valeur)
			if valeur == nombre :
				Score = round(ResponseTime * n,1)
				print("Gagné en ",n," tours !\nVotre score est de ",Score)
				Player = input("Enregistrez le score sous le nom : ")
				with open("game_log.txt","a") as file :
					file.write(Player+";"+str(Score))
				n = 15

			if valeur <  nombre :
				print("Trop petit")

			if valeur > nombre :
				print("Trop grand")

		if valeur != nombre :
			print("Nombre de tours dépassé !\nLa valeur recherchée était ",nombre,"\n")  #-------------------------------

	if valeur == "h" :
		#Afficher les best scores		
		with open("game_log.txt","r") as file :
			best = 100000000000000000000
			file = file.read()
			file = file.split("\n")
			while 10 :
				for i in file :
					i = i.split(";")
					if float(i[1]) < best :
						best = i
						file.remove(i)
				print(best)
			
	else :
		print("Entrez 'y' ou 'n'")		