#coding:utf-8

from tkinter import*
from random import*
from time import*

#-------------------------------------------------------------------------------------------------------------

root = Tk()
root.minsize(400,300)
main_frame = Frame(root,bg="blue")			#Menu Graphique
main_frame.pack(fill=BOTH,expand=1)

def make_button(name,text,cmd) :

	name = Button(main_frame,text=text,command=cmd)
	name.pack(fill=BOTH)

#-------------------------------------------------------------------------------------------------------------

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

	for i in range(11) :					#Formule A pour x = [0,10] dans une liste
		liste.append(formula(i))
		print(liste)

make_button("b2","deux",deux)


def trois() :
	print("\nexo n°3")
	name = input("nom et prenom plz : ")
	liste = name.split(" ")
	ini = (liste[1])[0] + (liste[0])[0]		#Initiales
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
	print("1ère methode : ",liste)				#Constructions de liste à pattern

	C = 1
	res = []
	liste = []
	while len(liste) < int(n)  :
		res.append(C)
		for e in res :
			liste.append(e)
		C = C + 1


	del liste[int(n):]
	print("\n2eme methode : ",liste)
	print(len(liste))


make_button("b4","quatre",quatre)


def cinq() :
	print("\nexo n°5")
	chaine1 = "abc"
	chaine2 = "de"
	"""['ad','ae','bd','be','cd','ce']"""

	liste = []
	for i in chaine1 :
		for o in chaine2 :								#Décomposition de caractère de chaines en liste
			liste.append(i+o)
	print("Par iteration : ",liste)
	
	liste = []
	liste = [i+o for i in chaine1 for o in chaine2]		
	print("Par comprehension : ",liste)

make_button("b5","cinq",cinq)


def six() :
	print("\nexo n°6")

	def premier(n) :										#Trouver tout les premiers en dessous ou egaux à n
		liste = list(range(1,n+1))
		print(liste)
		for i in range(n) : #i = tt les nombre a tester pour voir si ils sont premier
			for o in range(2,i) : # test de tous les diviseur possible
				if i%o == 0 and o <= i ** 0.5 and i in liste :
					
					liste.remove(i)				
		print(liste)			
	premier(31)	

make_button("b6","six",six)


def sept() :
	print("\nexo n°7")

	def compte_lettres(mot) :				#Trouver les occurences de chaques lettres d'un mot
		dico = {}
		for i in mot :
			dico[i] = mot.count(i)
		print(dico)	

	mot = input("Mot plz : ")
	compte_lettres(mot)	

make_button("b7","sept",sept)


def huit() :
	print("\nexo n°8")
	dico = {"A":1,"E":1,"I":1,"L":1,"N":1,"O":1,"R":1,"S":1,"T":1,"U":1,"D":2,"G":2,"M":2,"B":3,"C":3,"P":3,"F":4,"H":4,"V":4,"J":8,"Q":8,"K":10,"W":10,"X":10,"Y":10,"Z":10}

	def compte_points(mot) :
		C = 0
		for i in mot :
			p = i.upper()
			C = C + int(dico[p])				#Compter la valeur d'un mot à partir d'un dico

		print("voila",C)

	mot = input("mot plz : ")
	compte_points(mot)
	
make_button("b8","huit",huit)


def neuf() :
	print("\nexo n°9")

	elements = {"Au":{"Te":2970,"Tf":1063,"Z":79,"M":196.967},"Ga":{"Te":2237,"Tf":29.8,"Z":31,"M":69.72}}

	print(elements)
	print(elements["Au"]["Z"])					#Construire un dico contenant des dicos

make_button("b9","neuf",neuf)


def dix() :
	print("\nexo n°10")

	dico = {(48.85358,2.30149):"Paris",
			(11.61135,43.14775):"Djibouti",
			(37.02311,-8.99660):"Fortaleza",
			(7.67798,-5.02538):"Bouaké"}		#Utilisation de coordonnées GPS 

	def ville_pos(pos1,pos2) :
		print(dico[(pos1,pos2)])

	ville_pos(37.02311,-8.99660)

make_button("b10","dix",dix)	


def onze() :
	print("\nexo n°11")					#Comparer la rapidité de recherche entre une liste et un dico

	def recherche_liste(liste,k) :
		for i in liste :		
			if i[0] == k :
				return i[1]

	def recherche_dico(dico,k) :
		return dico[k]

	liste = [[i,i] for i in range(0,10**6-1)]
	shuffle(liste)
	dico = dict(liste)

	sec_dep = time()
	for i in range(0,50) :
		print(recherche_liste(liste,i))
	sec_fin = time()
	print("temps dans la liste : ",sec_fin-sec_dep)	


	sec_dep = time()
	for i in range(0,50) :
		print(recherche_dico(dico,i))
	sec_fin = time()
	print("temps dans le dico : ",sec_fin-sec_dep)	

make_button("b11","onze",onze)


#-------------------------------------------------------------------------------------------------------------

root.mainloop()