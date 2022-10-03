#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  classe_pile.py

###############
# classe Pile #
###############

class Pile:
	
	# constructeur
	def __init__(self,maxe=10):
		self.pil=[]	# pile vide
		self.limite = maxe

	# entrer une valeur dans la pile
	def empiler(self,valeur):
		if self.taille() >= self.limite :
			self.pil.pop(0)
		self.pil.append(valeur)

	def __str__(self) :
		s = ""
		cache = Pile()

		for i in range(self.taille()) :
			mid = self.depiler()
			cache.empiler(mid)
			s += str(mid) + "\n"

		for i in range(cache.taille()) :
			self.empiler(cache.depiler())

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
for i in range(30):
	pile.empiler(i)

print(pile)

print("taille :",pile.taille())
for i in range(12):
	print(i,pile.depiler())


