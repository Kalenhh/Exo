#coding:utf-8





import turtle 
from math import sin , cos , pi
from time import*

turtle.tracer(False)

def draw(modulo,taille) :

    
    for o in range(5001) :
        print(f"table : {o/100}")
        turtle.reset()

        for i in range(1,modulo) :

            
            turtle.goto(cos( -(2*pi/modulo)*i +pi/2)*taille,sin( -(2*pi/modulo)*i+pi/2)*taille )

            turtle.pendown()

            turtle.goto(cos( -(2*pi/modulo)*((i*o/100)%modulo) +pi/2)*taille,sin( -(2*pi/modulo)*((i*o/100)%modulo) +pi/2)*taille )

            turtle.penup()

        
        turtle.update()

    turtle.mainloop()


draw(200,400)
