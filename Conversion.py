#coding:utf-8

#déclaration de variable --------------------------------------------------------------------------------------------------------------------

input_principal = ""

#déclaration de fonction -------------------------------------------------------------------------------------------------------------------------

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

""" 'try_float(Valeur)' ,Si Valeur peut être converti en float retourne Vrai , sinon retourne Faux"""

def try_float(x) :
	try :
		x = float(x)
		return True
	except :
		return False	

""" 'information_conversion_kmh_ms()' ,Donne des informations sur 'conversion_kmh_ms()' """

def information_conversion_kmh_ms() :
	print("1. De km/h vers m/s \n2. De m/s vers km/h \nmenu. Afficher le menu \nexit. Quitter le programme \n")

""" 'conversion_kmh_ms(str)' ,Selon la variable d'entrée , propose un menu à plusieurs sortie possible"""

def conversion_kmh_ms(Choice) :
	
	if Choice == "1" :
				
		#convertir Vitesse en m/s

		Vitesse = input("Valeur en km/h : ")
		if try_float(Vitesse) == True :
			print(Vitesse,"km/h équivaut à ",round(convertir_kmh_ms(float(Vitesse)),3),"m/s.\n")
			return
		else :
			print("Rentrez une valeur numérique:\n")
			return
	
	if Choice == "2" :
				
		#convertir Vitesse en km/h
				
		Vitesse = input("Valeur en m/s :")
		if try_float(Vitesse) == True :
			print(Vitesse,"m/s équivaut à ",round(convertir_ms_kmh(float(Vitesse)),3),"km/h.\n")
			return
		else :
			print("Rentrez une valeur numérique:\n")
			return

	elif Choice.lower() == "menu" :
		information_conversion_kmh_ms()

	elif Choice.lower() == "exit" :
		print("-"*150)
		pass

	else :
		print("\nValeur non-valide , tapez 'menu' pour afficher les options\n") #erreur d'input

#programme principale ------------------------------------------------------------------------------------------------------------

print("Bienvenue\n")
information_conversion_kmh_ms()

while input_principal.lower() != "exit" :
	input_principal = input("=")
	conversion_kmh_ms(input_principal)