#lm.py
from copy import*











def tri(t) :
	for i in range(len(t)-1) :
		if t[i] + 1 != t[i+1] :
			return False

	return True


liste = [16 for o in range(10)]

print(liste)
print(tri(liste))



def rendu_monnaie(piece,somme) :
	"""
	piece = liste des pieces dispo pour le rendu en euro
	somme = valeur a rendre
	"""

	rendu = [] 		# liste des pieces qui seront rendu

	while somme > 0 :

		for i in piece :
			if i <= somme :
				rep = i

		rendu.append(rep)

		somme = somme - rep
		somme = round(somme,2)

	return rendu

liste = [i for i in [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20] for o in range(10)]

print("\nListe des pièces disponibles :",liste)
print("pièces rendu pour 2.46 :",rendu_monnaie(liste,2.46),"\n")


def sacados(objets,poids_max) :
	"""
	liste = liste des liste ordonné par valeur DECROISSANT
	poids_max = maximum du sac
	"""

	liste = deepcopy(objets)
	sac = [] # liste des liste dans le sac
	poids = 0 # poids du sac avec les liste

	ratio = 0
	while poids <= poids_max and len(liste) > 0:

		ratio=-0.1
		for i in range(len(liste)) :

			if liste[i][3] > ratio and poids + liste[i][1] < poids_max :
				rep = liste[i]
				index = i
				ratio = rep[3]

		poids = poids + rep[1]
		liste.remove(liste[index])
		sac.append(rep)
		print(liste)

	sac.pop(rep)
	return sac , poids

nom = ["montre","ordi","smartphone","appareil","imprimante","tablette","agenda","livres","cahiers","outils","lampe","gps"]
poids = [53,1900,220,1500,5800,480,220,2200,780,3450,570,154]
valeur = [150,949,399,1250,125,89,4,53,5.6,245,23,129]

liste = [[nom[i],poids[i],valeur[i],round(valeur[i]/poids[i],1)] for i in range(len(nom))]

print("Liste des objets dispo :",liste)
print("1er element = le nom de l objet et 2eme element = poids 3eme = valeur , 4eme = ratio")
print("objets pris :",sacados(liste,4000),"\n")


