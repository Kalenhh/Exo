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
		resultat.set("Le calcul n'est pas correcte")
		return
	
	if ecriture.get() == 2 :	
		resultat.set(str(  format(float(eval(calcul.get())),".1E")  ))
		return
	resultat.set(set(eval(calcul.get())))	

def effacer(e=0) :
	calcul.set("")

def fermer() :
	app.destroy()	

def key_pressed(event):
	print(event.char)
	w=Label(frame_calcul,text="Key Pressed:"+event.char)
	w.place(x=10,y=50)

# ----------------------------------------------------------------------

frame_calcul = Frame(main_frame)
frame_calcul.pack(side="left",fill=BOTH,expand=1)

entre_calcul = Entry(frame_calcul,textvariable=calcul).pack()
resultat_calcul = Label(frame_calcul,textvariable=resultat).pack()

R1 = Radiobutton(frame_calcul,text="écriture normal",variable=ecriture,value=1).pack()
R2 = Radiobutton(frame_calcul,text="écriture scientifique",variable=ecriture,value=2).pack()


app.bind("<Return>",calculer)
app.bind("<Alt_R>",effacer)
app.bind("<Key>",key_pressed)

# ----------------------------------------------------------------------

frame_bouton = Frame(main_frame)
frame_bouton.pack(side="right",fill=BOTH,expand=1)

bouton_calcul = Button(frame_bouton,text="=",command=calculer,bg="light green").pack(fill=BOTH)
bouton_effacer = Button(frame_bouton,text="Effacer",command=effacer,bg="light green").pack(fill=BOTH)
bouton_fermer = Button(frame_bouton,text="fermer",command=fermer,bg="red").pack(fill=BOTH,side="bottom")

app.mainloop()