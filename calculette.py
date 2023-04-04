#coding:utf-8

# Calculette pour faire des calculs au lieu d'aller sur google

from tkinter import*
from math import*


# Fenetre principal ----------------------------------------------------------------------

app = Tk()
app.title("Calculatrice")
app.minsize(700,120)
app.maxsize(700,120)

main_frame = Frame(app,bg="yellow")								#On crée la fenetre et la Frame principal
main_frame.pack(fill=BOTH,expand=1)


# Variables ----------------------------------------------------------------------

calcul = StringVar()		# Le texte entré par l'utilisateur
resultat = StringVar()		# Le texte affichant le résultat du calcul
ecriture = IntVar()			# Le mode d'écriture du resultat : =1 si ecriture normal , =2 si ecriture scientifique

pavé_aide = str("Bouton Rep : Copie la valeur selectionnée dans l'historique \nRaccourci : Ctrl droite \n"		# Le texte affiché dans la fenetre auxiliaire
				"\n Bouton Effacer : Efface le calcul \nRaccourci : Alt droite \n"
				"\nBouton Suppr : Supprime l'historique")


# Fonctions ----------------------------------------------------------------------

def calculer(e=0) :								# Calcul le resultat de l'expression contenue dans 'calcul' et l'associe a 'resultat' grace a la fonction eval()
	try :
		eval(calcul.get())									# Test si l'expression est interpretable , sinon , affiche 'Incorrecte'
	except :
		resultat.set("Incorrecte")
		return

	resultat.set(str(round(  eval(calcul.get()),4   )))			# Fais le calcul et affiche le resultat

	if historique_liste.get(0) != resultat.get() :
		historique_liste.insert(0,resultat.get())			# Si la valeur obtenu est differente de la derniere valeur de l'historique , l'insers dans la liste

	historique_liste.selection_clear(0,END)					# Nettoye la selection et selectionne le dernier element de la liste
	historique_liste.selection_set(0)

	if ecriture.get() == 2 :									# Si l'écriture demandée est scientifique ,formate le resultat
		resultat.set(str(  format(float(resultat.get()),".1E")  ))

	if len(resultat.get()) > 9 :							# Si le resultat est trop grand , formate automatiquement le resultat en écriture scientifique
		R2.invoke()

def effacer(e=0) :								# Efface l'expression contenue la zone de calcul
	calcul.set("")

def repliquer(e=0) :							# Prend la valeur selectionné dans l'historique et l'insere dans la zone de calcul
	calcul.set(calcul.get()+str(historique_liste.get(   historique_liste.curselection() or 0    )))
	entre_calcul.icursor(END)

def fenetre_aide() :							# Ouvre une fenetre auxiliaire qui indique le fonctionnement de la calculatrice
	global app_aide
	try :
		app_aide.state()						# Si la fenetre n'existe pas, on la crée
	except :
		app_aide = Tk()
		app_aide.title("Aide")

		frame_aide = Frame(app_aide,bg="light blue")
		frame_aide.pack(fill=BOTH,expand=1)

		texte_aide = Label(frame_aide,text=pavé_aide,bg="light blue")		# On affiche 'pavé_aide'
		texte_aide.pack(side="left")

		app_aide.mainloop()

def fermer() :									# Ferme les fenetres ouverte
	app.destroy()
	try :
		app_aide.destroy()
	except :
		return


# Liaisons des raccourcis claviers ----------------------------------------------------------------------

app.bind("<Return>",calculer)					# Touche entré pour calculer
app.bind("<Alt_R>",effacer)						# Touche Alt droit pour effacer
app.bind("<Control_R>",repliquer)				# Touche Control droit pour repliquer
app.bind("<Up>",lambda x:R1.invoke())			# Touche flèche haut pour invoquer le bouton radio ecriture normal
app.bind("<Down>",lambda x:R2.invoke())			# Touche flèche bas pour invoquer le bouton radio ecriture scientifique


# Historique ----------------------------------------------------------------------    # On commence à construire les objets contenus dans la calculatrice

historique_scroll = Scrollbar(main_frame)
historique_scroll.pack(side="left",fill=BOTH)

historique_liste = Listbox(main_frame,selectmode="single",yscrollcommand = historique_scroll.set)  	########
historique_liste.pack(side="left")																	# On associe la barre de défilement avec la liste 

historique_scroll.config(command = historique_liste.yview)											########


# Espace de calcul ----------------------------------------------------------------------

frame_calcul = Frame(main_frame)
frame_calcul.pack(side="left",fill=BOTH,expand=1)

entre_calcul = Entry(frame_calcul,textvariable=calcul)												# Zone de calcul
entre_calcul.pack()

resultat_calcul = Label(frame_calcul,textvariable=resultat,font=(None,20)).pack()					# Zone de résultat

R1 = Radiobutton(frame_calcul,text="écriture normal",variable=ecriture,value=1,command=calculer)	# Bouton écriture normal
R1.select()
R1.pack()

R2 = Radiobutton(frame_calcul,text="écriture scientifique",variable=ecriture,value=2,command=calculer)	# Bouton écriture scientifique
R2.select()
R2.pack()

R1.select()				# On selectionne par défaut le premier radio bouton

rep = Button(frame_calcul,text="Rep",command=repliquer)												# Bouton répliquer
rep.place(x=10,y=10)

suppr = Button(frame_calcul,text="Suppr",command=lambda:historique_liste.delete(0,END))				# Bouton supprimer ; sers à supprimer toutes les valeurs contenus dans l'historique
suppr.place(x=10,y=40)

aide = Button(frame_calcul,text="Aide",command=fenetre_aide)										# Bouton aide ; ouvre la fenetre d'aide
aide.place(x=270,y=10)


# Boutons principaux ----------------------------------------------------------------------

frame_bouton = Frame(main_frame)
frame_bouton.pack(side="right",fill=BOTH,expand=1)

bouton_calcul = Button(frame_bouton,text="=",command=calculer,bg="light green").pack(fill=BOTH)				# Bouton calculer
bouton_effacer = Button(frame_bouton,text="Effacer",command=effacer,bg="light green").pack(fill=BOTH)		# Bouton effacer
bouton_fermer = Button(frame_bouton,text="fermer",command=fermer,bg="red").pack(fill=BOTH,side="bottom")	# Bouton fermer


# Fin de la compilation ----------------------------------------------------------------------

app.mainloop()			# On lance le programme