#coding:utf-8

#déclaration de variable

programme_ouvert = True
input_principal = str

#déclaration de fonction

""" 'convertir_ms_kmh(variable à convertir)' ,Convertis une variable(float/int) de m/s à km/h
Une variable d'entrée , une de sortie"""

def convertir_ms_kmh(v1) :
	v = v1 * 3.6
	return v

""" 'convertir_kmh_ms(variable à convertir)' ,Convertis une variable(float/int) de km/h à m/s 
Une variable d'entrée , une de sortie"""

def convertir_kmh_ms(v1) :
	v = v1 / 3.6
	return v

""" 'quit(variable booléenne servant de cadenas a la boucle)' ,permet de break une boucle selon la valeur d'une variable 
choisi"""

def comparaison(Comparé = "",Comparant = "") :
	if Comparé == Comparant :
		return False
	else :
		return True

""" 'information_menu_conversion_kmh_ms()' Donne des informations sur 'fonction_conversion_kmh_ms()"""

def information_menu_conversation_kmh_ms() :
	print("1. de km/h vers m/s\n2. de m/s vers km/h\n")


def fonction_conversion_kmh_ms(Choix,MotClé) :
	
	if Choix == "1" :
				
		#convertir Entré en m/s

		Entré = float(input("Valeur en km/h : "))
		print(Entré,"km/h équivaut à ",round(convertir_kmh_ms(Entré),3),"m/s.\n")

	if Choix == "2" :
				
		#convertir Entré en km/h
				
		Entré = float(input("Valeur en m/s :"))
		print(Entré,"m/s équivaut à ",round(convertir_ms_kmh(Entré),3),"km/h.\n")
			
	elif Choix == "menu" :
		information_menu_conversation_kmh_ms()

	elif Choix == MotClé :
		pass

	else :
		print("\nchoisir entre 1 et 2\n") #erreur d'input

#programme principale

print("Bienvenue\n")
information_menu_conversation_kmh_ms()

while comparaison(input_principal,"quit") == True :

	input_principal = input("=")
	fonction_conversion_kmh_ms(input_principal,"quit")