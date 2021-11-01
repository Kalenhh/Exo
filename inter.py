#coding:utf-8

from tkinter import*
from tkinter.filedialog import *


app = Tk()
app.title("Sauce Folder")
app.minsize(300,200)

main_frame = Frame(app,bg="yellow")
main_frame.pack(side="right",fill=BOTH,expand=1)

texte = Label(main_frame, text = "application")
texte.pack(side="top")
texte.configure(fg = "blue")

#----------------------------------------------------------------------------------------------------------

def comparer_doublon() :
	with open("C:/Users/baudo/Desktop/number.txt","r") as liste_number :
		liste_number_lignes = liste_number.readlines()
		for element in liste_number_lignes :
			if int(element) == int(sauce.get()) :
				resultat.set("deja dans la liste")
				return
			resultat.set("pas dans la liste")

def eliminer_doublon() :
	with open("C:/Users/baudo/Desktop/number.txt","r") as liste_number :
		liste_number_lignes = liste_number.readlines()
		liste_clear = []
		for element in liste_number_lignes :
			if element not in liste_clear :
				liste_clear.append(element)
				continue
			print("doublon")

		with open("C:/Users/baudo/Desktop/number.txt","w") as liste_number :
			liste_number.writelines(liste_clear)

def quantity() :
	with open("C:/Users/baudo/Desktop/number.txt","r") as liste_number :
		liste_number_lignes = liste_number.readlines()
		quantite.set(len(liste_number_lignes))

#-------------------------------------------------------------------------------------------------------------

FrameMenu = Frame(app,bg="blue",borderwidth=10)
FrameMenu.pack(side="left",fill=BOTH)

comparer = Button(FrameMenu,text="Comparer")
comparer.pack()

nettoyer = Button(FrameMenu,text="clear")
nettoyer.pack(fill=BOTH)



app.mainloop()