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

        
        def avancerz(e=0) :
            self.pandaActor.posInterval(1,)

            self.pandaActor.setX(self.pandaActor.getX()+1)
        def avancers(e=0) :
            self.pandaActor.setX(self.pandaActor.getX()-1)
        def avancerq(e=0) :
            self.pandaActor.setY(self.pandaActor.getY()+1)
        def avancerd(e=0) :
            self.pandaActor.setY(self.pandaActor.getY()-1) 

            self.scene.base.cam.setY(self.base.camera.getY()-1)



        self.accept('z',avancerz)
        self.accept('s',avancers)
        self.accept('q',avancerq)
        self.accept('d',avancerd)



app = MyApp()
app.run()