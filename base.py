#coding:utf-8

#Déclaration de variable---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Fonctions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Transforme une base en decimal"""

def to10(Valeur,Base) :

	Nbase = str(Valeur)
	Ndecimal = 0
	Nbits = len(Nbase)
	for i in range(Nbits) :
		Ndecimal = Ndecimal + int(Nbase[Nbits-1-i])*(Base**i)
	return Ndecimal

def from10(Valeur,Base) :
	Ndecimal = str(Valeur)
	Nbase = ""
	while Ndecimal != 0 :
		Nbase =  Nbase + str(Ndecimal % Base)
		Ndecimal = (Ndecimal-(Ndecimal % Base)) / Base 

	return Nbase	




#Programme --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


print("Binevenu\n")
"""
while input_principal != "exit" :
"""

a = from10(13,2)

print(a)










