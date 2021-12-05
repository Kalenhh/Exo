#!/usr/bin/env python
# -- coding: utf-8 --

from random import*
from math import*

#Variables.

Lock = True                                                             # Booléen qui est Lock.
Valeur = ""                                                             #Valeur choisit par l'utilisateur.
Calcul_component = ["+","-","*"]										#Composants de calcul soit l'addition, la soustraction et la multiplication.

#Début.

#Programme.

while Lock == True :                                                    #Boucle générale.
    Valeur = input("\nVoulez-vous faire une partie ? O/N : ")			#Demande à l'utilisateur si il veut faire une partie ou non. (O = Oui, N = Non)

    if Valeur == "N" :                                                	#Quitter alors le jeu.
        Lock = False
        continue

    if Valeur == "O" :                                                	#Lancer alors le jeu.
        Score = 0														#Le score est donc de 0 pour le moment car l'utilisateur n'a pas encore joué.
        for i in range(10) :                                            #Boucle de 10 questions.
            Calcul = str(randint(0,10)) + Calcul_component[randint(0,2)] + str(randint(1,10))    #Définition du calcul mental et son format soit (entier entre 0 et 10) + ( ou + ou -) + (entier entre 0 et 10) dans l'ordre respectif.
            print(Calcul)
            Calcul = eval(Calcul)

            Valeur = input()
            if int(Valeur) == Calcul :                                  #Comparation entre la valeur donnée et le résultat voulu.
                print("Le compte est bon.")
                continue                                                #Continuer le programme.

            else :                                                      #Si le résultat est faux alors :
                print("Réponse érronée, le résultat attendu était",Calcul)   #Réponse érronée.

        print("Votre score est de :",Score)                             #Le jeu est terminé, fin de la série des questions.

    else :
        print("Entrez 'O' pour oui ou 'N' pour non")