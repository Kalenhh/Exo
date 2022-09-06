#diapo.py
#coding:utf-8

# Librairie pour faire des diapos tkinter

"""

from tkinter import*

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button clicked")

    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()



window = GUI()
window.createbutton("Click me")
window.mainloop()

"""

from random import*
from tkinter import*

window = Tk()
window.geometry("500x500")

texte = Label(window,text="Are you gae ?",font=(None,20))
texte.pack()

def move() :
	global bouton
	bouton.place(x=randint(0,450),y=randint(0,450))

def accept() :
	window.destroy()
	acc = Tk()
	acce = Label(acc,text="You gae",font=(None,200),bg="red")
	acce.pack()
	acc.mainloop()
	

bouton1 = Button(window,text="Yes",command=accept)
bouton1.pack()
bouton1.place(x=250,y=50)

bouton = Button(window,text="No",command=move)
bouton.pack()
bouton.place(x=222,y=50)

window.mainloop()