#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Activité 11 : création d'un tableau de données (entiers).

from random import*                                                           #Importation de la bibliothèque random.
from time import*                                                       #Importation de la bibliothèque time.

#Fonction de génération d'un tableau de n entiers compris entre 1 et max.

def creer_donnees(n,max):                                               #Definition de la fonction creer_donnees de n à max.
    donnees=[]                                                          #Liste des données.
    for i in range(n):                                                  #Pour i in range n.
        donnees.append(random.randint(1,max))                           #Choix aleatoire entier entre 1 et max.
    return donnees                                                      #Retourne les données.

def rechercher(table,valeur) :                                           #Definition de la fonction occurence table valeur, trouve la valeur dans la table et la retourne.
    assert len(table) > 0                                               #Entiers au dessus de 0 dans la table.
    position = []                                                       #Position vide.
    for i in range(len(table)) :                                        #Pour i in range dans la table.
        if valeur == table[i] :                                         #Si valeur comparée à table i.
            position.append(i)                                          #Position sur i.
    return position                                                     #Retourner la position.

def maximum(table) :                                                    #Definition de la fonction maximum table, retourne la valeur max dans la liste.
    """
    Renvoi alors la valeur max dans la liste.
    """
    assert len(table) > 0                                               #Entiers au dessus de 0 dans la table.
    maxi = table[0]                                                     #Maxi dans la table 0.
    for i in table :                                                    #Pour i dans la table.
        if i > maxi :                                                   #Si i est au dessus de maxi.
            maxi = i                                                    #Maxi est égale à i.

def minimum(table) :                                                    #Definition de la fonction minimum table, retourne la valeur mini dans la liste.
    """
    Renvoi alors la valeur mini de la liste.
    """
    assert len(table) > 0                                               #Entiers au dessus de 0 dans la table.
    mini = table[0]                                                     #Mini dans la table 0.
    for i in table :                                                    #Pour i dans la table.
        if i < mini :                                                   #Si i est plus petit que mini.
            mini = i                                                    #Mini est égale à i.

def extremum(table) :                                                   #Definition de la fonction extremum table, retourne la valeur max et la valeur mini dans la liste.
    """
    Cherche les extremes dans la liste.
    """
    assert len(table) > 0                                               #Entiers au dessus de 0 dans la table.
    return maximum(table) , minimum(table)                              #Retourne le max de la table, et le mini de la table, soit les extremum.


def moyenne(table) :                                                    #Definition de la fonction moyenne table, retourne la valeur moyenne, non pondérée, des valeurs contenues dans la liste table.
    """
    Renvoi alors la moyenne des valeurs de la liste.
    """
    assert len(table) > 0                                               #Entiers au dessus de 0 dans la table.
    moyenne = 0                                                         #Moyenne égale 0.
    for i in table :                                                    #Pour i dans la table.
        moyenne = moyenne + i                                           #Moyenne égale à moyenne + i.
    moyenne = moyenne / len(table)                                      #Moyenne égale ) moyenne divisée par len table.
    return moyenne                                                      #Retourne la moyenne de la table.

def creer_donnees(n,max):                                               #Def de la fonction creer_donnees qui produit une liste de taille n, avec une valeur random entre 1 et max.
    """
    Produit une liste de taille n, de valeur aléatoire, et entre 1 et max.
    """
    donnees=[]                                                          #Donnees vides.
    for i in range(n):                                                  #Pour i dans range n.
        donnees.append(randint(1,max))                                  #Choix aleatoire entier entre 1 et max.
    return donnees                                                      #Retourne données.

def complexite(fonction,facteur) :                                      #Definition de fonction complexite, mesure la complexité d'un algorithme.
    """
    Calcule alors la complexite de fonction.
    """
    valeur = 10000                                                      #Valeur égale à 10000.
    tempsclassique = 0                                                  #Tempsclassique à 0.
    tempsfacteur = 0                                                    #Tempsfacteur à 0.
    t1 = time()                                                         #t1 égale à time.
    eval(fonction)                                                      #eval de fonction.
    t2 = time()                                                         #t2 égale à time.
    tempsclassique = t2 - t1                                            #Tempsclassique égale à t2 moins t1.
    valeur = valeur * facteur                                           #Valeur égale valeur fois facteur.
    t1 = time()                                                         #t1 égale à time.
    eval(fonction)                                                      #Eval de fonction.
    t2 = time()                                                         #t2 égale à time.
    tempsfacteur = t2 - t1                                              #Tempsfacteur égale à t2 moins t1.
    return tempsfacteur / tempsclassique                                #Retourne Tempsfacteur divisé par Tempsclassique.

print(complexite("rechercher(creer_donnees(valeur,100),50)",2))  