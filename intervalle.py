#coding:utf-8

Liste = [5,6,52,1,5,654,65]
print(Liste,len(Liste))

def destockage(A) :

	fin = []
	for i in range(len(A)) :
		if i %3 == 0 and (i+3) <= len(A) :
			print("     ",i)
			mini = A[i]

			for o in A[i:i+3] :
				print(o)

				if o < mini :
					mini = o

				fin.append(o)
			fin.remove(mini)
		
		elif i %3 == 0 and (i+3) > len(A) :
			fin.append(A[i])	

	return fin

# Pour avoir le meilleur prix -> avoir des trio haut et trio bas -> trier par valeur -> rangement


def trier(liste) :
	# Tri par insertion

	for i in range(len(liste)) : 	# i : index de debut
		inser = 0 					# inser : index ou l'on insere l'element d'index i

		while liste[i] > liste[inser] :	
			inser = inser+1 					

		liste.insert(inser,liste[i])	
		liste.pop(i+1)	
	return liste


print(destockage(trier(Liste)))

