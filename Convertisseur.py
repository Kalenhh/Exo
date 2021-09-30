#coding:utf-8

#Déclaration de variable---------------------------------------------------------------------------------------------------------------------------------------------------------------

input_principal = ""

#Déclaration de fonctions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Donne des informations sur les choix dans le programme"""

def information_programme() :
	print("1. Convertir des vitesses \n2. Convertir des bases \nMenu. Afficher les options \nExit. Quitter le programme \n")


""" 'try_float(Variable)' ,Si la variable peut être convertie en float retourne Vrai , sinon retourne Faux"""

def try_float(x) :
	try :
		x = float(x)
		return True
	except :
		return False	


""" 'try_int(Variable)' ,Si la variable peut être convertie en entier retourne Vrai , sinon retourne Faux"""

def try_int(x) :
	try :
		x = int(x)
		return True
	except :
		return False		

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

""" 'convertir_ms_kmh(float)' ,Convertis une variable de m/s à km/h
Une valeur d'entrée , une de sortie"""

def convertir_ms_kmh(v1) :
	v = v1 * 3.6
	return v


""" 'convertir_kmh_ms(float)' ,Convertis une variable de km/h à m/s 
Une valeur d'entrée , une de sortie"""																							

def convertir_kmh_ms(v1) :
	v = v1 / 3.6
	return v


""" 'information_conversion_kmh_ms()' ,Donne des informations sur 'conversion_vitesse()' """

def information_conversion_kmh_ms() :
	print("1. De km/h vers m/s \n2. De m/s vers km/h \nOption. Afficher les choix \nExit. Revenir au menu \n")								#Fonctions conversion de vitesse


""" 'conversion_kmh_ms()' ,Propose un menu à plusieurs sorties possibles pour convertir des vitesses entre km/h et m/s"""

def conversion_vitesse() :
	while True :
		Choice = input(">")
		if Choice == "1" :
					
			#convertir Vitesse en m/s

			Vitesse = input("Valeur en km/h : ")
			if try_float(Vitesse) == True :
				print(Vitesse,"km/h équivaut à ",round(convertir_kmh_ms(float(Vitesse)),3),"m/s.\n")
				continue
			else :
				print("Rentrez une valeur numérique:\n")
				continue
		

		if Choice == "2" :
					
			#convertir Vitesse en km/h
					
			Vitesse = input("Valeur en m/s :")
			if try_float(Vitesse) == True :
				print(Vitesse,"m/s équivaut à ",round(convertir_ms_kmh(float(Vitesse)),3),"km/h.\n")
				continue
			else :
				print("Rentrez une valeur numérique.\n")
				continue


		elif Choice.lower() == "option" :
			information_conversion_kmh_ms()
			continue


		elif Choice.lower() == "exit" :
			return


		else :
			print("\nValeur non-valide , tapez 'Option' pour afficher les options\n") #erreur d'input
			continue


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def lettre(x) :
	try :
		x = int(x)
	except :
		x = ord(x) -65 + 10
		return x
	return x	


def verification(x,y) :
	for i in x :
		if ord(i) -65 +10 >= int(y) :
			return False
		try :
			i = int(i)
		except :
					
	return True		



"""Transforme une base en decimal"""

def vers_base_10(Valeur,Base) :

	Nbase = str(Valeur)
	Ndecimal = 0
	Nbits = len(Nbase)
	for i in range(Nbits) :
		Ndecimal = Ndecimal + lettre(Nbase[Nbits-1-i])*(int(Base)**i)											#Fonctions conversion de nombre sous différentes bases
	return Ndecimal


"""Transforme une valeur en base 10 en une autre base"""

def depuis_base_10(Valeur,Base) :
	Ndecimal = Valeur
	Nbase = ""
	while Ndecimal != 0 :
		inter = Ndecimal % int(Base)
		if inter >= 10 :
			inter = chr(inter -10 +65)
		Nbase = str(inter) + Nbase
		Ndecimal = Ndecimal // int(Base)
	return Nbase


""" 'conversion_base()' ,Converti une valeur d'une base donnée à une autre base donnée .Se ferme si une Valeur autre que int est rentrée"""

def conversion_base() :
	while True :

		valeur_entrée = input("Valeur à convertir :")
		if valeur_entrée.lower() == "exit" :
			return

		base_entré = input("et sur la base:")
		if base_entré.lower() == "exit" :
			return
		if try_int(base_entré) == False :
			print("Rentrez une valeur entière\n")
			return
		if verification(valeur_entrée,base_entré) == False :
			print("error 1")
			return

		base_sorti = input("Convertir sur une base:")
		if base_sorti.lower() == "exit" :
			return
		if try_int(base_sorti) == False :
			print("Rentrez une valeur entière\n")
			return	

		valeur_sortie = depuis_base_10((vers_base_10(valeur_entrée,base_entré)),base_sorti)
		print(valeur_entrée,"base",base_entré,"égale",valeur_sortie,"base",base_sorti,"\n")
		continue


#Programme --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Propose un menu graphique pour sélectionner deux convertisseurs fonctionnels
"""

print("Bienvenue\n")
information_programme()

while input_principal.lower() != "exit" :
	input_principal = input("--->")
	
	if input_principal == "1" :

		information_conversion_kmh_ms()
		conversion_vitesse()
		continue
			

	if input_principal == "2" :
		
		conversion_base()
		continue


	elif input_principal.lower() == "exit" :
		print("-"*150)
		continue


	elif input_principal.lower() == "menu" :
		information_programme()
		continue	


	else :
		print("erreur d'input")
		continue