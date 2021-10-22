#coding:utf-8

tried = ""
liste_number = open("C:/Users/Elève/Desktop/number.txt","r")
contenu = liste_number.readlines()
print(contenu)

cont = []
for un in contenu :
	un = un.strip()
	cont.append(un)

print(cont)
print(len(cont))

for element in cont :
	contsanselement = cont
	print("test de",element)
	del(contsanselement[contsanselement.index(element)])
	for i in contsanselement :
		if element == i :
			print("doublon")
		else :
			continue

print(cont)
print(len(cont))