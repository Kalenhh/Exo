#coding:utf-8
# Activité Tri fusion

# Fonctions donné ---------------------------------------------------------------------

from random import *
from time import *

#############
# fonctions #
#############

# fonction de génération d'un tableau de n entiers compris entre 1 et max
def creer_table(n,max=100):
	"""
	crée une liste de n entiers choisis aléatoirement
	compris entre 1 et max (100 par défaut)
	retourne la liste créée
	"""
	table = []
	for i in range(n):
		table.append(randint(1,max))	# choix aleatoire entier entre 1 et max
	return table

# test de complexité
def complexite(fonction,facteur=2):
	"""
	teste la complexité d'un algorithme inclus dans une fonction
	prend en paramètres le nom de la fonction, et le facteur souhaité sur la quantité de données
	renvoie le rapport du temps d'exécution entre une liste de 1000 valeurs
	et une liste de 1000xfacteur données
	renvoie None si la fonction ne se prete pas au test
	"""
	donnees0=[1,2,3,4]	# pour tester la validité du test
	donnees1=creer_table(1000,100)
	donnees2=creer_table(1000*facteur,100)
	# test si fonction valide
	try:
		eval(fonction+"(donnees0)")
	except:
		return None	# retourne None en cas d'erreur
	# test complexité
	n=10	# nombre de tests
	somme=0	# pour calculer moyenne des tests
	for i in range(n):	# test avec 1000 valeurs
		t1=time()
		eval(fonction+"(donnees1)")
		t2=time()
		dt1=t2-t1
		somme=somme+dt1
	dt1=somme/n	# calcul moyenne
	somme=0
	for i in range(n):	# test avec 1000xfacteur valeurs
		t1=time()
		eval(fonction+"(donnees2)")
		t2=time()
		dt2=t2-t1
		somme=somme+dt2
	dt2=somme/n	# calcul moyenne
	return dt2/dt1


# --------------------------------------------------------------------------------


def est_trie(tab) :
	"""
	Vérifie si un tableau est trié
	renvoie True si triée , False sinon

	tab : liste
	"""
	for i in range(len(tab)-1) :
		if tab[i] > tab[i+1] :
			return False
	return True

# Assertions
assert est_trie([1,2,3,4,5,6,7]) == True
assert est_trie([4,5,6,9,8,7,6,5,3,4,5,6]) == False



def fusion(tab1,tab2) :
	"""
	Fusionne 2 tableaux triés

	tab1 : liste
	tab2 : liste
	"""

	tab = []

	n1 = len(tab1)-1
	n2 = len(tab2)-1

	i1 = 0 
	i2 = 0 

	while i1 <= n1 or i2 <= n2 :

		if i1<=n1 and i2<=n2 :
			if tab1[i1]<tab2[i2] :
				tab.append(tab1[i1])
				i1 = i1 + 1

			else :
				tab.append(tab2[i2])
				i2 = i2 + 1

		if i1 == n1+1 and i2<=n2 :
			tab.append(tab2[i2])
			i2 = i2 + 1

		if i2 == n2+1 and i1<=n1 :
			tab.append(tab1[i1])
			i1 = i1 + 1

	return tab



def tri_fusion(tab) :
	"""
	Implémente le tri fusion
	-> 	Coupe le tableaux en deux jusqu'à ce que chaque tableau recoupé 
		soit de longueur 1 donc trié ,puis fusionne les tableaux jusqu'à retrouver
		un tableau entier trié

	tab : liste
	"""

	n = len(tab)

	if n <= 1 :
		return tab

	else :
		mid = int(round(n/2,0))

		left = tri_fusion(tab[0:mid])
		right = tri_fusion(tab[mid:n+1])
		return fusion(left,right)

# Assertion
assert est_trie(tri_fusion(creer_table(100))) == True



# Complexité
import matplotlib.pyplot as plt # Représentation graphique

comp = [] # Liste des valeurs donné par complexite()
for i in range(1,21) :
	comp.append(round(		complexite("tri_fusion",i)		,3))
	print("test ",i,"/",20)


norm = [i for i in range(1,21)] # Suite de 1 en 1 : [1,2,3,...,19,20]

fig , ax = plt.subplots()

ax.plot(norm,comp,label="fonction")
ax.plot(norm,norm,label="O(n)")
ax.plot(norm,[i**2 for i in range(1,21)],label="O(n²)")

ax.legend()
plt.show()