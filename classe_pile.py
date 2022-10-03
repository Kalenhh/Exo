#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  classe_pile.py

###############
# classe Pile #
###############

class Pile:
	
	# constructeur
	def __init__(self,max=10):
		self.pil=[]	# pile vide
		self.limite = max

	# entrer une valeur dans la pile
	def empiler(self,valeur):
		if self.taille() >= self.limite :
			self.pil.pop(0)
		self.pil.append(valeur)

	def __str__(self) :
		s = ""
		self.pil.reverse()
		for i in self.pil :
			s += str(i)+"\n"
		self.pil.reverse()
		return s
			

		
	# sortir une valeur de la pile
	def depiler(self):
		if len(self.pil)>0:
			return self.pil.pop()
		else:
			return None
		
	# taille de la pile
	def taille(self):
		return len(self.pil)
		
	# la pile est-elle vide ?
	def pileestvide(self):
		if len(self.pil)==0:
			return True
		else:
			return False
	
#############
# test pile #
#############

pile=Pile()	# initalisation pile vide
print(pile.pileestvide())
for i in range(10):
	pile.empiler(i)

print(pile)

print("taille :",pile.taille())
for i in range(12):
	print(i,pile.depiler())


