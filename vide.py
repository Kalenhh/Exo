#vide.py
#coding:utf-8

from tkinter import*
from time import*
from copy import*
from random import*


root = Tk()


def tri_insert() :
	"""
	On prend chaque item et on l'insere juste apres la valeur plus petite que lui
	"""
	liste = [o for o in range(100)]
	shuffle(liste)

	for i in range(len(liste)) : 	# i est l'index de l'item selectionné
		j = 0 						# j est l'index ou l'item sera inseré

		while liste[i] > liste[j] :		# Si la valeur à i est plus grande que la valeur à j 
			j = j+1 					# On incrémente j 

		liste.insert(j,liste[i])	# On insere la valeur i à l'index j
		liste.pop(i+1)				# On supprime la valeur i donc i+1

		print(deepcopy(liste))
		actu(deepcopy(liste))
		print(i)
		pass

def actu(liste) :
	sleep(1)
	global can
	can.destroy()
	can = Canvas(root,bg="yellow",width=300, height=200)
	can.pack()

	pla = 10
	for i in liste :
		can.create_line(pla,0,pla,i*10,fill="red",width=5,tags="ligne")
		pla = pla+10

	return	

can = Canvas(root,bg="yellow",width=300, height=200)
can.pack()

la = Button(root,text="la",command=tri_insert)
la.pack(side="right")

root.mainloop()
