#coding:utf-8

# Exercice 1

def moyenne(liste) :

	if len(liste) == 0 :
		return "Erreur"

	somme = 0
	for i in liste :
		somme += i

		print(somme)

	return somme/len(liste)

liste1 = [5,3,8]
liste2 = [1,2,3,4,5,6,7,8,9,10]
liste3 = []

print(moyenne(liste1),moyenne(liste2),moyenne(liste3))

def trie(liste) : 

	if len(liste) == 0 :
		return "Erreur"

	index = [0,len(liste)]

	while index[1]-index[0] != 0 :

		if liste[index[0]] == 0 :
			index[0] += 1

		else :
			liste.insert(index[1],liste[index[0]])
			liste.pop(index[0])
			index[1] -= 1

	return liste
	
print(trie([0,1,0,1,0,0,0,1,0,1,1,1,0,1]))		


