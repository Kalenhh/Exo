#coding:utf-8
# Liste chainée

def longueur(chain) :

	if chain == [] :
		return "Empty List E0"

	longueur = 0
	while chain != None :
		longueur += 1
		chain = chain[1]

	return longueur
	

A = [14,[12,[9,None]]]
B = []
C = [3,None]
print(A,B,C)

"""
print("test longueur : ",longueur(A),longueur(B),longueur(C))	"""


def acceder(chain,i) :

	if chain == [] :
		return "Empty List E1"

	if i > longueur(chain):
		return "Index I1"	

	for o in range(i-1) :
		chain = chain[1]

	return chain[0]
"""
print("test acceder : ",acceder(A,1),acceder(B,1),acceder(C,1))
print("test acceder : ",acceder(A,2),acceder(B,2),acceder(C,2))
print("test acceder : ",acceder(A,3),acceder(B,3),acceder(C,3))"""

def ajouter(chain,element) :

	if len(chain) == 0 :
		chain = [element,None]
		return chain

	seg = chain
	while seg[1] != None :
		seg = seg[1]

	seg[1] = [element,None]
	return chain



print("test ajouter : ",ajouter(A,5),ajouter(B,5),ajouter(C,5))

def inserer(chain,i,element) :

	if longueur(chain) < i :
		return "Index big"

	if i == 0 :
		chain = [element,chain]
		return chain

	seg = chain
	for o in range(i) :
		seg=seg[1]

	if seg is None :
		chain = ajouter(chain,element)
		return chain

	seg[1] = [seg[0],seg[1]]
	seg[0] = element
	
	return chain

print("test inserer : ",inserer(A,0,9))

def supprimer_val(chain,element) :

	if len(chain) == 0 :
		print("Vide")

	seg = chain
	while seg[0]!=element :
		seg = seg[1]

	seg[0:] = seg[1]
	return chain

print("test supp",supprimer_val(A,14))


from random import*
cara = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g",
		"h","j","k","l","m","w","x","c","v","b","n"]
def rec() :
	global cara
	print( 	cara[randint(0,len(cara))]   )
	rec()

