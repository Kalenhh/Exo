#coding:utf-8

from tkinter import*
from tkinter.filedialog import *
import random

app = Tk()
app.title("Sauce Folder")
app.minsize(600,400)

main_frame = Frame(app,bg="yellow")
main_frame.pack(fill=BOTH,expand=1)

#Fonction data :----------------------------------------------------------------------------------------------------------

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

def random() :
	with open("C:/Users/baudo/Desktop/number.txt","r") as liste_number :
		liste_number_lignes = liste_number.readlines()
		random.set(liste_number_lignes[random.randrange(len(liste_number_lignes))])

#Fonction Tk.Frame :-------------------------------------------------------------------------------------------------------------

def menu():
	FrameMenu = Frame(main_frame,bg="blue",borderwidth=10)
	FrameMenu.pack(side="left",fill=BOTH)

	comparer = Button(FrameMenu,text="Comparer",command=frame_comparer)
	comparer.pack()

	doublon = Button(FrameMenu,text="clear",command=frame_doublon)
	doublon.pack(fill=BOTH)

	stat = Button(FrameMenu,text="stat",command=frame_stat).pack(fill=BOTH)

def frame_stat():
	global frame_affichage
	frame_affichage.destroy()
	frame_affichage = Frame(main_frame)
	
	frame_affichage.pack(side="right",fill=BOTH,expand=1)
	stat = Label(frame_affichage,text="ok stat").pack()


def frame_comparer():
	global frame_affichage
	frame_affichage.destroy()
	frame_affichage = Frame(main_frame)
	frame_affichage.pack(side="right",fill=BOTH,expand=1)

	FrameComparer = Frame(frame_affichage,bg="green")
	FrameComparer.pack(side="right",fill=BOTH,expand=1)


def frame_doublon():
	global frame_affichage
	frame_affichage.destroy()
	frame_affichage = Frame(main_frame)
	frame_affichage.pack(side="right",fill=BOTH,expand=1)

	FrameDoublon = Frame(frame_affichage,bg="pink")
	FrameDoublon.pack(side="right",fill=BOTH,expand=1)


#Programme :---------------------------------------------------------------------------------------------------------

menu()
frame_affichage = Frame(main_frame)
frame_affichage.pack(side="right",fill=BOTH,expand=1)
frame_stat()
frame_doublon()



app.mainloop()