#coding:utf-8

#Projet : Lecture et traitement de fichier CSV 

from csv import*
from tkinter import*
from time import*

root = Tk()
root.minsize(600,400)
frame = Frame(root)
frame.pack()

sss = StringVar()


def ouverture(fichier) :
	global progress
	global bar

	with open(fichier,"r",encoding="utf-8") as donné :
		aaa = reader(donné,delimiter=";")
		table = ["1","A","2020","0"]
		letter = "A"
		progress = 0 
		for i in aaa :
			if i[1][0] != letter:
				letter = i[1][0]
				progress = progress + 1
				bar = progress *100/434
				print(int(round(bar,0)))
				sss.set(bar)


			table.append(i)

		return table

vued = ouverture("nat2020.csv")
print(len(vued))



def requete1(donné,prenom,année) :
	trouvé = False
	while trouvé == False :
		for i in donné :
			if prenom == i[1] and année == i[2] :
				trouvé = True
				return i[3]
				continue

lab = Label(frame,textvariable=sss).pack()


root.mainloop()