#coding:utf-8

#Déclaration de variable ------------------------------------------------------------------------------------------------------------------------------

entré = ""
Bentré = ""
Bsortie = ""

#Déclaration de fonction --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#__________________________________________________________________

def ConvBinDec(nbin) :

	Nbase = str(n)
	Ndecimal = 0
	Nbits = len(Nbase)
	for i in range(Nbits) :
		Ndecimal = Ndecimal + Nbase[Nbits-1-i]*(2**i)											
	return Ndecimal

																		#Fonctions modèles non-utlisées 
def ConvDecBin(n) :

	Ndecimal = n
	Nbin = ""
	while Ndecimal != 0 :
		quotient = Ndecimal % 2
		Nbin = str(quotient) + Nbase
		Ndecimal = Ndecimal // 2
	return Nbin	

#___________________________________________________________________


"""Si value n'est pas un entier , retourne la valeur numérique correspondante à la valeur du caractère value dans la table ASCII ; Sers à convertir 1 valeur (entier/string) 
	en une valeur uniquement entière
"""

def ConvBaseSup(value) :
	try :
		value = int(value)
	except :
		value = ord(value) -65 + 10
		return value
	return value


"""Convertis un nombre nbase de base b en un nombre de base 10
"""

def ConvBaseDec(nbase,b) :

	Nbase = str(nbase)
	Ndecimal = 0
	Nbits = len(Nbase)
	for i in range(Nbits) :
		Ndecimal = Ndecimal + ConvBaseSup(Nbase[Nbits-1-i])*(int(b)**i)
	return Ndecimal


"""Convertis un nombre n de base 10 en un nombre de base b
"""

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


"""Verifie que chaque élément de nombre soit inclus dans la base b , retourne Faux si un des élément ne peut être transcris dans la base b.
"""

def NombreValide(nombre,b) :
	for i in nombre :
		if ord(i) -65 +10 >= int(b) or ord(i)-65 < 0 :
			return False
		try :
			int(i)
		except : 
			continue
		if int(i) >= int(b) :
			return False					
	return True	


"""Convertis un nombre nbase de base b1 en un nombre de meme valeur de base b2
"""

def ConvBaseBase(nbase,b1,b2) :
	valeur = ConvDecBase((ConvBaseDec(nbase,b1)),b2)
	return valeur


#Programme --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Programme-boucle convertisseur universel jusqu'à la base 36 

"""

print("Bienvenue\n")
while entré.lower() != "exit" and Bentré.lower() != "exit" and Bsortie.lower() != "exit" :

	entré = input("Valeur à convertir: ")
	if entré.lower() == "exit" :
		continue

	Bentré = input("Sur la base :")
	if Bentré.lower() == "exit" :
		continue
	try :
		int(Bentré)
	except :	
		print("error 2")
		continue

	if NombreValide(entré,Bentré) == False :
		print("error 1")
		continue

	Bsortie = input("Sur une base : ")
	if Bsortie.lower() == "exit" :
		continue
	try :
		int(Bsortie)
	except :
		print("error 2")
		continue		
		
	print(ConvBaseBase(entré,Bentré,Bsortie),"\n")