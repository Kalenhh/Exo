#coding:utf-8
# Exo 4 (type Bac)
"""
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







# ---------------------------------------------------------------------
# Exo Bac 

flotte = {
	12 : {"type" : "electrique", "etat" : 1,"station" : "Prefecture"},
	80 : {"type" : "classique", "etat" : 0,"station" : "Saint-Leu"},
	45 : {"type" : "classique", "etat" : 1,"station" : "Baraban"},
	41 : {"type" : "classique", "etat" : -1,"station" : "Citadelle"},
	26 : {"type" : "classique", "etat" : 1,"station" : "Coliseum"},
	28 : {"type" : "electrique", "etat" : 0,"station" : "Coliseum"},
	74 : {"type" : "electrique", "etat" : 1,"station" : "Jacobins"},
	13 : {"type" : "classique", "etat" : 0,"station" : "Citadelle"},
	83 : {"type" : "classique", "etat" : -1,"station" : "Saint-Leu"},
	22 : {"type" : "electrique", "etat" : -1,"station" : "Joffre"}
}


def velosdispo(station) :
	liste = []
	for v in flotte :
		if flotte[v]["station"] == station :
			liste.append(v)

	return liste		


def velo_pas_pt() :
	for v in flotte :
		if flotte[v]["etat"] != -1 :
			print(v,flotte[v]["station"])

def ou_aller(user_pos) :

	for i in station_pos :
		dis = distance(station_pos[i],user_pos)
		dispo = velosdispo(station_pos[i])
		if dis <= 800 :
			print(station_pos[i],distance,dispo)


"""


# Liste chainée POO

class ListeChainée() :

	def __init__(self,element=None,suivant1=None) :
		self.valeur = element 
		self.suivant = suivant1

	def ajouter(self,element) :

		if self.valeur is None :
			self.valeur = element
			return

		elif self.suivant is None :
			self.suivant = ListeChainée(element)
			return

		else :
			self.suivant.ajouter(element)

	def longueur(self,i=0) :
		if self.valeur is None :
			return 0

		i += 1
		if self.suivant is None :	
			return i

		else :
			return self.suivant.longueur(i)

	def acceder(self,i) :

		if i == 0 :
			return self.valeur

		elif self.suivant is None and i != 0 :
			return "Index big fonction acceder"

		else :
			return self.suivant.acceder(i-1)

	def inserer(self,element,i) :

		if i == 0 :
			self.suivant = ListeChainée(self.valeur,self.suivant)
			self.valeur = element
			return

		elif i > 0 and self.suivant is None :
			return "Index big fonction inserer"

		else :
			self.suivant.inserer(element,i-1)


	def supprimer_val(self,element) :

		if self.valeur == element :
			self.valeur = self.suivant.valeur
			self.suivant = self.suivant.suivant

		elif self.suivant is None and self.valeur != element :
			print("Not In List fonction supprimer_val")
			return

		else :
			self.suivant.supprimer_val(element)


	def supprimer_ind(self,i) :

		if i == 0 :
			self.valeur = self.suivant.valeur
			self.suivant = self.suivant.suivant

		elif self.suivant == None and i > 0 :
			print("Index Big fonction supprimer_ind")
			return 

		else :
			self.suivant.supprimer_ind(i-1)


	def modifier(self,element,i) :

		if i == 0 :
			self.valeur = element
			return

		elif self.suivant == None and i > 0 :
			print("Index Big fonction modifier")
			return 

		else :
			self.suivant.modifier(element,i-1)
			

	def vider(self) :
		self.valeur,self.suivant = None,None
		return

	def __str__(self) :
		
		s = ""
		for i in range(self.longueur()) :
			s += str(self.acceder(i))
		return s

	def copy(self) :
		new = ListeChainée()
		
		for i in range(self.longueur()) :
			new.ajouter(self.acceder(i))

		return new	

		


						



def aff() :
	for i in range(10) :
		print(a.acceder(i),i)
	print("\n")


a = ListeChainée(0)

for i in range(1,11) :
	a.ajouter(i)

a.inserer("lol",3)

aff()

a.supprimer_ind(3)

aff()

a.modifier(45,3)

aff()

print(a)

a.vider()
print(a.valeur,a.suivant)




# -------------------------------------------------------------------------

"""
def fonc(a,b) :
	fonc = 3
	return a+b

fonc = fonc(3,3)

print(fonc)

"""