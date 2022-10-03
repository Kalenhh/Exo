#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  classe_file.py

###############
# classe File #
###############

class File:
	# constructeur
	def __init__(self):
		self.fil=[]
			
	# entrer une valeur dans la file
	def entrer(self,valeur):
		self.fil.append(valeur)
	
	# sortir une valeur de la file
	def sortir(self):
		if len(self.fil)>0:
			return self.fil.pop(0)
		else:
			return None
	
	# taille de la file
	def taille(self):
		return len(self.fil)
	
	# la file est-elle vide ?
	def fileestvide(self):
		if len(self.fil)==0:
			return True
		else:
			return False
	
#############
# test file #
#############

file_=File()	# initalisation file vide
print(file_.fileestvide())
for i in range(10):
	file_.entrer(i)
print(file_.taille())
for i in range(12):
	print(file_.sortir())


