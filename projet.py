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
print(vued)

def requete1(donné,prenom,année) :
	trouvé = False
	while trouvé == False :
		for i in donné :
			if prenom == i[1] and année == i[2] :
				trouvé = True
				return i[3]
				continue

