#coding:utf-8

#Projet : Lecture et traitement de fichier CSV 

# Import :--------------------------------------------------------------------------------------------------------

from csv import*

# Fonctions :---------------------------------------------------------------------------------------------------

def ouverture(root) :

	with open(root,"r",encoding="utf-8") as fichier :
		lecteur = reader(fichier,delimiter=";")
		table = []
		for i in lecteur :
			table.append(i)

		return table


def requete1(donné,prenom,genre,année="XXXX") :
	trouvé = False
	i=0

	if genre == "m" :
		genre = "1"
	if genre == "f" :
		genre = "2"

	while trouvé == False :

		if i == len(donné) :
			trouvé = True
			return
			continue

		if prenom == donné[i][1] and année == donné[i][2] and genre == donné[i][0] :
			trouvé = True
			return donné[i][3]
			continue

		i = i + 1


def requete2(donné,année) :
	
	donnéG = [i for i in donné if i[0]=="1" if i[2]==année if i[1] != "_PRENOMS_RARES"]
	donnéF = [i for i in donné if i[0]=="2" if i[2]==année if i[1] != "_PRENOMS_RARES"]

	garcon = ()
	fille = ()

	best = 0
	for i in donnéG :
		if int(i[3]) > best :
			best = int(i[3])
			garcon = (i[1],best)

	best = 0
	for i in donnéF :
		if int(i[3]) > best :
			best = int(i[3])
			fille = (i[1],best)

	return garcon , fille


def requete3(donne,prenom) :

	maxi = ()
	best = 0
	for i in donne :
		if i[1] == prenom and int(i[3]) > best :
			best = int(i[3])
			maxi = (i[2],best,i[0])
	if maxi == () :
		return None
	else :
		return maxi	
				
def pavé() :
	print("╔═════════════════════════════════════════════════════════════════════════════════╗")
	print("║                        ▲♠▲            MENU DES TACHES.           ▲♠▲            ║")
	print("║                        ▲♠▲        Que voulez-vous faire ?        ▲♠▲            ║")
	print("╠═════════════════════════════════════════════════════════════════════════════════╣")
	print("║1 ► Nombre d'individus qui portent un prénom donné pour une année donnée. ˃      ║")
	print("║2 ► Prénoms les plus courant pour une année donnée. ˃                            ║")
	print("║3 ► Année qui correspond au maximum d'un prénom donné. ˃                         ║")
	print("║4 ► Afficher les options. ˃                                                      ║")
	print("║5 ► Quitter le programme. ˃                                                      ║")
	print("╚═════════════════════════════════════════════════════════════════════════════════╝\n")

# Programme :---------------------------------------------------------------------------------------

print("Hello world")

source = ouverture("nat2020.csv")
print("Fichier chargé :",len(source),"ligne.\n")
pavé()

Lock = True
while Lock == True :

	choix = input("> ")

	if choix == "5" :
		Lock = False
		continue

	if choix == "4" :
		pavé()
		continue	

	if choix == "1" :
		pre = input("Prénom :")
		ann = input("Année :")
		sexe = input("Prénom masculin ou féminin ,m/f :")

		if ann.isnumeric() == False :
			print(requete1(source,pre.upper(),sexe.lower),"sur toute la période.")
			continue
		else :
			print(requete1(source,pre.upper(),sexe.lower(),ann),"personnes ont été nommées",pre,"en",ann)
			continue

	if choix == "2" :
		anné = input("Année :")
		print(requete2(source,anné))
		continue

	if choix == "3" :
		pren = input("Prénom :")
		print(requete3(source,pren.upper()))
		continue

	else :
		print("Erreur")