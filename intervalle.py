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
	cal = (round(freq-1.96*mid,4),round(freq+1.96*mid,4))

	###

	print("Borne inférieur : ",cal[0],"\nBorne supérieur : ",cal[1])
	return cal

# Exemple
print("Fréquence et Intervalle de confiance pour 135 caractère sur un échantillon de 400 :\n")
print(inter(135,400))