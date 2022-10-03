#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pile.py

#############
# fonctions #
#############

# entrer une valeur dans la pile
def empiler(pile,valeur):
	pile.append(valeur)
	
# sortir une valeur de la pile
def depiler(pile):
	if len(pile)>0:
		return pile.pop()
	else:
		return None
	
# taille de la pile
def taille(pile):
	return len(pile)
	
# la pile est-elle vide ?
def pileestvide(pile):
	if len(pile)==0:
		return True
	else:
		return False
	
#############
# test pile #
#############

pile=[]	# initalisation pile vide
print(pileestvide(pile))
for i in range(10):
	empiler(pile,i)
print(taille(pile))
for i in range(12):
	print(depiler(pile))


