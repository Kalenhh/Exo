#lm.py
#coding:utf-8

# Activité Algo de tri

#Import
from random import*
from time import*
from copy import*


# Définition de la liste de valeurs servant à tester les algorithmes de tris :-------------------------------------------------------------

donne = [o for o in range(0,101)] # Liste de valeurs utilisés : 0 à 100

print("liste :",donne)
print(len(donne),"\n")

shuffle(donne)
print("liste désordonné :",donne,"\n")


# Tri par insertion :-------------------------------------------------------------------

def tri_insert(liste) :
	"""
	On prend chaque item et on l'insere juste apres la valeur plus petite que lui
	"""

	for i in range(len(liste)) : 	# i est l'index de l'item selectionné
		j = 0 						# j est l'index ou l'item sera inseré

		while liste[i] > liste[j] :		# Si la valeur à i est plus grande que la valeur à j 
			j = j+1 					# On incrémente j 

		liste.insert(j,liste[i])	# On insere la valeur i à l'index j
		liste.pop(i+1)				# On supprime la valeur i donc i+1
	return liste


# Tri par selection :------------------------------------------------------------------------

def tri_select(liste) :
	"""
	On prend la 1ère valeur puis on cherche le minimum dans le reste de la liste pour l'inserer à la suite puis on ré-itère.
	"""

	for i in range(len(liste)-1) : 	# i est l'index de l'item selectionné
		minimum = liste[i]
		position = i

		for j in range(i,len(liste)) :	# j est l'index des items comparé avec la valeur i 
			if liste[j] < minimum :		# On cherche la plus petite valeur
				minimum = liste[j]
				position = j 

		liste.insert(i,minimum)		# On insere la plus petite valeur trouvé à l'index i 
		liste.pop(position+1)		# On supprime la valeur i donc i+1
	return liste


# Recherche par dichotomie :------------------------------------------------------------------------

def recherche_dicho(liste,valeur) :
	"""
	La liste mise en argument doit forcement etre ordonné.
	On coupe la liste en deux , puis on enleve la partie ne contenant pas la valeur recherché , et on ré-itère jusqu'a avoir une seule valeur.
	"""

	inf = 0 			# Borne inférieure
	sup = len(liste) 	# Borne supérieure
 
	while sup-inf > 1 :			# Tant qu'il y a plus d'une valeur entre les deux bornes
		milieu = (inf+sup)//2 			# On determine le milieu des bornes
		if liste[milieu] < valeur :		# On compare la valeur milieu avec la valeur recherché , et on change la position des bornes en conséquences
			inf = milieu
		else :
			sup = milieu

	if liste[inf] == valeur :	# On compare les valeurs des bornes avec la valeur recherché
		position = int(inf)
	elif liste[sup] == valeur :
		position = int(sup)
	else :
		position = None			# None si la valeur n'est pas présente

	return position	

def recherche_normal(liste,valeur) :
	"""
	Recherche classique
	On parcourt toute la liste et si on trouve une occurence , on retourne la position
	"""

	for i in range(len(liste)) :
		if liste[i] == valeur :
			return i

def test_recherche() :
	"""
	On test l'efficacité de la recherche dichotomique par rapport à la recherche normal
	"""

	donne = [i for i in range(100**3*10)]

	t1 = time()
	recherche_dicho(donne,100**3)
	t2 = time()

	print("temps pour recherche_dicho :",t2-t1)

	t1 = time()
	recherche_normal(donne,100**3)
	t2 = time()

	print("temps pour recherche_normal :",t2-t1)


# Test :---------------------------------------------------------------------------------------------------------------

def test() :
	"""
	On test les fonctions avec des assertions
	"""

	liste = [o for o in range(11)]		# Liste de valeur de 0 à 100

	liste_s = deepcopy(liste)
	shuffle(liste_s)
	liste_insert = tri_insert(liste_s)	# Liste trié par insertion
	liste_select = tri_select(liste_s)	# Liste trié par selection

	for i in range(len(liste)) :
		assert liste_insert[i] == i 		# Si chaque valeur est égale à son index (donc trié sans erreur)
		assert liste_select[i] == i

		assert recherche_normal(liste,i) == i 	
		assert recherche_dicho(liste,i) == i
test()


# :------------------------------------------------------------------------------------------------------------------

print("liste trié par insert :",tri_insert(deepcopy(donne)),"\n")

print("liste trié par selection :",tri_select(deepcopy(donne)),"\n")

print("On cherche 8 par dichotomie dans la liste , position = ",recherche_dicho(tri_insert(donne),8),"\n")

test_recherche()
