#coding:utf-8

from tkinter import*


root = Tk()
root.minsize(400,300)
main_frame = Frame(root,bg="blue")
main_frame.pack(fill=BOTH,expand=1)


def make_button(name,text,cmd) :

	name = Button(main_frame,text=text,command=cmd)
	name.pack(fill=BOTH)


def un() :

	print("\nexo n°1")
	liste = [45,17,89,38,10,74]
	print(f"La liste est :{liste}")
	liste.sort()
	print(f"La liste triée est :{liste}")	
	liste.append(12)
	print(f"La liste + 12 est :{liste}")
	liste.reverse()	
	print(f"La liste reversed est :{liste}")
	print(f"L'index de 10 est :{liste.index(10)}")
	del liste[liste.index(38)]
	print(f"La liste -38 est :{liste}")
	print(f"La liste de 2 a 3 est :{liste[1:3]}")
	print(f"La liste de 1 a 2 est :{liste[0:2]}")
	print(f"La liste a partir de 3 est :{liste[2:]}")
	print(f"Le dernier element est :{liste[-1]}")

make_button("b1","un",un)


def deux() :
	print("\nexo n°2")
	liste = []
	def formula(n) :
		A = (n**2)-2*n+3
		return A

	for i in range(11) :
		liste.append(formula(i))
		print(liste)

make_button("b2","deux",deux)


def trois() :
	print("\nexo n°3")
	name = input("nom et prenom plz : ")
	liste = name.split(" ")
	ini = (liste[1])[0] + (liste[0])[0]
	ini = ini.upper()
	print(f"Les initiales sont : {ini}")

make_button("b3","trois",trois)

def quatre() :
	print("\nexo n°4")
	n = input("taille de la chaine : ")
	liste = []
	compteur = 1
	for i in range(int(n)) :
		liste.append(1)
		liste.append(compteur)
		compteur = compteur + 1
	print(liste)	

make_button("b4","quatre",quatre)

root.mainloop()



"""
nom = input("nom >")
prenom = input("prenom >")
initiales = prenom[0] + nom[0]
initiales = initiales.upper()

print(f"Votre nom est {nom}\nVotre prénom est {prenom}\nVos initiales sont {initiales}")
"""