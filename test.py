#coding:utf-8

"""
tried = ""
liste_number = open("C:/Users/baudo/Desktop/number.txt","r")
contenu = liste_number.readlines()
print(contenu)

cont = []
for un in contenu :
	un = un.strip()
	cont.append(un)

print(cont)
print(len(cont))

cont = list(dict.fromkeys(cont))

print(cont)
print(len(cont))"""


with open("C:/Users/baudo/Desktop/number.txt","r") as liste_number :
	liste_number_lignes = liste_number.readlines()
	res = []
	for element in liste_number_lignes :
		if element not in res :
			res.append(element)
			print("clear")
			continue
		print("doublon")
	print(res)
	print(len(liste_number_lignes))
	print(len(res))

with open("C:/Users/baudo/Desktop/number.txt","w") as liste_number :
	liste_number.writelines(res)


