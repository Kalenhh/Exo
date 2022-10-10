#coding:utf-8
# Exo type Bac cryptage

def xor(N1,N2) :
	chain1,chain2 = str(bin(N1)) , str(bin(N2))
	crypt = ""
	for i in range(len(chain2)) :
		if chain1[i] == chain2[i] :  # LAAAAAAAAAAAA C EST PAS BON Y A 9 CHIFFRES
			crypt += "0"
		else :
			crypt += "1"
	return crypt

print(xor(70,83))


def xor_crypt(message,cle) :
	assert isinstance(message,str)
	assert isinstance(cle,str)

	code = ""
	for i in range(len(message)) :
		code += xor(ord(message[i]),ord(cle[i]))
	return code

print(xor_crypt("ALPHA","YAKYA"))

def generer_cle(mot,n) :

	cle = ""
	i = 0
	while len(cle) < n :
		cle += mot[i]
		i+=1
		if i >= len(mot) :
			i = 0
	return cle	
	
print(generer_cle("YAK",8))


def decrypt(code,cle) :
	decrypt = ""
	for i in range(len(cle)) :
		a = code[8*i:8*(i+1)]
		b = bin(ord(cle[i]))
		
		b = b[2:]
		b = "0"+b
		print(a,b)
		mid = ""
		for o in range(len(a)) :
			print(a[o],b[o])

			if a[o] == b[o] :
				mid += "0"
				print("0")
			elif a[o] != b[o] :
				mid += "1"
				print("1")

		print(mid,chr(int(mid)))

		decrypt += chr(int(mid))
	return decrypt



print(decrypt(xor_crypt("ALPHA","YAKYA"),"YAKYA"))