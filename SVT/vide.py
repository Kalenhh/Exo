#vide.py
#coding:utf-8

# Librairies :-----------------------------------------------------------------------------------------------------------

from tkinter import*
from math import*
from csv import*
from time import*
from colour import*

# Set Variables :--------------------------------------------------------------------------------------------------

lieu_cdi = [[(287,241)],0]
lieu_ateliers = [[(445,366),(405,629),(619,710)],0]
lieu_cantine = [[(339,896)],0]
lieu_perm = [[(356,303)],0]
lieu_vie_sco = [[(300,306)],0]
lieu_gymnase = [[(105,489)],0]
lieu_recre = [[(344,408),(358,197)],0]
lieu_muscu = [[(453,584)],0]
lieu_internat = [[(187,69)],0]
lieu_classe = [[(430,546),(378,246)],0]
lieu_labo = [[(378,107)],0]
lieu_couloirs = [[(421,565),(468,432)],0]
lieu_admin = [[(543,798),(549,931)],0]
lieu_profs = [[(288,170)],0]

lieu_all_0 = [lieu_cdi,lieu_ateliers,lieu_cantine,lieu_perm,lieu_vie_sco,lieu_gymnase,lieu_recre,lieu_muscu,
lieu_internat,lieu_classe,lieu_labo,lieu_couloirs,lieu_admin,lieu_profs]
lieu_all = [o for i in lieu_all_0 for o in i[0]]



red = "#ff0000"
blue = "#66ccff"
green = "#66B266"

chart = list(Color("green").range_to(Color("red"),100))

# Fonctions :-------------------------------------------------------------------------------------------

def ouverture(root) :
	"""
	Ouverture du fichier csv
	"""
	with open(root,"r",encoding="utf-8") as fichier :
		lecteur = reader(fichier,delimiter=";")
		table = []
		for i in lecteur :
			table.append(i)
		return table


def distance(x1,y1,x2,y2) :
	"""
	calcule la distance entre 2 points
	retourne la distance en METRE
	"""

	delta = sqrt(((x1-x2)**2)+(y1-y2)**2)

	delta = delta * 130 / 580
	return int(round(delta,0))


def point_value(source,distance) :
	"""
	source = valeur en DECIBEL de la source de bruit
	distance = distance entre la source et le point en METRE
	value = sortie en DECIBEL
	"""

	if distance == 0 :
		distance = distance+1

	ratio = (1/distance)**2
	value = source + (10*log(ratio,10))
	return int(round(value,0))


def point_total_value(liste,coord) :
	"""
	liste = toute les sources appareillé avec leur valeur
	coord = coordoné du point qu'on determiine la sous forme de TUPLE
	"""

	value = 25 # ------------------ Valeur minimale en decibel (bruit ambient) -----------------------------------

	for i in liste :
		# i[0] = liste des tuple de coord  i[1] = valeur en dB


		if i[1] == "None" :
			continue

		for o in i[0] : # pour tt les tuples,o =tuple

			rep = point_value(int(i[1]),  distance(coord[0],coord[1],o[0],o[1])  )

			value = 10*log((10**(value/10))+(10**(rep/10)),10)

	return int(round(value,0)) 		


def draw_data(liste,heure,donne) :

	global chart
	global can
	rep = appairage(liste,heure,donne)
	print(rep)

	for i in range(70) : # x du point 
		for o in range(100) : # y du point 

			value = point_total_value(rep,(i*10,o*10))
			print(value)

			can.create_line(i*10,o*10,10+i*10,10+o*10,width=10,fill=chart[value])
			root.update()
			

def appairage(liste,heure,donne) :
	"""
	liste = liste des mesure
	heure = heure demandé
	donne = mini maxi ou moyenne = 2 , 3 , 4 
	"""

	for i in liste :
		if int(i[1]) == heure :

			if i[0] == "CDI" :
				lieu_cdi[1] = i[donne]

			if i[0] == "Ateliers" :
				lieu_ateliers[1] = i[donne]

			if i[0] == "Cantine" :
				lieu_cantine[1] = i[donne]

			if i[0] == "Permanence" :
				lieu_perm[1] = i[donne]

			if i[0] == "Vie Scolaire" :
				lieu_vie_sco[1] = i[donne]

			if i[0] == "Gymnase" :
				lieu_gymnase[1] = i[donne]

			if i[0] == "Cours" :
				lieu_recre[1] = i[donne]
			
			if i[0] == "Salle de muscu" :
				lieu_muscu[1] = i[donne]

			if i[0] == "Internat" :
				lieu_internat[1] = i[donne]

			if i[0] == "Salle de classe" :
				lieu_classe[1] = i[donne]
			
			if i[0] == "Laboratoire" :
				lieu_labo[1] = i[donne]

			if i[0] == "Couloirs" :
				lieu_couloirs[1] = i[donne]

			if i[0] == "Administration" :
				lieu_admin[1] = i[donne]
			
			if i[0] == "Salle des Profs" :
				lieu_profs[1] = i[donne]

	lieu_all_0 = [lieu_cdi,lieu_ateliers,lieu_cantine,lieu_perm,lieu_vie_sco,lieu_gymnase,lieu_recre,lieu_muscu,
	lieu_internat,lieu_classe,lieu_labo,lieu_couloirs,lieu_admin,lieu_profs]

	return lieu_all_0



# Main root :----------------------------------------------------------------------------------------------




mesure_all = ouverture("mesure.csv")
mesure_all.pop(0)

root = Tk()
root.minsize(1000,1000)
root.maxsize(1000,1000)

frame_dessin = Frame(root,height=1000,width=700)
frame_dessin.pack(side="left")

can = Canvas(frame_dessin,height=1000,width=700,bg=green)
can.pack()

repliste = []

def mmove(event):
	global repliste
	print(event.x, event.y)
	repliste.append((event.x,event.y))
	print(repliste)


root.bind('<Button-1>', mmove)




draw_data(mesure_all,6,2)

print(point_total_value(appairage(mesure_all,1,4),(287,241)))



source = PhotoImage(file="plan.PNG")
can.create_image(0,0,anchor=NW,image=source)

for i in lieu_all :
	can.create_line(i[0]-1,i[1]-1,i[0]+1,i[1]+1,width=5,fill=green)




frame_config = Frame(root,height=1000,width=300,bg="yellow")
frame_config.pack(side="right",fill=BOTH)


root.mainloop()