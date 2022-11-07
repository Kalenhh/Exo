#coding:utf-8
# Test file

from math import pi, sin, cos , radians

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from direct.gui.DirectGui import *
from pandac.PandaModules import WindowProperties



class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)

		base.disableMouse()
		props = WindowProperties()
		props.setCursorHidden(False)
		base.win.requestProperties(props)

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
		self.pandaActor.inerti = -10

		self.taskMgr.add(self.move,'move')
		self.taskMgr.add(self.pause_menu,'pause_menu')

		self.camLens.setFov(80)

	def move(self,task) :
		speed = 0.3
		camera_sensi = 25
		jump = 2

		is_down = base.mouseWatcherNode.is_button_down

		if is_down('z') :

			self.pandaActor.setX(   self.pandaActor.getX()+( cos(radians(self.pandaActor.getH()-90))*speed  )  )
			self.pandaActor.setY(   self.pandaActor.getY()+( sin(radians(self.pandaActor.getH()-90))*speed  )  )
		
		if is_down('s') :

			self.pandaActor.setX(   self.pandaActor.getX()-( cos(radians(self.pandaActor.getH()-90))*speed  )  )
			self.pandaActor.setY(   self.pandaActor.getY()-( sin(radians(self.pandaActor.getH()-90))*speed  )  )

		if is_down('q') :
			self.pandaActor.setX(   self.pandaActor.getX()+( cos(radians(self.pandaActor.getH()))*speed  )  )
			self.pandaActor.setY(   self.pandaActor.getY()+( sin(radians(self.pandaActor.getH()))*speed  )  )

		if is_down('d') :
			self.pandaActor.setX(   self.pandaActor.getX()-( cos(radians(self.pandaActor.getH()))*speed  )  )
			self.pandaActor.setY(   self.pandaActor.getY()-( sin(radians(self.pandaActor.getH()))*speed  )  )

		if is_down('space') and self.pandaActor.inerti <= -10 :
			self.pandaActor.inerti = jump


		if is_down('p') :
			self.pandaActor.setZ(0)
		
		if self.pandaActor.inerti > -10 :
			self.pandaActor.inerti -= 0.1

		self.pandaActor.setZ(self.pandaActor.getZ()+self.pandaActor.inerti)
		
		if self.pandaActor.getZ() < 0 :
			self.pandaActor.setZ(0)
			self.pandaActor.inerti = -10


		x,y = 0,0
		if base.mouseWatcherNode.hasMouse():
			x = round(base.mouseWatcherNode.getMouseX() , 2 )
			y = round(base.mouseWatcherNode.getMouseY() , 2 )
			props = base.win.getProperties()
			base.win.movePointer(0,props.getXSize() // 2,props.getYSize() // 2)
		
		x,y = x*camera_sensi,y*camera_sensi

		self.camera.setPos(self.pandaActor.getX(),self.pandaActor.getY(),self.pandaActor.getZ()+3.5)
		
		self.camera.setH(self.camera.getH()-x)
		self.pandaActor.setH(self.camera.getH()-180)

		self.camera.setP(self.camera.getP()+y)

		return Task.cont

	def closer(self) :
		self.b.destroy()
		self.taskMgr.add(self.move,'move')
		self.taskMgr.add(self.pause_menu,'pause_menu')
		return

	def destruire(self) :
		self.destroy()


	def pause_menu(self,task) :

		is_down = base.mouseWatcherNode.is_button_down

		if is_down('p') :
			taskMgr.remove('move')
			props = WindowProperties()
			props.setCursorHidden(False)
			base.win.requestProperties(props)	

			self.b = DirectButton(text='return',command=self.closer,scale=0.1)

			self.bert = DirectButton(text='destroy',command=self.destruire,scale=0.1,pos=(0.5,0.5,0.2))
			print(self.bert['text_pos'])

			self.taskMgr.remove('pause_menu')
			return Task.cont

		return Task.cont

app = MyApp()
app.run()