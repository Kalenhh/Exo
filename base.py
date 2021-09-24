#coding:utf-8

print("Hello world")

def somme() :
	a= input("a:")
	b= input("b:")
	c= a+b
	return c

while True :
	binaire = str(input(":::"))
	decimal = 0
	nbits = len(binaire)
	for i in range(nbits) :
		decimal = decimal + int(binaire[nbits-1-i])*(2**i)

	print(decimal)	




