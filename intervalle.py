#coding:utf-8
# Fonction intervalle de confiance

"""

from math import sqrt

def inter(cara,n) :
	# cara 	= nombre d'échantillon possédant le caractère
	# n 	= taille total de l'échantillon

	freq = cara/n 	# Calcul de la fréquence
	print("La fréquence vaut : ",freq,"",freq*100,"%")

	### Partie calcul compliqué

	mid = sqrt(freq*(1-freq)/n)
	cal = (round(freq-1.96*mid,4),round(freq+1.96*mid,4))

	###

	print("Borne inférieur : ",cal[0],"\nBorne supérieur : ",cal[1])
	return cal

# Exemple
print("Fréquence et Intervalle de confiance pour 135 caractère sur un échantillon de 400 :\n")
print(inter(180,900))

def pop(m,c,r) :
	# m : effectif de la population marqué lors de la 1ere capture
	# c : effectif de la populations capturé lors de la 2eme capture
	# r : effectif des individus marqués parmi c

	proportion = r/c # Pech

	echantillon = sqrt(		(proportion*(1-proportion))		/c)	# Sech

	cal = ( 	m/(proportion + 1,96*echantillon) , m/(proportion - 1,96*echantillon)	)

	return cal 

print(pop())


"""


class ListeChainée() :
	"""
	Interface pour des listes chainées
	"""

	def __init__(self,element=None,suivant1=None) :
		"""
		Initialisation des valeurs de l'objet
		'element' : objet
		'suivant' : 'ListeChainée'
		"""
		self.valeur = element 
		self.suivant = suivant1


	def ajouter(self,element) :
		"""
		Ajouter une valeur à la fin de la liste chainée
		'element' : objet à ajouter à la chaine
		"""

		if self.valeur is None :		# Si l'objet 'ListeChainée' actuel n'as pas de valeur
			self.valeur = element		# On lui attribue 'element'
			return

		elif self.suivant is None :		# Si l'objet 'ListeChainée' actuel n'as pas pointeur valide et est donc le dernier chainon
			self.suivant = ListeChainée(element)	# On lui attribue un objet 'ListeChainée' de valeur = 'element'
			return

		else :
			self.suivant.ajouter(element)	# On passe la commande au prochain pointeur


	def longueur(self,i=0) :
		"""
		Retourne la longueur de la liste chainée
		i : nombre de chainon de la liste chainée
		"""

		if self.valeur is None :	# Si l'objet 'ListeChainée' actuel n'as pas de valeur
			return i

		i += 1
		if self.suivant is None :	# Si l'objet 'ListeChainée' actuel n'as pas pointeur valide et est donc le dernier chainon
			return i

		else :
			return self.suivant.longueur(i)	# On passe la commande au prochain pointeur


	def acceder(self,i) :
		"""
		Retourne la valeur du chainon d'index i dans la liste chainée
		i : index du chainon recherché
		"""

		if i == 0 :					# Si l'objet 'ListeChainée' actuel est celui recherché
			return self.valeur

		else :
			return self.suivant.acceder(i-1)	# On passe la commande au prochain pointeur


	def inserer(self,element,i) :
		"""
		Inserer un objet 'ListeChainée' dans la liste chainée à l'index 'i' avec pour valeur 'element'
		'element' 	: valeur du chainon
		'i' 		: index où l'inserer 
		"""

		if i == 0 :					# Si l'objet 'ListeChainée' actuel est celui recherché
			self.suivant = ListeChainée(self.valeur,self.suivant)
			self.valeur = element
			return


		else :
			self.suivant.inserer(element,i-1)	# On passe la commande au prochain pointeur


	def supprimer_val(self,element) :
		"""
		Supprimer la premiere occurence de 'element' dans la liste chainée
		'element' : valeur à supprimer
		"""

		if self.valeur == element :		# Si la valeur de l'objet correspond à 'element'
			self.valeur = self.suivant.valeur
			self.suivant = self.suivant.suivant

		elif self.suivant is None and self.valeur != element : # Si 'element' n'est pas dans la liste chainée
			print("erreur")
			return

		else :
			self.suivant.supprimer_val(element)		# On passe la commande au prochain pointeur


	def supprimer_ind(self,i) :
		"""
		Supprimer le chainon d'index i
		i : index du chainon à supprimer
		"""

		if i == 0 :				# Si l'objet 'ListeChainée' actuel est celui recherché
			self.valeur = self.suivant.valeur
			self.suivant = self.suivant.suivant

		else :
			self.suivant.supprimer_ind(i-1)		# On passe la commande au prochain pointeur


	def modifier(self,element,i) :
		"""
		Remplacer la valeur du chainon d'index i par 'element'
		'element' 	: futur valeur du chainon
		'i' 		: index du chainon à modifier
		"""

		if i == 0 :				# Si l'objet 'ListeChainée' actuel est celui recherché
			self.valeur = element
			return

		else :
			self.suivant.modifier(element,i-1)		# On passe la commande au prochain pointeur


	def vider(self) :
		"""
		Vider totalement la liste chainée
		"""

		self.valeur,self.suivant = None,None
		return

	def __str__(self) :
		"""
		Redéfinition de la fonction 'print()'
		"""
		
		s = "("							# Chaine de caractère
		mid = self.longueur()

		for i in range(mid) :			# On parcourt tout les chainons de la liste chainée
			s += str(self.acceder(i))	# On incrémente la chaine de caractère avec la valeur des chainons

			if (mid-i-1) != 0 :			# Si i n'est pas le dernier de la boucle
				s += ","				# On ajoute une virgule de séparation

		return s + ")"

	
	def copy(self) :
		"""
		Créer une copie profonde de la liste
		"""

		new = ListeChainée()
		
		for i in range(self.longueur()) :		# On parcourt toute la liste chainée
			new.ajouter(self.acceder(i))		# On ajoute chaque valeur de chaque chainon à la nouvelle liste chainée

		return new	


	def __add__(self,a) :
		"""
		Redéfinition de l'opération '+'
		a : objet que l'on ajoute , doit etre un objet 'ListeChainée'
		"""

		for i in range(a.longueur()) :		# On parcourt toute la liste chainée
			self.ajouter(a.acceder(i))		# On ajoute chaque valeur de chaque chainon à la liste chainée
		return self



def verif() :
	"""
	Fonction de verification du bon fonctionnement de la classe 'ListeChainée'
	'show' 	: False > vérification par assertion , True > vérification par assertion avec retour visuel
	"""

	chain = ListeChainée()
	for i in range(10) :		# On crée une liste chainée
		chain.ajouter(i)

	assert chain.acceder(0) == 0 
	assert chain.acceder(9) == 9		# Fonction acceder et longueur
	assert chain.longueur() == 10

	chain.inserer("test",3)
	assert chain.acceder(3) == "test"	# Fonction acceder

	chain.supprimer_ind(3)
	assert chain.acceder(3) == 3		# Fonction supprimer_ind

	chain.modifier(45,3)
	assert chain.acceder(3) == 45		# Fonction modifier

	chain += chain
	assert chain.longueur() == 20		# Opération +

	chain2 = chain.copy()
	chain2.modifier("chain2",0)
	assert chain.acceder(0) == 0 		# Fonction copy
	assert chain2.acceder(0) == "chain2"


verif()