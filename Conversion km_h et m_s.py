#coding:utf-8

#déclaration de variable

programme_ouvert = True

#déclaration de fonction

""" 'in_kmh()' ,Convertis une variable(float/int) de m/s à km/h
Une variable d'entrée , une de sortie"""

def convertir_ms_kmh(v1) :
	v = v1 * 3.6
	return v

""" 'in_ms()' ,Convertis une variable(float/int) de km/h à m/s 
Une variable d'entrée , une de sortie"""

def convertir_kmh_ms(v1) :
	v = v1 / 3.6
	return v

def information_menu() :
	print("1. de km/h vers m/s\n2. de m/s vers km/h\n")

def fonction_conversion_kmh_ms(Choix,FinProgramme) :
	if Choix == "1" :
			
		#convertir Entré en m/s

		Entré = float(input("Valeur en km/h : "))
		print(Entré,"km/h équivaut à ",round(convertir_kmh_ms(Entré),3),"m/s.\n")

	if Choix == "2" :
			
		#convertir Entré en km/h
			
		Entré = float(input("Valeur en m/s :"))
		print(Entré,"m/s équivaut à ",round(convertir_ms_kmh(Entré),3),"km/h.\n")
		
	elif Choix == "quit" :	#commande de sortie
		FinProgramme = False
		return FinProgramme
		
	elif Choix == "menu" :
		information_menu()

	else :
		print("\nchoisir entre 1 et 2\n") #erreur d'input

#programme principale

print("Bienvenue\n")
information_menu()
while programme_ouvert == True :

	choix_menu = input("=")
	fonction_conversion_kmh_ms(choix_menu,programme_ouvert)
	print(programme_ouvert)











"""test github"""	