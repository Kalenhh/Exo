#vide.py

from random import*
from time import*

#----------------------------------------------------------------------------------------------------------------------------
# Activité 10 : Assertion et prototypage


def est_entier(n):
	if abs(n-int(n))>0.5:	# cas si n=x.99999999
		decimal=abs(n-int(n+1))*100000	# partie decimal
	else:					# cas si n=x.000000001
		decimal=abs(n-int(n))*100000	# partie decimal
	if decimal<1:
		return True
	else:
		return False


def verifier(op,a,b) :
	"""
	Verifie que le résultat de l'opération est positif et entier
	"""

	assert op in ["+","-","*","/","**"]
	assert type(a + b) == int

	Calcul = eval(str(a)+op+str(b))

	if est_entier(Calcul) == True and abs(Calcul) == Calcul : #Verifie que Calcul est entier + positif
		return True
	else:
		return False


def test():
	"""
	Fonction de test pour verifier()
	"""
	paquet = [("-",8,7),("*",8,9),("**",-4,9)]
	for i in paquet :

		assert verifier(i[0],i[1],i[2]) == True
	assert verifier("/",4,3) == False



#------------------------------------------------------------------------------------------------------------------------
# Activité 11 : Parcours sequentiel de tableau de valeurs


def rechercher(table,valeur) :
	"""
	Trouve les occurences d'une valeur dans une liste
	"""

	assert len(table) > 0

	position = []

	for i in range(len(table)) :
		if valeur == table[i] :
			position.append(i)
	return position


def maximum(table) :
	"""
	Retourne la valeur maximale dans la liste table
	"""

	assert len(table) > 0

	maxi = table[0]
	for i in range(len(table)) :
		
		if table[i] > maxi :
			maxi = table[i]


def minimum(table) :
	"""
	Retourne la valeur minimale de la liste table
	"""			

	assert len(table) > 0

	mini = table[0]
	for i in range(len(table)) :

		if table[i] < mini :
			mini = table[i]


def extremum(table) :
	"""
	Trouve les extremes dans une liste
	"""

	assert len(liste) > 0

	return maximum(table) , minimum(table)


def moyenne(table) :
	"""
	Retourne la moyenne des valeurs de la liste table
	"""

	moyenne = 0

	for i in table :
		moyenne = moyenne + i

	moyenne = moyenne / len(table)
	return moyenne	


#----------------------------------------------------------------------------------------------------------------------------

def creer_donnees(n,max):
	"""
	Créer une liste de taille n de valeur aléatoire entre 1 et max
	"""

	donnees=[]
	for i in range(n):
		donnees.append(randint(1,max))	# choix aleatoire entier entre 1 et max
	return donnees


def complexite(fonction,valeur_base,facteur,n) :

	valeur = valeur_base
	temps_base = []
	temps_facteur = []

	for i in range(n) :
		t1 = time()
		eval(fonction)
		t2 = time()
		temps = t2 - t1

		temps_base.append(temps)

	valeur = valeur_base * facteur
	
	for i in range(n) :
		t1 = time()
		eval(fonction)
		t2 = time()
		temps = t2 - t1

		temps_facteur.append(temps)

	return moyenne(temps_facteur)/moyenne(temps_base)

print(round(complexite("rechercher(creer_donnees(valeur,100),9)",10000,2,10),2))