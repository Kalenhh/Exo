#coding:utf-8
# Test file

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


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
		self.camera.setH(90)

	def move(self,task) :
		speed = 1
		turn_speed = 1

		is_down = base.mouseWatcherNode.is_button_down

		if is_down('z') :

			self.pandaActor.setX(   self.pandaActor.getX()+( cos(self.pandaActor.getH())*speed  )  )
			self.pandaActor.setY(   self.pandaActor.getY()+( sin(self.pandaActor.getH())*speed  )  )

		if is_down('d') :
			self.pandaActor.setH(   self.pandaActor.getH()- turn_speed)

		if is_down('q') :
			self.pandaActor.setH(   self.pandaActor.getH()+ turn_speed)
			print(self.pandaActor.getH())
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