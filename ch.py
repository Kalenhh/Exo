#coding:utf-8
# Liste chainée

def open(liste) :
	return liste[1]

def longueur(chain) :

	if len(chain) == 0 :
		return 0

	longueur = 0
	while chain != None :
		longueur += 1
		chain = open(chain)

	return longueur
	

A = [14,[12,[9,None]]]
B = []
C = [3,None]

print("test longueur : ",longueur(A),longueur(B),longueur(C))	


def acceder(chain,i) :

	if len(chain) == 0 :
		return "Liste vide"

	if i > longueur(chain):
		return "index"	

	for o in range(i-1) :
		chain = open(chain)

	return chain[0]	

print("test acceder : ",acceder(A,1),acceder(B,1),acceder(C,1))
print("test acceder : ",acceder(A,2),acceder(B,2),acceder(C,2))
print("test acceder : ",acceder(A,3),acceder(B,3),acceder(C,3))

def ajouter(chain,element) :

	if len(chain) == 0 :
		return [element,None]

	seg = chain
	while seg[1] != None :
		seg = seg[1]

	seg[1] = [element,None]

	return chain

print("test ajouter : ",ajouter(A,5),ajouter(B,5),ajouter(C,5))

def inserer(chain,i,element) :

	if len(chain) == 0 and i != 0 :
		return "Index big"

	if i == 0 :
		return [element,chain]

	seg = chain
	for o in range(i) :
		seg=seg[1]

	try :
		a = seg[1]
	except:
		seg[1] = [element,None]
		return chain	

	seg[1] = [seg[0],seg[1] or None ]
	seg[0] = element
	
	return chain

print("test inserer : ",inserer(A,4,9))
