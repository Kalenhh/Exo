#coding:utf-8
# Exo 4 (type Bac)

def destockage(A) :

	fin = []
	for i in range(len(A)) :
		if i %3 == 0 and (i+3) <= len(A) :  # On verifie que l'on peut faire des groupe de 3 et qui i est un multiple de 3
			mini = A[i] 

			for o in A[i:i+3] :

				if o < mini : # Le minimum du trio
					mini = o

				fin.append(o)
			fin.remove(mini)
		
		elif i %3 == 0 and (i+3) > len(A) : # Si il reste 2 ou 1 element
			fin.append(A[i])

	return fin

# Pour avoir le meilleur prix -> avoir des trio haut et trio bas -> trier par valeur -> rangement


def trier(liste) :
	# Tri par insertion

	for i in range(len(liste)) : 	# i : index de debut
		inser = 0 					# inser : index ou l'on insere l'element d'index i

		while liste[i] > liste[inser] :
			inser = inser+1

		liste.insert(inser,liste[i])
		liste.pop(i+1)

	liste.reverse() # On transforme la liste en decroissante pour mettre les produits cher en premier
	return liste

from copy import deepcopy

Liste = [5,6,52,1,5,654,65]
print(f"Liste:{Liste} , longueur :{len(Liste)}")
print("Prix sans tri :",sum(destockage(deepcopy(Liste))))
print("Prix avec tri :",sum(destockage(trier(deepcopy(Liste)))))


