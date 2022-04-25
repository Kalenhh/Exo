#lm.py
#coding:utf-8

# Activité Algo de tri

from random import*
from time import*

donne = [o for o in range(1,14) for i in range(4)]

print("liste :",donne)
print(len(donne),"\n")

shuffle(donne)
print("liste désordonné :",donne,"\n")


# Tri par insertion

def tri_insert(liste) :

	for i in range(len(liste)) :
		j = 0

		while liste[i] > liste[j] :
			j = j+1

		liste.insert(j,liste[i])
		liste.pop(i+1)
	return liste

print("liste trié par insert :",tri_insert(donne),"\n")


def tri_select(liste) :

	for i in range(len(liste)-1) :
		minimum = liste[i]
		position = i

		for j in range(i,len(liste)) :
			if liste[j] < minimum :
				minimum = liste[j]
				position = j 

		liste.insert(i,minimum)
		liste.pop(position+1)
	return liste

donne = [o for o in range(1,14) for i in range(4)]
print("liste trié par selection :",tri_select(donne),"\n")


# Recherche par dichotomie

def recherche_dicho(liste,valeur) :

	inf = 0
	sup = len(liste)

	while sup-inf > 1 :
		milieu = (inf+sup)//2

		if liste[milieu] < valeur :
			inf = milieu
		else :
			sup = milieu

	if liste[inf] == valeur :
		position = inf 

	if liste[sup] == valeur :
		position = sup

	else :
		position = None

	return position

print("On cherche 8 dans la liste , position = ",recherche_dicho(donne,8),"\n")

def recherche_normal(liste,valeur) :

	for i in range(len(liste)) :
		if liste[i] == valeur :
			return i

# On teste l'efficacité de la recherche dichotomique

donne = [i for i in range(100**3*10)]

t1 = time()
recherche_dicho(donne,100**3)
t2 = time()
print(t1)
print(t2)

print("temps pour recherche_dicho :",t2-t1)

t1 = time()
recherche_normal(donne,100**3)
t2 = time()

print("temps pour recherche_normal :",t2-t1)
