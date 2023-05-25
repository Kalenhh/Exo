#coding:utf-8

import tkinter as tk
from time import sleep

app = tk.Tk()




class Cell() :
	def __init__(self,pos) :

		self.pos = pos
		self.state = "dead"
		self.number_voisin = 0

class Terrain() :
	def __init__(self,width,height) :

	# Faire le quadrillage ------------------
		c = tk.Canvas(app,width=600,height=600)
		c.configure(bg="white")
		c.pack()

		for i in range(height) :
			c.create_line(0,600/height*i,600,600/height*i)

		for i in range(width) :
			c.create_line(600/width*i,0,600/width*i,600)
	# ----------------------------------------

		self.ground = {}
		for o in range(height) :
			for i in range(width) :
				self.ground[(i,o)] = Cell((i,o))


	def loop() :
		while self.running == True :

			# Prendre le nbr de voisin

			# Actualisé les cellules
			for i in zone.ground :
				sta = zone.ground[i].state
				voi = zone.ground[i].number_voisin

				if sta == "alive" and voi < 2 :
					sta = "dead"

				if sta == "dead" and voi >= 2 :
					sta == "alive"

			# Dessiner




zone = Terrain(10,10)












app.mainloop()