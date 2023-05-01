#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import inf
from copy import deepcopy


def minimum_dico(dico):
	"""
	renvoie la clé du dictionnaire 'dico' qui contient la valeur minimale
	"""
	minimum = inf	
	for cle in dico :
		if dico[cle] < minimum :
			minimum = dico[cle]
			cle_mini = cle
	return cle_mini


def dijkstra(graphe,depart) :
	"""
	renvoie un dictionnaire dont les clés (sommets de 'graphe') donnent
	la distance minimale par rapport au sommet 'depart'
	"""

	if depart not in graphe :
		return None
	
	d_minimales = {}	# distances minimales
	d_courantes = {sommet:inf for sommet in graphe}	# distances courantes infinies pour commencer
	d_courantes[depart] = 0		# distance courante 0 pour le sommet de départ
	l = []

	while d_courantes!={}:
		
		sommet = minimum_dico(d_courantes)

		for voisin in (graphe[sommet]) :
			distance=graphe[sommet][voisin]

			if voisin not in d_minimales :
				d_courantes[voisin] = min(d_courantes[voisin], d_courantes[sommet] + distance)

		d_minimales[sommet] = d_courantes[sommet]
		del d_courantes[sommet]

		l.append((sommet,d_minimales[sommet]))

	print('fini')
	return l



graphe={"Bar Le Duc":{"Nancy":83,"Metz":101},
"Nancy":{"Metz":55,"Bar Le Duc":83,"Lunéville":36},
"Metz":{"Nancy":55,"Bar Le Duc":101,"Thionville":30,"Sarrebourg":96},
"Lunéville":{"Nancy":36,"Sarrebourg":54,"Saint-Die":52},
"Sarrebourg":{"Lunéville":54,"Metz":96,"Saint-Die":71},
"Thionville":{"Metz":30},
"Saint-Die":{"Lunéville":52,"Sarrebourg":71}
}

depart=input("Sommet de départ : ? ")
print(dijkstra(graphe,depart))

