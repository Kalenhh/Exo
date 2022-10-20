#coding:utf-8
# Test file

from math import pi, sin, cos , radians

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from direct.gui.DirectGui import *


class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)


		# Load the environment model.
		self.scene = self.loader.loadModel("models/environment")
		# Reparent the model to render.
		self.scene.reparentTo(self.render)
		# Apply scale and position transforms on the model.
		self.scene.setScale(0.25, 0.25, 0.25)
		self.scene.setPos(-8, 42, 0)

		# Load and transform the panda actor.
		self.pandaActor = Actor("models/panda-model",
								{"walk": "models/panda-walk4"})
		self.pandaActor.setScale(0.005, 0.005, 0.005)
		self.pandaActor.reparentTo(self.render)
		# Loop its animation.
		self.pandaActor.loop("walk")

		self.taskMgr.add(self.move,'move')
		self.taskMgr.add(self.pause_menu,'pause_menu')

		self.camLens.setFov(60)

	def move(self,task) :
		speed = 0.1
		turn_speed = 2

		is_down = base.mouseWatcherNode.is_button_down

		if is_down('z') :

			self.pandaActor.setX(   self.pandaActor.getX()+( cos(radians(self.pandaActor.getH()-90))*speed  )  )
			self.pandaActor.setY(   self.pandaActor.getY()+( sin(radians(self.pandaActor.getH()-90))*speed  )  )

		if is_down('d') :
			self.pandaActor.setH(   self.pandaActor.getH()- turn_speed)

		if is_down('q') :
			self.pandaActor.setH(   self.pandaActor.getH()+ turn_speed)
			print(self.pandaActor.getH(),self.pandaActor.getPos())

		if is_down('p') :
			self.pandaActor.setH(0)
			self.pandaActor.setPos(0,0,0)

		self.camera.setPos(self.pandaActor.getX(),self.pandaActor.getY(),3.5)
		self.camera.setH(self.pandaActor.getH()-180)
		self.camera.setP(-20)

		return Task.cont

	def pause_menu(self,task) :

		def close() :
			bouton.destroy


		is_down = base.mouseWatcherNode.is_button_down

		if is_down('p') :

			bouton = DirectButton(lambda : bouton.destroy() ,text="ok")

		return Task.cont






	def avancers(self,e=0) :
		self.camera.setX(self.camera.getX()-1)
	def avancerq(self) :
		self.camera.setY(self.camera.getY()+1)
	def avancerd(self) :
		self.camera.setY(self.camera.getY()-1)
	def avancerz(self) :
		self.camera.setX(self.camera.getX()+1)

app = MyApp()
app.run()