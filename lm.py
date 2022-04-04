#lm.py
#coding:utf-8

from tkinter import*
from math import*

app = Tk()
app.title("Calculatrice")
app.minsize(600,100)

main_frame = Frame(app,bg="yellow")
main_frame.pack(fill=BOTH,expand=1)

# ----------------------------------------------------------------------

calcul = StringVar()
resultat = IntVar()

# ----------------------------------------------------------------------

def calculer(e=0) :
	resultat.set(eval(calcul.get()))

def effacer() :
	calcul.set("")

def fermer() :
	app.destroy()	

# ----------------------------------------------------------------------

frame_calcul = Frame(main_frame)
frame_calcul.pack(side="left",fill=BOTH,expand=1)

entre_calcul = Entry(frame_calcul,textvariable=calcul).pack()
resultat_calcul = Label(frame_calcul,textvariable=resultat).pack()

app.bind("<Return>",calculer)

# ----------------------------------------------------------------------

frame_bouton = Frame(main_frame)
frame_bouton.pack(side="right",fill=BOTH,expand=1)

bouton_calcul = Button(frame_bouton,text="=",command=calculer).pack(fill=BOTH)
bouton_effacer = Button(frame_bouton,text="Effacer",command=effacer).pack(fill=BOTH)
bouton_fermer = Button(frame_bouton,text="fermer",command=fermer).pack(fill=BOTH,side="bottom")

app.mainloop()