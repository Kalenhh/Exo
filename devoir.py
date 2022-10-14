#coding:utf-8

def moyenne(liste) :
	"""Retourne la moyenne des entiers de la liste"""
	if len(liste) == 0 :
		return "Erreur : Liste vide"	# Liste Vide

	somme = 0
	for i in liste :		# On parcourt la liste
		somme += i 
	return somme/len(liste)

print(moyenne([5,3,8]),moyenne([1,2,3,4,5,6,7,8,9,10]),moyenne([]))


def tri(tab) :
	"""On tri un tableau de 0 et de 1"""
	i = 0 			# Borne inférieur de la zone non triée
	j = len(tab)-1	# Borne supérieur de la zone non triée

	while i != j :			# Tant que la zone existe
		if tab[i] == 0 :	# On cherche le premier element de la zone
			i = i + 1 		# Si 0 alors la zone réduit

		else :
			valeur = tab[j]	# Sinon on remplace avec l'element de fin
			tab[j] = tab[i]
			tab[i] = valeur
			j = j-1
	return tab

print(tri([0,1,0,1,0,1,0,1,0]))	