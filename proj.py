#coding:utf-8
# Terminale Générale BAUDOIN Mathieu
# Projet 01 Calculatrice HP et logique RPN

from math import*

class Pile() :
	"""
	Structure de donnée abstraite : les valeurs sortent et entrent par la fin
	La pile part de l'index 0 ;   exemple : [1,2,3,4] 
											1 est la valeur au fond de la pile
											4 est la valeur sur le dessus de la pile
	"""

	def __init__(self,limite=8) :
		self.values = []		# Liste contenant les valeurs de la pile
		self.max_len = limite 	# Taille maximale de la pile

	def depiler(self) :
		"""
		Retourne la valeur sur le dessus de la pile et l'enleve de la liste des valeurs
		"""
		if not self.estvide() :
			top_value = self.values.pop()
			return top_value

	def empiler(self,add_value) :
		"""
		Ajoute une valeur sur le dessus de la pile
		"""
		if len(self.values) >= self.max_len :	# Si la taille maximale est atteinte , on supprime la valeur du fond de la pile
			self.values.pop(0)
		self.values.append(add_value)

	def taille(self) :
		"""
		Retourne la taille (int) actuelle de la pile
		"""
		return len(self.values)

	def estvide(self) :
		"""
		Retourne Vrai si la pile est vide sinon Faux
		"""
		if self.taille() == 0 :
			return True
		else :
			return False

	def __str__(self) :
		"""
		Redefinis la fonction integre 'print()' pour la Classe Pile
		"""
		string = ""
		for i in range(len(self.values)) :
			string = "| "+str(len(self.values)-i) + " | " + str(self.values[i]) + "\n" + string
		return string


def operation(pile,op) :
	"""
	Effectue l'operation 'op' sur les 2 premiers elements de l'objet Pile 'pile'
	"""

	first,second = pile.depiler(),pile.depiler()	# On prend les valeurs utilises pour le calcul

	try :
		resultat = eval(str(second)+op+str(first))	# On essaye d'effectuer la calcul
		pile.empiler(resultat)						# Fonctionne si 'op' est une operation de base : +,-,*,**
	except :
		try :											# On essaye d'effectuer la calcul
			resultat = eval(op+"("+str(first)+")")		# Fonctionne si 'op' est une operation de la librairie 'math' : cos,tan,log,...
			pile.empiler(resultat)
		except :
			print("L'opération n'est pas réalisable")	# Si 'op' ne correspond a rien , On affiche une erreur et rempile les valeurs
			if second is not None :
				pile.empiler(second)
			if first is not None :
				pile.empiler(first)

	return pile


class Calculatrice() :
	"""
	Objet Calculatrice qui utilise la logique RPN des calculatrices HP pour effectuer des calculs
	"""

	def __init__(self) :
		self.memory = Pile(limite=8)							# On initialise la memoire de la calculette
		self.op = 	["+","-","*","/","**",						# Liste des opérations
					 "sin","cos","tan","exp","log","log10"]

	def loop(self) :
		active = True
		while active :
			cmd = input('>')
			cmd = cmd.lower()

			for i in self.op :
				if cmd == i :
					self.memory = operation(self.memory,cmd)	
					cmd = self.memory.depiler()

			if cmd == 'q' :
				active = False

			elif cmd == 's' :
				self.memory.depiler()

			else :
				if cmd is not None :
					try : int(cmd)
					except : print("L'entrée n'est pas valide") ; continue
					self.memory.empiler(cmd)
			
			print(self.memory)

app = Calculatrice()
app.loop()


