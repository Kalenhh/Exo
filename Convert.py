#coding:utf-8

#Déclaration de variable ------------------------------------------------------------------------------------------------------------------------------

entré = ""
Bentré = ""
Bsortie = ""

#Déclaration de fonction --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	
def ConvBinDec(nbin) :

	Nbase = str(n)
	Ndecimal = 0
	Nbits = len(Nbase)
	for i in range(Nbits) :
		Ndecimal = Ndecimal + Nbase[Nbits-1-i]*(2**i)											
	return Ndecimal


def ConvDecBin(n) :

	Ndecimal = n
	Nbin = ""
	while Ndecimal != 0 :
		quotient = Ndecimal % 2
		Nbin = str(quotient) + Nbase
		Ndecimal = Ndecimal // 2
	return Nbin	


def ConvBaseSup(x) :
	try :
		x = int(x)
	except :
		x = ord(x) -65 + 10
		return x
	return x

"""Transforme une base en decimal"""

def ConvBaseDec(nbase,b) :

	Nbase = str(nbase)
	Ndecimal = 0
	Nbits = len(Nbase)
	for i in range(Nbits) :
		Ndecimal = Ndecimal + ConvBaseSup(Nbase[Nbits-1-i])*(int(b)**i)											#Fonctions conversion de nombre sous différentes bases
	return Ndecimal

def ConvDecBase(n,b) :
	Ndecimal = n
	Nbase = ""
	while Ndecimal != 0 :
		quotient = Ndecimal % int(b)
		if quotient >= 10 :
			quotient = chr(quotient -10 +65)
		Nbase = str(quotient) + Nbase
		Ndecimal = Ndecimal // int(b)
	return Nbase

def NombreValide(nombre,b) :
	for i in nombre :
		if ord(i) -65 +10 >= int(b) :
			return False
		try :
			int(i)
		except : 
			continue
		if int(i) >= int(b) :
			return False					
	return True	
	
def ConvBaseBase(nbase,b1,b2) :
	valeur = ConvDecBase((ConvBaseDec(nbase,b1)),b2)
	return valeur

#Programme --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Bienvenu\n")
while entré or Bentré or Bsortie != "exit" :

	entré = input("Valeur à convertir: ")
	if entré == "exit" :
		continue
	Bentré = input("Sur la base :")

	if Bentré == "exit" :
		continue
	if NombreValide(entré,Bentré) == False :
		print("error 1")
		continue

	Bsortie = input("Sur une base : ")

	if Bsortie == "exit" :
		continue
		
	print(ConvBaseBase(entré,Bentré,Bsortie),"\n")