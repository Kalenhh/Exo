#coding:utf-8

from random import*
cara = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g",
		"h","j","k","l","m","w","x","c","v","b","n"]
def rec() :
	global cara
	print( 	cara[randint(0,len(cara))]   )
	rec()


def fonction(n) :
	u = 2

	for i in range(n) :
		u = 0.5*u+3

	return u



print(f"f(1) : {fonction(1)}\tf(2) : {fonction(2)}")

def somme(n) :
	u = 2
	s = 0

	for i in range(n+1) :
		s += u
		u = 0.5*u+3

	return s	

print(f"s(1) : {somme(1)}\ts(2) : {somme(2)}")

def cal(n,o,r,c) :
	# n = rang
	# o = U0
	# r = raison
	# c = constante

	u = o

	for i in range(n) :
		u = u*r+c

	return u

print(cal(20,3,0.1,-1))

def somme(n,o,r,c) :
	t = 0

	for i in range(n) :
		t += cal(i,o,r,c)

	return t	

print(somme(10,0.5,2,2))

def somme_borne(n1,n2,o,r,c) :
	s1 = somme(n1,o,r,c)
	s2 = somme(n2,o,r,c)

	return s2 - s1

print(somme_borne(12,20,3,0.4,1))

def deter(e,o,r,c) :
	# e = element a rechercher

	u = 0
	n = 0
	while u <= e :

		u = cal(n,o,r,c)
		n += 1 

	return n-1,u

print(deter(50,1,1.1,2),cal(13,1,1.1,2))



# Uo = 1000
# U(n+1) = U(n)*1.2-100

# 1000*1.2-100

def yui() :
	n = 0
	while cal(n,1000,1.2,-100) <= 30000 :
		n += 1
	print(n)	
	print(cal(n,1000,1.2,-100))

yui()	
