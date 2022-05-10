#vide.py
#coding:utf-8

# Librairies :-----------------------------------------------------------------------------------------------------------

from tkinter import*

# Set Variables :--------------------------------------------------------------------------------------------------

lieu_cdi = [(287,241)]
lieu_ateliers = [(445,366),(405,629),(619,710)]
lieu_cantine = [(339,896)]
lieu_perm = [(356,303)]
lieu_vie_sco = [(300,306)]
lieu_gymnase = [(105,489)]
lieu_recre = [(344,408),(358,197)]
lieu_muscu = [(453,584)]
lieu_internat = [(187,69)]
lieu_classe = [(430,546),(378,246)]
lieu_labo = [(378,107)]
lieu_couloirs = [(421,565),(468,432)]
lieu_admin = [(543,798),(549,931)]
lieu_profs = [(288,170)]

lieu_all_0 = [lieu_cdi,lieu_ateliers,lieu_cantine,lieu_perm,lieu_vie_sco,lieu_gymnase,lieu_recre,lieu_muscu,lieu_internat,lieu_classe,lieu_labo,lieu_couloirs,lieu_admin,lieu_profs]
lieu_all = []
for i in lieu_all_0 :
	for o in i :
		lieu_all.append(o)

red = "#ff0000"
blue = "#66ccff"
green = "#66B266"

# Main root :----------------------------------------------------------------------------------------------

root = Tk()
root.minsize(1000,1000)
root.maxsize(1000,1000)

frame_dessin = Frame(root,height=1000,width=700)
frame_dessin.pack(side="left")

can = Canvas(frame_dessin,height=1000,width=700,bg=green)
can.pack()




source = PhotoImage(file="plan.PNG")
can.create_image(0,0,anchor=NW,image=source)




for i in lieu_all :
	can.create_line(i[0]-1,i[1]-1,i[0]+1,i[1]+1,width=2,fill=red)




frame_config = Frame(root,height=1000,width=300,bg="yellow")
frame_config.pack(side="right",fill=BOTH)


root.mainloop()