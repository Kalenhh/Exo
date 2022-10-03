"""from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

verti = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edgez = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
def Cube():
    glBegin(GL_LINES)
    for edge in edgez:
        for vertex in edge:
            glVertex3fv(verti[vertex])
    glEnd()

def main():
    pygame.init()
    display = (900, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(35, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(3, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(15)

main()"""


#coding:utf-8

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