#vide.py
#coding:utf-8

from tkinter import*
from time import*
from copy import*
from random import*


root = Tk()

def tri_insert() :
	"""
	On prend chaque item et on l'insere juste avant la valeur plus grande que lui en partant du debut de la liste
	"""
	liste = [o for o in range(100)]
	shuffle(liste)

	for i in range(len(liste)) : 	# i est l'index de l'item selectionné
		j = 0 						# j est l'index ou l'item sera inseré

		actu(deepcopy(liste),i)

		while liste[i] > liste[j] :		# Si la valeur à i est plus grande que la valeur à j 
			j = j+1 					# On incrémente j

		liste.insert(j,liste[i])	# On insere la valeur i à l'index j
		liste.pop(i+1)				# On supprime la valeur i donc i+1

		actu(deepcopy(liste),j)

		print(deepcopy(liste))
		print(i)


def tri_select() :
	"""
	On prend la 1ère valeur puis on cherche le minimum dans le reste de la liste pour l'inserer à la suite puis on ré-itère.
	"""
	liste = [o for o in range(100)]
	shuffle(liste)

	for i in range(len(liste)-1) : 	# i est l'index de l'item selectionné
		minimum = liste[i]
		position = i

		actu(deepcopy(liste),position-1)

		for j in range(i,len(liste)) :	# j est l'index des items comparé avec la valeur i 
			if liste[j] < minimum :		# On cherche la plus petite valeur
				minimum = liste[j]
				position = j

		actu(deepcopy(liste),position)

		liste.insert(i,minimum)		# On insere la plus petite valeur trouvé à l'index i 
		liste.pop(position+1)		# On supprime la valeur i donc i+1
	
	actu(deepcopy(liste),position)


def actu(liste,val) :
	sleep(0.05)
	global can
	can.delete(ALL)

	pla = 10
	for i in range(len(liste)) :
		if i == val :
			can.create_line(pla,200,pla,200-liste[i]*2,fill="blue",width=5,tags="ligne")
		else :
			can.create_line(pla,200,pla,200-liste[i]*2,fill="red",width=5,tags="ligne")
		pla = pla+10

	root.update()	

can = Canvas(root,bg="yellow",width=1030, height=200)
can.pack()

la = Button(root,text="insertion",command=tri_insert)
la.pack(side="right")

select = Button(root,text="selection",command=tri_select)
select.pack(side="right")

root.mainloop()
