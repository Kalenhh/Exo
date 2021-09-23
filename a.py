#coding:utf-8

#déclaration de variable --------------------------------------------------------------------------------------------------------------------

input_principal = str

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

""" 'comparaison(variable 1,variable 2)' ,Si 1 = 2 ; retourne Vrai , sinon retourne Faux"""

def comparaison(Comparé,Comparant) :
	if Comparé == Comparant :
		return True
	else :
		return False

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
		print("\nchoisir entre 1 et 2\n") #erreur d'input

#programme principale ------------------------------------------------------------------------------------------------------------

print("Bienvenue\n")
information_conversion_kmh_ms()

while comparaison(input_principal,"exit") == False :
	input_principal = input("=")
	conversion_kmh_ms(input_principal)