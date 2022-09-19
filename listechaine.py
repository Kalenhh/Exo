#coding:utf-8
# Liste chainée	

def longueur(chain) :
	# Retourne la longueur de la liste chainée 'chain'

	if chain == [] :	# Liste vide
		return "Empty List E0"

	longueur = 0
	while chain != None and chain[0] is not None : 	# Incrémente tant que chain est une 
		longueur += 1 								# liste de la forme [valeur,liste]
		chain = chain[1]

	return longueur


def acceder(chain,i) :
	# Retourne la valeur à l'index i dans la liste chainée 'chain'

	if chain == [] :	# Liste vide
		return "Empty List E1"

	if i >= longueur(chain):	# Index trop grand
		return "Index I1"	

	for o in range(i) :		# On cherche la valeur d'index i
		chain = chain[1]

	return chain[0]


def ajouter(chain,element) :
	# Ajoute 'element' à la fin de la liste chainée 'chain'

	if chain == [] :	# Liste vide
		print("Empty list E2")
		return

	seg = chain
	if chain[0] is None :		# Si chain est chainée et vide [None,None]
		seg[:] = [element,None]
		return
	
	while seg[1] is not None :	# On parcourt la liste jusqu'à la fin
		seg = seg[1]

	seg[:] = [seg[0],[element,None]]


def inserer(chain,i,element) :
	# Insérer 'element' à l'index i dans la liste chainée 'chain'

	if longueur(chain) <= i :	# l'index est trop grand
		return "Index I3"

	seg = chain
	for o in range(i) :			# On parcourt jusque l'index i
		seg=seg[1]

	seg[:] = [element,[seg[0],seg[1]]]  # on insère 'element'


def supprimer_val(chain,element) :
	# Supprimer la premiere occurence de 'element' dans la liste chainée 'chain'

	if chain == [] :		# liste vide
		print("Empty List E4")

	seg = chain
	while seg[0]!= element : # On parcourt jusque 'element'
		seg = seg[1]

		if seg[1][1] is None and seg[0] != element and seg[1][0] == element :  # Si element est le dernier element de la chaine
			seg[1] = None
			return

		if seg is None :			# Si 'element' n'est pas present dans la liste
			print("Element non present P4")
			return

	seg[:] = seg[1]		# On supprimer 'element' et on raccorde la liste chainée


def supprimer_ind(chain,i) :
	# Supprimer l'element d'index i dans la liste chainée 'chain'

	if chain == [] :		# liste vide
		print("Empty List E5")
		return

	if longueur(chain) <= i :	# L'index est trop grand
		print("Index I5")
		return

	seg = chain
	for o in range(i) :
		
		if seg[1][1] is None : # Si l'index i designe le dernier element de la liste chainée
			seg[1] = None
			return

		seg = seg[1]

	seg[:] = seg[1]


def modifier(chain,i,element) :
	# Modifier la valeur de l'element a l'index i par 'element' dans la liste chainée 'chain'

	if chain == [] :		 # Liste vide
		print("Empty Liste E6")

	if longueur(chain) <= i :	# L'index est trop grand
		print("Index I6")
		return

	seg = chain
	for i in range(i) : # On parcourt 'chain' jusqu'a l'index i
		seg=seg[1]

	seg[0:] = [element,seg[1]] # On change la valeur de l'element d'index i


def vider(A) : 
	# Reinitialiser la liste chainée
	A[:] = [None,None]
	return

