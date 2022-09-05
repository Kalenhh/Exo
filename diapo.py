#diapo.py
#coding:utf-8

# Librairie pour faire des diapos tkinter

from tkinter import*

class App :

	def __init__(self) :
		self.root = Tk()

		self.root.mainloop()

	def bg(self,color) :
		self.root.configure(bg=color)	


root = App()
root.bg("green")