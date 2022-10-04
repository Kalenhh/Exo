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

        # Create the four lerp intervals needed for the panda to
        # walk back and forth.

        hprInterval2 = self.pandaActor.hprInterval(0.5,
                                                    Point3(10, 0, 0),
                                                    startHpr=Point3(0, 0, 0))
        posInterval = self.pandaActor.posInterval(0.5,
                                                    Point3(10,0,0),
                                                    startPos=Point3(0,0,0))


        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(  hprInterval2,
                                    posInterval,
                                    name="pandaPace")
        self.pandaPace.loop()

    # Define a procedure to move the camera.


app = MyApp()
app.run()