#coding:utf-8

#Déclaration de variable ------------------------------------------------------------------------------------------------------------------------------

entré = ""
Bentré = ""
Bsortie = ""

#Déclaration de fonction --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#__________________________________________________________________

def ConvBinDec(nbin) :
	"""Convertis un nombre binaire en décimal
	"""

	Nbase = str(n)
	Ndecimal = 0
	Nbits = len(Nbase)
	for i in range(Nbits) :
		Ndecimal = Ndecimal + Nbase[Nbits-1-i]*(2**i)
	return Ndecimal

																		#Fonctions modèles non-utlisées 
def ConvDecBin(n) :
	"""Convertis un nombre décimal en binaire
	"""

	Ndecimal = n
	Nbin = ""
	while Ndecimal != 0 :
		quotient = Ndecimal % 2
		Nbin = str(quotient) + Nbase
		Ndecimal = Ndecimal // 2
	return Nbin

#___________________________________________________________________

def ConvBaseSup(value) :
	"""Si 'value' n'est pas un entier , retourne la valeur numérique correspondante à la valeur du caractère 'value'
	dans la table ASCII -65 +10 ; Sers à convertir 1 valeur (entier/string) en une valeur uniquement entière.
	ex:  value =A   return =10
				B 			11
				F 			15
	"""

	try :
		value = int(value)
	except :
		value = ord(value) -65 + 10
		return value
	return value

def ConvBaseDec(nbase,b) :
	"""Convertis un nombre nbase de base b en un nombre decimal.
	"""

	Nbase = str(nbase)
	Ndecimal = 0
	Nbits = len(Nbase)
	for i in range(Nbits) :
		Ndecimal = Ndecimal + ConvBaseSup(Nbase[Nbits-1-i])*(int(b)**i)
	return Ndecimal


def ConvDecBase(n,b) :
	"""Convertis un nombre n décimal en un nombre de base b
	"""

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
	"""Vérifie que chaque élément de nombre soit inclus dans la base b , retourne Faux si un des élément ne peut être transcris dans la base b.
	"""

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
	"""Convertis un nombre nbase de base b1 en un nombre de même valeur de base b2.
	"""

	valeur = ConvDecBase((ConvBaseDec(nbase,b1)),b2)
	return valeur


#Programme --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Convertisseur universel de valeur jusqu'à la base 36
"""

print("Bienvenue\n")
while entré.lower() != "exit" and Bentré.lower() != "exit" and Bsortie.lower() != "exit" :

	entré = input("Valeur à convertir: ")	#prend la valeur à convertir
	if entré.lower() == "exit" :
		continue

	Bentré = input("Sur la base :")			#Prend la base du nombre à convertir
	if Bentré.lower() == "exit" :
		continue

	try :													#test si la base est un entier
		int(Bentré)
	except :
		print("Erreur : entrez une valeur entière\n")
		continue

	if NombreValide(entré,Bentré) == False :		#test si la valeur est correcte dans la base donnée
		print("Cette valeur n'existe pas.\n")
		continue

	Bsortie = input("Sur une base : ")		#Prend la base dans laquelle convertir la valeur
	if Bsortie.lower() == "exit" :
		continue

	try :													#test si la base est un entier
		int(Bsortie)
	except :
		print("Erreur : entrez une valeur entière\n")
		continue

	print(ConvBaseBase(entré,Bentré,Bsortie),"\n")