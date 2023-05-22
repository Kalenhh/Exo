#coding:utf-8

import tkinter as tk
from random import *
from time import*

class Cell() : 
	def __init__(self,pos,maze_size) :
		"""
		cluster : int
		pos : tuple (x,y)
		maze_size : tuple (largeur,hauteur)
		top , bottom , left , right : 	"w" --> wall , 
										"r" --> road ,
										"l" --> locked


		directions --->       0
							3 c 1
							  2
		"""
		self.state = "dispo"

		self.adj = {0:(0,1,2),
					1:(1,0,3),
					2:(0,-1,0),
					3:(-1,0,1)}

		self.cluster = pos[0] + pos[1]*maze_size[0]
		self.pos = pos

	# Init wall -------------------------------
		# Si les cellules sont sur les bords les murs sont "locked"

		if pos[1] == maze_size[1] -1 : self.top = "l"			
		else : self.top = "w"

		if pos[1] == 0 : self.bottom = "l"
		else : self.bottom = "w"

		if pos[0] == 0 : self.left = "l"
		else : self.left = "w"
		
		if pos[0] == maze_size[0] -1 : self.right = "l"
		else : self.right = "w"

		self.wall = [self.top,self.right,self.bottom,self.left]

	# -----------------------------------

	def voisine(self,direction,maze_dict) :

		voisine = maze_dict[ ( self.pos[0]+self.adj[direction][0] , self.pos[1]+self.adj[direction][1] ) ]

		return voisine

	def open_wall(self,direction,reverse = False) :

		if reverse == False :
			self.wall[direction] = "r"
		else :
			self.wall[self.adj[direction][2]] = "r"

	def lock_wall(self,direction,reverse = False) :

		if reverse == False :
			self.wall[direction] = "l"
		else :
			self.wall[self.adj[direction][2]] = "l"

	def wall_dispo(self) :
		"""
		Retourne la direction dans laquel un mur est dispo pour destruction
	
		"""
		if "w" not in self.wall :
			return None

		while True :
			direction = randint(0,3)
			if self.wall[direction] == "w" :
				return direction


def generate_maze(width,eight,can) :

	total_time = time()

	cell_dict = {(x,y) : Cell(  (x,y),(width,eight)   ) for x in range(width) for y in range(eight)} 
	cell_ind = [ o for o in cell_dict ]

	p = 0
	while len(cell_ind)>1 :
		p += 1
		print(p,"/",width*eight," ",len(cell_ind))

		cell = cell_dict[cell_ind[randint(0,len(cell_ind)-1)]]  # On prend une cellule dispo
	
		direction = cell.wall_dispo()	# On prend une direction dispo
		cell_voisine = cell.voisine(direction,cell_dict) # On prend la voisine


		cell.open_wall(direction)
		cell_voisine.open_wall(direction,reverse=True)		# ON OUVRE LE WALL

		cluster_to_stay = cell.cluster 
		cluster_to_change = cell_voisine.cluster 

		
		for i in cell_dict :
			curr = cell_dict[i]

			if curr.cluster == cluster_to_change :		# CHANGER LES CLUSTER
				curr.cluster = cluster_to_stay
	

		for i in cell_dict :
			curr = cell_dict[i]

			for o in range(len(curr.wall)) :	# LOCK LES PAROI ENTRE 2 MEME CLUSTER

				if curr.wall[o] == "w" :
					if curr.cluster == curr.voisine(o,cell_dict).cluster :
						curr.lock_wall(o)
						curr.voisine(o,cell_dict).lock_wall(o,reverse = True)
	



		for i in cell_dict :
			curr = cell_dict[i]					# ENLEVER LES CELLULES TERMINEES

			if curr.wall_dispo() == None and curr.state == "dispo" :
				cell_ind.remove(curr.pos)
				curr.state = "full"

	
		







	





	# Draw the maze

	pad = 50
	for i in cell_dict : 	

		top_left = ( 500/width*i[0] +pad, 500/eight*(i[1]+1) +pad)
		top_right = ( 500/width*(i[0]+1) +pad, 500/eight*(i[1]+1) +pad)

		bottom_left = ( 500/width*i[0] +pad, 500/eight*i[1] +pad)
		bottom_right = ( 500/width*(i[0]+1) +pad, 500/eight*i[1]+pad)

		cell = cell_dict[i]
		cell_wall = cell.wall 

		color = []
		for o in cell_wall :
			if o == "l" :
				color.append("black")
			else : 
				color.append("red")


		if cell_wall[0] != 'r' :  	# VERS LE HAUT
			can.create_line( top_left[0],top_left[1],top_right[0],top_right[1], fill=color[0],width=2)

		if cell_wall[1] != 'r' :	# VERS LA DROITE
			can.create_line( top_right[0],top_right[1],bottom_right[0],bottom_right[1] , fill=color[1],width=2)

		if cell_wall[2] != 'r' :	# VERS LE BAS
			can.create_line( bottom_left[0],bottom_left[1],bottom_right[0],bottom_right[1] , fill=color[2],width=2)

		if cell_wall[3] != 'r' :	# VERS LA GAUCHE
			can.create_line( top_left[0],top_left[1],bottom_left[0],bottom_left[1] , fill=color[3],width=2)
	# ---------------------------------





	print(f"total time : {time()-total_time}")


app = tk.Tk()

c = tk.Canvas(app,width=1000,height=1000)
c.configure(bg="white")
c.pack()

generate_maze(40,40,c)

app.mainloop()