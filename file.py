#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file.py

#############
# fonctions #
#############

# entrer une valeur dans la file
def entrer(file_,valeur):
	file_.append(valeur)
	
# sortir une valeur de la file
def sortir(file_):
	if len(file_)>0:
		return file_.pop(0)
	else:
		return None
	
# taille de la file
def taille(file_):
	return len(file_)
	
# la file est-elle vide ?
def fileestvide(file_):
	if len(file_)==0:
		return True
	else:
		return False

#############
# test file #
#############

file_=[]	# initalisation file vide
print(fileestvide(file_))
for i in range(10):
	entrer(file_,i)
print(taille(file_))
for i in range(12):
	print(sortir(file_))


