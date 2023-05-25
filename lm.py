#coding:utf-8

with open('livre.txt','r',encoding='utf-8') as root :
	texte = root.read()

def naive(texte,motif) :

	n = len(texte)
	p = len(motif)
	i, j = 0, 0 

	occurence = bool(True)
	position = list([])

	for i in range(n-p) :
		occurence = True 
		j = 0

		while occurence == True and j < p :
			if motif[j] != texte[i+j] :
				occurence = False

			j += 1

		if occurence == True :
			position.append(i)

	return position


def horse(texte,motif) :

	n = len(texte)
	p = len(motif)

	i, j = 0, 0

	occurence = True 
	position = []

	while i <= n-p :
		occurence = True 
		j = p-1

		while occurence == True and j >= 0 :

			if motif[j] != texte[i+j] :
				occurence = False
				if texte[i+j] not in motif :
					i = i+j+1

				else :
					i = i+p-j

			else :
				j = j-1

		if occurence == True :
			position.append(i)
			i = i + p 

	return position


def boyer(texte,motif):

	n = len(texte)
	p = len(motif)
	positions = []
	position_adroite = {}

	for k in range(len(motif)):
		position_adroite[motif[k]]=k
	i=0
	
	while i<n-p:
		occurrence=True
		# parcours fenêtre texte de droite à gauche
		j=p-1
		while occurrence==True and j>=0:
			if motif[j]!=texte[i+j]:	# si texte différent de motif
				occurrence=False
				if texte[i+j] not in motif:	# si caractère pas dans motif
					i=i+j+1	# optimisation
				else:
					if j-position_adroite[texte[i+j]]>0:
						i=i+j-position_adroite[texte[i+j]]	# optimisation du décalage
					else:
						i=i+p-j		# début optimisation
			else:
				j=j-1	# on recule d'une position dans la fenêtre texte
		if occurrence==True:	# si motif dans texte
			positions.append(i)
			i=i+p

	return positions


from time import time

def temps(texte,motif) :
	t1 = time()
	naive(texte,motif)
	t2 = time()
	print(t2 - t1)

	t1 = time()
	horse(texte,motif)
	t2 = time()
	print(t2 - t1)

	t1 = time()
	boyer(texte,motif)
	t2 = time()
	print(t2 - t1)


print([1,2]+[3,6])