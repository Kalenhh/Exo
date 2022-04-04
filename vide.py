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
	Verifie que le résultat de l'opération (a op b) est positif et entier
	"""

	assert op in ["+","-","*","/","**"]			# op est une opération compréhensible par Python
	assert type(a + b) == int 					# a et b sont des entiers

	Calcul = eval(str(a)+op+str(b))

	if est_entier(Calcul) == True and abs(Calcul) == Calcul : #Verifie que Calcul est entier + positif
		return True
	else:
		return False


def test():
	"""
	Fonction de test pour controler l'intégrité de verifier()
	"""
	paquet = [("-",8,7),("*",8,9),("**",4,8)]	# Jeu de test à effectuer
	for i in paquet :

		assert verifier(i[0],i[1],i[2]) == True

	assert verifier("/",4,3) == False

test()


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
	for i in table :
		
		if i > maxi :
			maxi = i


def minimum(table) :
	"""
	Retourne la valeur minimale de la liste table
	"""			

	assert len(table) > 0

	mini = table[0]
	for i in table :

		if i < mini :
			mini = i


def extremum(table) :
	"""
	Trouve les extremes dans une liste
	"""

	assert len(table) > 0

	return maximum(table) , minimum(table)


def moyenne(table) :
	"""
	Retourne la moyenne des valeurs de la liste table
	"""

	assert len(table) > 0

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
	"""
	Calcule la complexité d'une fonction
	fonction ; fonction en str avec le paramètre variable visé nommé "valeur"
	valeur_base ; valeur de base donné à valeur
	facteur ; valeur de multiplication de valeur_base pour faire une seconde itération (si complexité en O(n) , facteur est proche de résultat)
	n ; le nombre de test effectué pour affiner la moyenne retourné
	"""

	valeur = valeur_base
	temps_base = []
	temps_facteur = []

	for i in range(n) :					# Calcul de la complexité avec valeur_base
		t1 = time()
		eval(fonction)
		t2 = time()
		temps = t2 - t1

		temps_base.append(temps)

	valeur = valeur_base * facteur
	
	for i in range(n) :					# Calcul de la complexité avec valeur_base * facteur
		t1 = time()
		eval(fonction)
		t2 = time()
		temps = t2 - t1

		temps_facteur.append(temps)

	return moyenne(temps_facteur)/moyenne(temps_base)

fonction = "rechercher(creer_donnees(valeur,100),9)"

<<<<<<< Updated upstream
print(round(complexite(fonction,10000,5,20),2))
=======
print(round(complexite(fonction,1000000000,5,20),2))


>>>>>>> Stashed changes
