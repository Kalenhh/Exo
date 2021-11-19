#coding:utf-8

from random import*
from time import*

# Variables :______________________________________________________________________________________________________________

valeur = ""
nombre = 0
n = 0
Lock = True

# Prog :____________________________________________________________________________________________________________________

print("Jeu du +/-\n")
while Lock == True :
	valeur = input("Faire une partie ? y/n :")

	if valeur == "n" :
		Lock = False
		continue

	if valeur == "y" :
		
		n = 0
		nombre = randint(1,100)
		while n != 15 :
			valeur = input("Prosition de valeur : ")
			n = n+1

			valeur = int(valeur)
			if valeur == nombre :
				print("Gagné en ",n," tours !\n")
				n = 15

			if valeur <  nombre :
				print("Trop petit")

			if valeur > nombre :
				print("Trop grand")

		if valeur != nombre :
			print("Nombre de tours dépassé !\nLa valeur recherchée était ",nombre?"\n")

	else :
		print("Entrez 'y' ou 'n'")		