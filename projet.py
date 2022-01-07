#coding:utf-8

#Projet : Lecture et traitement de fichier CSV 

from csv import*

def ouverture(root) :

	with open(root,"r",encoding="utf-8") as fichier :
		lecteur = reader(fichier,delimiter=";")
		table = []
		for i in lecteur :
			table.append(i)

		return table

source = ouverture("nat2020.csv")
print("La liste est de",len(source),"ligne.\n")


def requete1(donné,prenom,année) :
	trouvé = False
	i=0
	while trouvé == False :

		if i == len(donné) :
			trouvé = True 
			return None
			continue

		if prenom == donné[i][1] and année == donné[i][2] :
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
			maxi = (i[2],best)
	if maxi == () :
		return None
	else :
		return maxi	
				



Lock = True

while Lock == True :

	print("pavé césar")

	choix = input("> ")

	if choix == "q" :
		Lock = False
		continue

	if choix == "1" :
		pre = input("Prénom :")
		ann = input("Année :")
		print(requete1(source,pre.upper(),ann))
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