def verif(show=False) :
	A = [1,[2,[3,[4,None]]]]
	assert longueur(A) == 4
	assert acceder(A,0) == 1
	assert acceder(A,longueur(A)-1) == 4
	assert ajouter(A,'ajout') == None
	assert A == [1,[2,[3,[4,['ajout',None]]]]]
	assert inserer(A,0,"inser0") == None
	assert A == ['inser0',[1,[2,[3,[4,['ajout',None]]]]]]
	assert supprimer_val(A,'inser0') == None
	assert A == [1,[2,[3,[4,['ajout',None]]]]]
	assert supprimer_ind(A,4) == None
	assert A == [1,[2,[3,[4,None]]]]
	assert modifier(A,0,7) == None
	assert A == [7,[2,[3,[4,None]]]]
	assert vider(A) == None
	assert A == [None,None]

	if show is True :				# Verification visuelle
		A = [14,[12,[9,None]]]
		B = [None,None]				# Liste 
		C = [3,None]

		print(f"longueur : \t{longueur(A)}\t{longueur(B)}\t{longueur(C)}")

		print(f"access\t{acceder(A,0)}\t{acceder(B,0)}\t{acceder(C,0)}")
		print(f"access\t{acceder(A,1)}\t{acceder(B,1)}\t{acceder(C,1)}")
		print(f"access\t{acceder(A,2)}\t{acceder(B,2)}\t{acceder(C,2)}")

		print(f"Liste :\t{A}\t{B}\t{C}")

		print("\nFonction ajouter :")
		ajouter(A,"ajouter")
		ajouter(B,"ajouter")
		ajouter(C,"ajouter")
		ajouter(A,"ajouter1")
		ajouter(B,"ajouter1")
		ajouter(C,"ajouter1")

		print(f"Liste :\n{A}\n{B}\n{C}")

		print("\nFonction inserer :")
		inserer(A,0,"inser0")
		inserer(B,0,"inser0")
		inserer(C,0,"inser0")
		inserer(A,2,"inser2")
		inserer(B,2,"inser2")
		inserer(C,2,"inser2")
		inserer(A,4,"inser4")
		inserer(B,4,"inser4")
		inserer(C,4,"inser4")

		print(f"Liste :\n{A}\n{B}\n{C}")

		print("\nFonction supprimer_val :")
		supprimer_val(A,"inser0")
		supprimer_val(B,"inser0")
		supprimer_val(C,"inser0")
		supprimer_val(A,"ajouter1")
		supprimer_val(B,"ajouter1")
		supprimer_val(C,"ajouter1")

		print(f"Liste :\n{A}\n{B}\n{C}")

		print("\nFonction supprimer_ind : ")
		supprimer_ind(A,3)
		supprimer_ind(B,3)
		supprimer_ind(C,3)

		print(f"Liste :\n{A}\n{B}\n{C}")

		print("\nFonction modifier : ")
		modifier(A,0,"modif")
		modifier(B,1,"modif")
		modifier(C,2,"modif")

		print(f"Liste :\n{A}\n{B}\n{C}")

		print("\nFonction vider : ")
		vider(A)
		vider(B)
		vider(C)
		print(f"Liste :\n{A}\n{B}\n{C}")

verif(True)
	

"""

from random import*
cara = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g",
		"h","j","k","l","m","w","x","c","v","b","n"]
def rec() :
	global cara
	print( 	cara[randint(0,len(cara))]   )
	rec()


def fonction(n) :
	u = 2

	for i in range(n) :
		u = 0.5*u+3

	return u

print(f"f(1) : {fonction(1)}\tf(2) : {fonction(2)}")

def somme(n) :
	u = 2
	s = 0

	for i in range(n+1) :
		s += u
		u = 0.5*u+3

	return s	

print(f"s(1) : {somme(1)}\ts(2) : {somme(2)}")

def cal(n,o,r,c) :
	# n = rang
	# o = U0
	# r = raison
	# c = constante

	u = o

	for i in range(n) :
		u = u*r+c

	return u

print(cal(20,3,0.1,-1))

def somme(n,o,r,c) :
	t = 0

	for i in range(n) :
		t += cal(i,o,r,c)

	return t	

print(somme(10,0.5,2,2))

def somme_borne(n1,n2,o,r,c) :
	s1 = somme(n1,o,r,c)
	s2 = somme(n2,o,r,c)

	return s2 - s1

print(somme_borne(12,20,3,0.4,1))

def deter(e,o,r,c) :
	# e = element a rechercher

	u = 0
	n = 0
	while u <= e :

		u = cal(n,o,r,c)
		n += 1 

	return n-1,u

print(deter(50,1,1.1,2),cal(13,1,1.1,2))

for i in range(50) :
	print(i)


def u(n) :
	return 1000*1.2**n-100*n	
	"""