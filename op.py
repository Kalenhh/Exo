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
		"""


		self.cluster = pos[0] + pos[1]*maze_size[0]
		self.pos = pos

	# -------------------------------
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


def generate_maze(width,eight,can) :

	t1 = time()
	cell_dict = {(x,y) : Cell(  (x,y),(width,eight)   ) for x in range(width) for y in range(eight)} 

	adj = {	0:(0,1,2),
			1:(1,0,3),
			2:(0,-1,0),
			3:(-1,0,1)}

	print(time()-t1)
	t1 = time()

	cluster_numbers = width * eight 
	while cluster_numbers > 1 :

		cell = cell_dict[ (randint(0,width-1),randint(0,eight-1)) ]    # Choisir une cellule

		direction = randint(0,3)					#   0                Choisir une direction pour le mur
						 							# 3   1
													#   2

		wall = cell.wall[ direction ] 					# Le meme mur

		if wall == "w" :

			voisine_cell = cell_dict[ ( cell.pos[0]+adj[direction][0] , cell.pos[1]+adj[direction][1] ) ]   # cellule voisine

			voisine_wall = voisine_cell.wall[adj[direction][2]]		# Le meme mur mais link a la cellule voisine
			cluster_to_change = voisine_cell.cluster


			if cell.cluster != voisine_cell.cluster :

				cell.wall[direction] = "r"
				voisine_cell.wall[adj[direction][2]] = "r"

				for i in cell_dict :
					if cell_dict[i].cluster == cluster_to_change :
						cell_dict[i].cluster = cell.cluster


				cluster_numbers -= 1

			else :
				cell.wall[direction] = "l"
				voisine_cell.wall[adj[direction][2]] = "l"


	print(time()-t1)
	# Montrer le maze

	t1 = time()
	pad = 50
	for i in cell_dict : 	

		top_left = ( 500/width*i[0] +pad, 500/eight*(i[1]+1) +pad)
		top_right = ( 500/width*(i[0]+1) +pad, 500/eight*(i[1]+1) +pad)

		bottom_left = ( 500/width*i[0] +pad, 500/eight*i[1] +pad)
		bottom_right = ( 500/width*(i[0]+1) +pad, 500/eight*i[1]+pad)

		cell = cell_dict[i]
		cell_wall = cell.wall 


	# --------------------------------
		if cell_wall[0] != 'r' :  	# VERS LE HAUT
			can.create_line( top_left[0],top_left[1],top_right[0],top_right[1], fill="black",width=2)

		if cell_wall[1] != 'r' :	# VERS LA DROITE
			can.create_line( top_right[0],top_right[1],bottom_right[0],bottom_right[1] , fill="black",width=2)

		if cell_wall[2] != 'r' :	# VERS LE BAS
			can.create_line( bottom_left[0],bottom_left[1],bottom_right[0],bottom_right[1] , fill="black",width=2)

		if cell_wall[3] != 'r' :	# VERS LA GAUCHE
			can.create_line( top_left[0],top_left[1],bottom_left[0],bottom_left[1] , fill="black",width=2)
	# ---------------------------------

	print(time()-t1)






app = tk.Tk()

c = tk.Canvas(app,width=1000,height=1000)
c.configure(bg="white")
c.pack()

generate_maze(80,80,c)

app.mainloop()