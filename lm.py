#lm.py
#coding:utf-8

from tkinter import*
from math import*

app = Tk()
app.title("Calculatrice")
app.minsize(600,100)
app.maxsize(600,100)

main_frame = Frame(app,bg="yellow")
main_frame.pack(fill=BOTH,expand=1)

# ----------------------------------------------------------------------

calcul = StringVar()
resultat = StringVar()
ecriture = IntVar()

# ----------------------------------------------------------------------

def calculer(e=0) :
	try :
		eval(calcul.get())
	except :
		resultat.set("Calcul incorrecte")
		return

	resultat.set(str(eval(calcul.get())))

	if historique_liste.get(0) != resultat.get() :
		historique_liste.insert(0,resultat.get())

	historique_liste.selection_clear(0,END)
	historique_liste.selection_set(0)

	if ecriture.get() == 2 :	
		resultat.set(str(  format(float(eval(calcul.get())),".1E")  ))

def effacer(e=0) :
	calcul.set("")

def fermer() :
	app.destroy()	

def repliquer(e=0) :
	calcul.set(calcul.get()+str(historique_liste.get(   historique_liste.curselection() or 0    )))
	entre_calcul.icursor(END)

# ----------------------------------------------------------------------

historique_scroll = Scrollbar(main_frame)
historique_scroll.pack(side="left",fill=BOTH)

historique_liste = Listbox(main_frame,selectmode="single",yscrollcommand = historique_scroll.set)
historique_liste.pack(side="left")

historique_scroll.config(command = historique_liste.yview)

# ----------------------------------------------------------------------

frame_calcul = Frame(main_frame)
frame_calcul.pack(side="left",fill=BOTH,expand=1)

entre_calcul = Entry(frame_calcul,textvariable=calcul)
entre_calcul.pack()
resultat_calcul = Label(frame_calcul,textvariable=resultat).pack()

R1 = Radiobutton(frame_calcul,text="écriture normal",variable=ecriture,value=1,command=calculer)
R1.select()
R1.pack()

R2 = Radiobutton(frame_calcul,text="écriture scientifique",variable=ecriture,value=2,command=calculer)
R2.select()
R2.pack()

R1.select()

rep = Button(frame_calcul,text="Rep",command=repliquer)
rep.place(x=10,y=10)
# ----------------------------------------------------------------------

app.bind("<Return>",calculer)
app.bind("<Alt_R>",effacer)
app.bind("<Control_R>",repliquer)
app.bind("<Up>",lambda x:R1.invoke())
app.bind("<Down>",lambda x:R2.invoke())

# ----------------------------------------------------------------------

frame_bouton = Frame(main_frame)
frame_bouton.pack(side="right",fill=BOTH,expand=1)

bouton_calcul = Button(frame_bouton,text="=",command=calculer,bg="light green").pack(fill=BOTH)
bouton_effacer = Button(frame_bouton,text="Effacer",command=effacer,bg="light green").pack(fill=BOTH)
bouton_fermer = Button(frame_bouton,text="fermer",command=fermer,bg="red").pack(fill=BOTH,side="bottom")

app.mainloop()