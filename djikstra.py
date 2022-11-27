#coding:utf-8

from graphviz import *



class Node() :

	def __init__(self,nom) :
		self.name = nom 		# ID du node
		self.connexion = {}		# {'NOM du patelin direction':la distance jusque laba en entier }

	def add_connexion(self,co,dis) :
		"""
		co : nom du patelin 
		dis : distance
		"""
		if co not in self.connexion.keys() :  # CHECK
			self.connexion[co] = dis


class Graphique() :
	"""
	Graph avec des arete avec des valeurs et bilateral
	"""

	def __init__(self) :
		self.nodes = {}      # {'A':node Object,'B':node Object}

	def add(self,node1,node2,distance) :
		"""
		

		"""

		if node1 not in self.nodes :
			self.nodes[node1] = Node(node1)

		if node2 not in self.nodes :
			self.nodes[node2] = Node(node2)

		self.nodes[node1].add_connexion(node2,distance)
		self.nodes[node2].add_connexion(node1,distance)




	def chemin_plus_court(self,depart,arrive) :   # ALGO DE DJIKSTRA MAIS PAS FAIT AVEC UNE MATRICE
		"""
		tab : tableau 								# (CASE , DISTANCE)
		depart et arrive : 'A' 'B' 'C'
		"""

		tab = []     	# liste de tuple : ('A','B',distance) A = source , B = node , distance = somme distance depuis depart
		ban = []   		# liste du nom de node bannis
		current = (depart,depart,'0')  	# tuple de l'iteration actuelle

		for i in range(len(self.nodes)-1) :

			for o in self.nodes[current[1]].connexion :

				if self.nodes[current[1]].connexion[o] in ban :
					continue


				tab.append((current[1],o,int(self.nodes[current[1]].connexion[o])+int(current[2])))


			ban.append(current[1])

			current = tab[0]
			for o in tab :
				if o[2] < current[2] :
					current = o

				if o[1] in ban :
					tab.remove(o)

			print(tab,ban,'\n')












											



	def aff(self) :
		"""
		Affiche le graphique
		"""

		ban = []

		g = Graph('g')

		for i in self.nodes :  # 'A' , 'B'  > les clé du dico

			ban.append(i)

			for o in self.nodes[i].connexion : 		# les clé du dico connexion de chaque node object de i

				if o in ban :
					continue

				g.edge(i,o,label=str(self.nodes[i].connexion[o]))

		g.view()		




gr = Graphique()

gr.add('B','H',12)
gr.add('B','G',13)
gr.add('G','C',7)
gr.add('G','F',5)
gr.add('G','E',9)
gr.add('E','F',3)
gr.add('F','C',11)
gr.add('F','D',21)
gr.add('C','D',8)
gr.add('C','H',20)
gr.add('D','H',9)


gr.chemin_plus_court('B','F')

"""
g = Graph('g')




g.attr('node',color='#000000')			# GRAPHVIZ PART
g.edge('a','b')

g.node('a',color='#0000ff')



g.view()



"""





"""
from pandac import PandaModules as P
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from direct.actor import Actor
#window-type none is in my Config.prc (the only change).
base.openMainWindow(type = 'onscreen')#you may not need this

base.cTrav = P.CollisionTraverser()#traverser
base.cTrav.setRespectPrevTransform(1)
class World(DirectObject):
	def __init__(self):
		#load ralph
		self.ralph = Actor.Actor("models/ralph",
			{"run":"models/ralph-run",#animations are not used yet
			"walk":"models/ralph-walk"})
		self.ralph.reparentTo(render)
		self.ralph.setScale(.2)
		self.ralph.setCollideMask(P.BitMask32.allOff())
		#set up ralph's collision ray
		self.ray = P.CollisionRay(0, 0, 2, 0, 0, -1)#from head & point down?
		self.ralphRay = self.ralph.attachNewNode(P.CollisionNode('ray'))
		self.ralphRay.node().addSolid(self.ray)
		self.ralphRay.show()
		#load environ
		self.environ = loader.loadModel("models/world")
		self.environ.reparentTo(render)
		self.environ.setCollideMask(P.BitMask32.allOn())
		self.environ.setH(180)
		self.environ.setPos(0,0,-5)
		#the floor handler keeps ralph grounded
		self.floor = P.CollisionHandlerFloor()
		self.floor.setMaxVelocity(2)#if set higher or to 0 ralph goes under.
##        self.floor.setOffset(.2) #I haven't figured this out yet
		base.cTrav.addCollider(self.ralphRay,self.floor)
		self.floor.addCollider(self.ralphRay,self.ralph)
		#shows the collision solids
		base.cTrav.showCollisions(render)
		#setup keyboard
		for k,v in {'arrow_up':'up','arrow_down':'dn','arrow_left':'lf',
			'arrow_right':'rt'}.items():
			self.accept(k,self.move,[v])
	def move(self,direction):
		if direction == 'up':
			self.ralph.setFluidY(self.ralph.getY()+.1)
		if direction == 'dn':
			self.ralph.setFluidY(self.ralph.getY()-.1)
		if direction == 'lf':
			self.ralph.setFluidX(self.ralph.getX()-.1)
		if direction == 'rt':
			self.ralph.setFluidX(self.ralph.getX()+.1)
World()
run()"""