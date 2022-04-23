#lm.py
#coding:utf-8

from tkinter import*
from math import*


# Fenetre principal ----------------------------------------------------------------------

app = Tk()
app.title("Calculatrice")
app.minsize(700,120)
app.maxsize(700,120)

main_frame = Frame(app,bg="yellow")
main_frame.pack(fill=BOTH,expand=1)


# Variables ----------------------------------------------------------------------

calcul = StringVar()
resultat = StringVar()
ecriture = IntVar()

pavé_aide = str("Bouton Rep : Copie la valeur selectionnée dans l'historique \nRaccourci : Ctrl droite \n"
				"\n Bouton Effacer : Efface le calcul \nRaccourci : Alt droite \n"
				"\nBouton Suppr : Supprime l'historique")


# Fonctions ----------------------------------------------------------------------

def calculer(e=0) :
	try :
		eval(calcul.get())
	except :
		resultat.set("Incorrecte")
		return

	resultat.set(str(round(  eval(calcul.get()),4   )))

	if historique_liste.get(0) != resultat.get() :
		historique_liste.insert(0,resultat.get())

	historique_liste.selection_clear(0,END)
	historique_liste.selection_set(0)

	if ecriture.get() == 2 :	
		resultat.set(str(  format(float(eval(calcul.get())),".1E")  ))

	if len(resultat.get()) > 9 :
		R2.invoke()

def effacer(e=0) :
	calcul.set("")

def repliquer(e=0) :
	calcul.set(calcul.get()+str(historique_liste.get(   historique_liste.curselection() or 0    )))
	entre_calcul.icursor(END)

def fenetre_aide() :
	global app_aide
	try :
		app_aide.state()
	except :
		app_aide = Tk()
		app_aide.title("Aide")

		frame_aide = Frame(app_aide,bg="light blue")
		frame_aide.pack(fill=BOTH,expand=1)

		texte_aide = Label(frame_aide,text=pavé_aide,bg="light blue")
		texte_aide.pack(side="left")

		app_aide.mainloop()

def fermer() :
	app.destroy()
	try :
		app_aide.destroy()
	except :
		return


# Liaisons des raccourcis claviers ----------------------------------------------------------------------

app.bind("<Return>",calculer)
app.bind("<Alt_R>",effacer)
app.bind("<Control_R>",repliquer)
app.bind("<Up>",lambda x:R1.invoke())
app.bind("<Down>",lambda x:R2.invoke())


# Historique ----------------------------------------------------------------------

historique_scroll = Scrollbar(main_frame)
historique_scroll.pack(side="left",fill=BOTH)

historique_liste = Listbox(main_frame,selectmode="single",yscrollcommand = historique_scroll.set)
historique_liste.pack(side="left")

historique_scroll.config(command = historique_liste.yview)


# Espace de calcul ----------------------------------------------------------------------

frame_calcul = Frame(main_frame)
frame_calcul.pack(side="left",fill=BOTH,expand=1)

entre_calcul = Entry(frame_calcul,textvariable=calcul)
entre_calcul.pack()

resultat_calcul = Label(frame_calcul,textvariable=resultat,font=(None,20)).pack()

R1 = Radiobutton(frame_calcul,text="écriture normal",variable=ecriture,value=1,command=calculer)
R1.select()
R1.pack()

R2 = Radiobutton(frame_calcul,text="écriture scientifique",variable=ecriture,value=2,command=calculer)
R2.select()
R2.pack()

R1.select()

rep = Button(frame_calcul,text="Rep",command=repliquer)
rep.place(x=10,y=10)

suppr = Button(frame_calcul,text="Suppr",command=lambda:historique_liste.delete(0,END))
suppr.place(x=10,y=40)

aide = Button(frame_calcul,text="Aide",command=fenetre_aide)
aide.place(x=270,y=10)


# Boutons principaux ----------------------------------------------------------------------

frame_bouton = Frame(main_frame)
frame_bouton.pack(side="right",fill=BOTH,expand=1)

bouton_calcul = Button(frame_bouton,text="=",command=calculer,bg="light green").pack(fill=BOTH)
bouton_effacer = Button(frame_bouton,text="Effacer",command=effacer,bg="light green").pack(fill=BOTH)
bouton_fermer = Button(frame_bouton,text="fermer",command=fermer,bg="red").pack(fill=BOTH,side="bottom")


# Fin de la compilation ----------------------------------------------------------------------

app.mainloop()