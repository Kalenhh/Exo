#coding:utf-8

chaine = input("rentrez une chaine :")
chaine_fini = ""
for i in chaine :
	if i == "e" :
		chaine_fini= chaine_fini + "A"
		continue
	chaine_fini = chaine_fini + i

print(chaine_fini)