#coding:utf-8
# Liste chainée

A = [14,[12,[9,None]]]
B = [None,None]
C = [3,None]
print(f"Liste :\t{A}\t{B}\t{C}")


def longueur(chain) :

	if chain == [] :
		return "Empty List E0"

	longueur = 0
	while chain != None and chain[0] is not None :
		longueur += 1
		chain = chain[1]

	return longueur

print(f"len\t{longueur(A)}\t{longueur(B)}\t{longueur(C)}")


def acceder(chain,i) :

	if chain == [] :
		return "Empty List E1"

	if i >= longueur(chain):
		return "Index I1"	

	for o in range(i) :
		chain = chain[1]

	return chain[0]

print(f"access\t{acceder(A,0)}\t{acceder(B,0)}\t{acceder(C,0)}")
print(f"access\t{acceder(A,1)}\t{acceder(B,1)}\t{acceder(C,1)}")
print(f"access\t{acceder(A,2)}\t{acceder(B,2)}\t{acceder(C,2)}")

print(f"Liste :\t{A}\t{B}\t{C}")


def ajouter(chain,element) :

	if len(chain) == 0 :
		print("Empty list E2")
		return

	seg = chain
	while seg[1] != None :
		seg = seg[1]

	seg[:] = [seg[0],[element,None]]

	if chain[0] is None :
		seg[:] = [element,None]

print("\nFonction ajouter :")
ajouter(A,"ajouter")
ajouter(B,"ajouter")
ajouter(C,"ajouter")
ajouter(A,"ajouter1")
ajouter(B,"ajouter1")
ajouter(C,"ajouter1")

print(f"Liste :\n{A}\n{B}\n{C}")


def inserer(chain,i,element) :

	if longueur(chain) <= i :
		return "Index I3"

	seg = chain
	for o in range(i) :
		seg=seg[1]

	seg[:] = [element,[seg[0],seg[1]]]

print("\nFonction inserer :")
inserer(A,0,"inser0")
inserer(B,0,"inser0")
inserer(C,0,"inser0")
inserer(A,2,"inser2")
inserer(B,2,"inser2")
inserer(C,2,"inser2")
inserer(A,4,"inser4")
inserer(B,4,"inser4")
inserer(C,4,"inser4")

print(f"Liste :\n{A}\n{B}\n{C}")


def supprimer_val(chain,element) :

	if chain == [] :
		print("Empty List E4")

	seg = chain
	while seg[0]!=element :
		seg = seg[1]

	if seg[1] is None :
		seg[:] = (None,)
		seg[:] =
		return
	seg[:] = seg[1]


print("\nFonction supprimer_val :")
supprimer_val(A,"inser0")
supprimer_val(B,"inser0")
supprimer_val(C,"inser0")
supprimer_val(A,"ajouter1")
supprimer_val(B,"ajouter1")
supprimer_val(C,"ajouter1")

print(f"Liste :\n{A}\n{B}\n{C}")



"""

def supprimer_ind(chain,i) :
	if len(chain) == 0 :
		print("vide")

	seg = chain
	for i in range(i) :
		seg = seg[1]

	seg[0:] = seg[1]
	return chain


def modifier(chain,i,element) :
	if len(chain) == 0:
		print("vide")

	seg = chain
	for i in range(i) :
		seg=seg[1]

	seg[0:] = [element,seg[1]]
	return chain


def vider(A) :
	A = [None,None]
	return A



from random import*
cara = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g",
		"h","j","k","l","m","w","x","c","v","b","n"]
def rec() :
	global cara
	print( 	cara[randint(0,len(cara))]   )
	rec()"""