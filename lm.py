#lm.py


"""

def tri(t) :
	for i in range(len(t)-1) :
		if t[i] + 1 != t[i+1] :
			return False

	return True


liste = [16 for o in range(10)]

print(liste)
print(tri(liste))

"""

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
	objets = liste des objets ordonné par valeur DECROISSANT
	poids_max = maximum du sac
	"""

	sac = [] # liste des objets dans le sac
	poids = 0 # poids du sac avec les objets

	for i in range(len(objets)) :
		if objets[i][1] + poids <= poids_max :
			sac.append(objets[i][0])
			poids = poids + objets[i][1]

	return sac
	
liste = [(i,[2,7,5,9,5,4,2,1,9,8,6,5,4,3][i]) for i in range(10)]

print("Liste des objets dispo :",liste)
print("1er element = le nom de l objet et 2eme element = poids , liste trié par ratio valeur/poids decroissant")
print("Objets pris :",sacados(liste,20),"\n")



