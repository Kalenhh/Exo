#coding:utf-8

#Projet : Lecture et traitement de fichier CSV 

from csv import*


def ouverture(fichier) :

	with open(fichier,"r",encoding="utf-8") as donné :
		aaa = reader(donné,delimiter=";")
		table = []
		for i in aaa :
			table.append(i)

		return table

vued = ouverture("nat2020.csv")
print(len(vued),"c good")



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
	
	donnéG = [i for i in donné if i[0]=="1" if i[2]==année]
	donnéF = [i for i in donné if i[0]=="2" if i[2]==année]
	
	garcon =



	for i in donné :
		if i == 1
			if i2 == année
				if i > best :
					best = i

requete2(vued,"2005")


	

