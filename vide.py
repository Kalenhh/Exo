#coding:utf-8
# Vide

class Node() :

	def __init__(self,element,gauche=None,droit=None) :
		self.value = element
		self.left = gauche
		self.right = droit

class Arbre() :

	def __init__(self,element) :
		self = Node(element)


	def modif(self,element,path) :
		"""
		modifier la valeur d'un node
		"""

		for i in path :
			if i isinstance(Node) is False or (i != self.left and i != self.right) :
				print("incorrect path")
				return

			self = i

		self.value = element

	def add(self,element,pos,path) :
		"""
		True : droit
		False : gauche
		"""

		for i in path :
			self = i 
		if pos :
			self.right = Node(element)
		if not pos :
			self.left = Node(element)

	def node_value(self,path) :
		for i in path :
			self = i 

		return self.value







