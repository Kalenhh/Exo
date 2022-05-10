#vide.py
#coding:utf-8

from tkinter import*

root = Tk()

can = Canvas(root,height=1000,width=800)
can.pack()




can.create_line(0,0,20,20,width=5,fill="blue")




source = PhotoImage(file="plan.PNG")
can.create_image(0,0,anchor=NW,image=source)

root.mainloop()