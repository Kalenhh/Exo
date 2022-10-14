#coding:utf-8
# Terminale Générale BAUDOIN Mathieu
# Projet 01 Calculatrice HP et logique RPN

from math import*

class Pile() :
	"""
	Structure de donnée abstraite : les valeurs sortent et entrent par la fin
	"""

	def __init__(self) :
		self.values = []
		self.max_len = 8

	def depiler(self) :
		if not self.estvide() :
			top_value = self.values.pop()
			return top_value

	def empiler(self,add_value) :
		if len(self.values) >= self.max_len :
			self.values.pop(0)
		self.values.append(add_value)

	def taille(self) :
		return len(self.values)

	def estvide(self) :
		if self.taille() == 0 :
			return True
		else :
			return False

	def __str__(self) :
		string = ""
		for i in range(len(self.values)) :
			string = "| "+str(len(self.values)-i) + " | " + str(self.values[i]) + "\n" + string
		return string
			



a = Pile()
a.empiler(25)
a.empiler(567)
for i in range(20) :
	a.empiler(i)
print(a)
print(a.depiler())
print(a.depiler())

def operation(pile,op) :

	first,second = pile.depiler(),pile.depiler()

	try :
		resultat = eval(op+"("+str(first)+")")
		pile.empiler(resultat)
	except :
		try :
			resultat = eval(str(second)+op+str(first))
			pile.empiler(resultat)
		except :
			print("Erreur op 45")
			if second is not None :
				pile.empiler(second)
			if first is not None :
				pile.empiler(first)

	return pile


class Calculatrice() :

	def __init__(self) :
		self.memory = Pile()
		self.op = ["+","-","*","/","**","sin","cos","tan","exp","log","log10"]

	def loop(self) :
		active = True
		while active :
			cmd = input('>')


			for i in self.op :
				if cmd == i :
					self.memory = operation(self.memory,cmd)	
					cmd = self.memory.depiler()

			if cmd == 'q' :
				active = False

			elif cmd == 's' :
				self.memory.depiler()

			elif cmd == "" :
				continue

			else :
				if cmd is not None :
					self.memory.empiler(cmd)
			print(self.memory)

app = Calculatrice()
app.loop()


