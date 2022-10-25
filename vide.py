#coding:utf-8
# Vide
from graphviz import*
from notebook import*
from jupyter import*

"""
# triplet = (value,left,right)

class Node() :

	def __init__(self,element,gauche=None,droit=None) :
		self.value = element
		self.left = gauche
		self.right = droit

def new_node(valeur,gauche=None,droit=None) :
	return Node(valeur,gauche,droit)

def valeur(node) :
	return node.value

def fils_gauche(node) :
	return node.left

def fils_droit(node) :
	return node.right




def taille(root) :
	n = 0 
	nodes = []
	nodes.append(root)
	while len(nodes) > 0 :
		explore = nodes[len(nodes)-1]
		nodes.pop()

		n += 1

		if explore.left is not None :
			nodes.append(explore.left)
		if explore.right is not None :
			nodes.append(explore.right)

	return n


def tracer(root) :

	graphe=Digraph(filename='arbre',format='png')

	nodes = []
	nodes.append(root)
	while(len(nodes) > 0) :
		explore = nodes[0]
		nodes.pop(0)

		if explore.left is not None :
			graphe.edge(str(explore.value),str(explore.left.value))
			nodes.append(explore.left)

		if explore.right is not None :
			graphe.edge(str(explore.value),str(explore.right.value))
			nodes.append(explore.right)

	return graphe.view()




f = new_node("f")
g = new_node("g")
e = new_node("e",f,g)
d = new_node("d")
b = new_node("b",d,e)
h = new_node("h")
i = new_node("i")
c = new_node("c",h,i)
arbre = new_node("a",b,c)

print(taille(arbre))
tracer(arbre)


"""

for i in range(1000) :
	print(11*i)