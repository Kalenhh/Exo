#coding:utf-8
# Fonction intervalle de confiance



from math import sqrt

def inter(cara,n) :
	# cara 	= nombre d'échantillon possédant le caractère
	# n 	= taille total de l'échantillon

	freq = cara/n 	# Calcul de la fréquence
	print("La fréquence vaut : ",freq,"",freq*100,"%")

	### Partie calcul compliqué

	mid = sqrt(freq*(1-freq)/n)
	print(1.96*mid,"regtqerg")
	cal = (round(freq-1.96*mid,4),round(freq+1.96*mid,4))

	###

	print("Borne inférieur : ",cal[0],"\nBorne supérieur : ",cal[1])
	return cal

# Exemple
print(inter(100,200),"\n")

def pop(m,c,r) :
	# m : effectif de la population marqué lors de la 1ere capture
	# c : effectif de la populations capturé lors de la 2eme capture
	# r : effectif des individus marqués parmi c

	proportion = r/c # Pech

	echantillon = sqrt(		(proportion*(1-proportion))		/c)	# Sech

	cal = ( 	m/(proportion + 1.96*echantillon) , m/(proportion - 1.96*echantillon)	)

	return cal 

print(pop(34,52,26))


"""


def premier(n) :

	P = []
	for i in range(2,n+1) :
		if len(P) == 0 :
			P.append(i)
		else :
			prem = True 
			for k in P :
				if i % k == 0 :
					prem = False
			if prem == True :
				P.append(i)
	return P	
	
print(premier(100))			"""		
