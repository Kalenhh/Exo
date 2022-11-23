#coding:utf-8

x = 4
L = []

def modif(x,L) :
	x = x + 1
	L.append(2*x)
	return x,L 

print(modif(x,L))
print(x,L)

print(int(4.5))