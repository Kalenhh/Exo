#vide.py

def est_entier(n):
	if abs(n-int(n))>0.5:	# cas si n=x.99999999
		decimal=abs(n-int(n+1))*100000	# partie decimal
	else:					# cas si n=x.000000001
		decimal=abs(n-int(n))*100000	# partie decimal
	if decimal<1:
		return True
	else:
		return False

def verifier(op,a,b) :
	"""
	Verifie que le résultat de l'opération est positif et entier
	"""

	assert op in ["+","-","*","/","**"]
	assert a, b == int

	res = eval(str(a)+op+str(b))

	if est_entier(res) == True and abs(res) == res : #Verifie que res est entier + positif
		return True
	else:
		return False

print(verifier("-",8,8),verifier("/",4,3))

def test():
	paquet = [("-",8,8),("/",4,3),("*",8,9),("**",-4,9)]
	for i in paquet :
		print(i)
		assert verifier(i[0],i[1],i[2]) in [True,False]
		print(verifier(i[0],i[1],i[2]))

test()