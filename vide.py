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
	assert type(a + b) == int

	res = eval(str(a)+op+str(b))

	if est_entier(res) == True and abs(res) == res : #Verifie que res est entier + positif
		return True
	else:
		return False


def test():
	paquet = [("-",8,7),("/",4,3),("*",8,9),("**",-4,9)]
	for i in paquet :
		print(i)
		print(verifier(i[0],i[1],i[2]))


def occurence(valeur,liste) :
	"""
	Trouve les occurences d'une valeur dans une liste
	"""

	assert len(liste) > 0

	position = []

	for i in range(len(liste)) :
		if valeur == liste[i] :
			position.append(i)
	return position

port = [3,4,5,6,7,8,9,4,3,1]
print(occurence(3,port))


def extremum(liste) :
	"""
	Trouve les extremes dans une liste et leurs occurences
	"""

	assert len(liste) > 0

	maxi = liste[0]
	position_maxi = []

	mini = liste[0]
	position_mini = []

	for i in range(len(liste)) :

		if liste[i] == mini :		#Occurence de mini		
			position_mini.append(i)

		if liste[i] == maxi :		#Occurence de maxi
			position_maxi.append(i)

		if liste[i] > maxi : 		#Trouver le maximum
			maxi = liste[i]
			position_maxi = [i]

		if liste[i] < mini :		#Trouver le minimum
			mini = liste[i]
			position_mini = [i]

	return (maxi,position_maxi) , (mini,position_mini)

port = [i*o for i in range(-10,20) for o in range(-10,20)]
print(extremum(port),len(port),port)