#coding:utf-8

#déclaration de variable ------------------------------------------------------------------------------------------------

input_principal = str

#déclaration de fonction ---------------------------------------------------------------------------------------------

""" 'convertir_ms_kmh(float/int)' ,Convertis une variable de m/s à km/h
Une valeur d'entrée , une de sortie"""

def convertir_ms_kmh(v1) :
	v = v1 * 3.6
	return v

""" 'convertir_kmh_ms(float/int)' ,Convertis une variable de km/h à m/s 
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

"""
def try_float(x) :
	try :
		y = float(x)
		pass
	except :
		return "erreur d input"

		WIP--------------"""









""" 'information_conversion_kmh_ms()' ,Donne des informations sur 'conversion_kmh_ms()' """

def information_conversion_kmh_ms() :
	print("1. de km/h vers m/s\n2. de m/s vers km/h\n")

""" 'conversion_kmh_ms(str)' ,Selon la variable d'entrée , propose un menu à plusieurs sortie possible"""

def conversion_kmh_ms(Choice) :
	
	if Choice == "1" :
				
		#convertir Vitesse en m/s

		Vitesse = float(input("Valeur en km/h : "))
		print(Vitesse,"km/h équivaut à ",round(convertir_kmh_ms(Vitesse),3),"m/s.\n")

	if Choice == "2" :
				
		#convertir Vitesse en km/h
				
		Vitesse = input("Valeur en m/s :")
		print(try_float(Vitesse) or Vitesse,"m/s équivaut à ",round(convertir_ms_kmh(float(Vitesse)),3),"km/h.\n") #WIP--------------
			
	elif Choice == "menu" :
		information_conversion_kmh_ms()

	elif Choice == "exit" :
		pass

	else :
		print("\nchoisir entre 1 et 2\n") #erreur d'input

#programme principale ------------------------------------------------------------------------------------------------------------

print("Bienvenue\n")
information_conversion_kmh_ms()

while comparaison(input_principal,"exit") == False :
	input_principal = input("=")
	conversion_kmh_ms(input_principal)