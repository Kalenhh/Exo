#coding:utf-8

"""
tried = ""
liste_number = open("C:/Users/baudo/Desktop/number.txt","r")
contenu = liste_number.readlines()
print(contenu)

cont = []
for un in contenu :
	un = un.strip()
	cont.append(un)

print(cont)
print(len(cont))

cont = list(dict.fromkeys(cont))

print(cont)
print(len(cont))"""

"""
with open("C:/Users/baudo/Desktop/number.txt","r") as liste_number :
	liste_number_lignes = liste_number.readlines()
	res = []
	for element in liste_number_lignes :
		if element not in res :
			res.append(element)
			print("clear")
			continue
		print("doublon")
	print(res)
	print(len(liste_number_lignes))
	print(len(res))

with open("C:/Users/baudo/Desktop/number.txt","w") as liste_number :
	liste_number.writelines(res) """

import tkinter as tk
import glob



class App:

	def __init__(self, root):
		self.root = root
		self.menu()
		self.text()
		self.root.bind("<Control-l>", lambda x: self.hide())
		self.hidden = 0

	def menu(self):
		self.frame1 = tk.Frame(self.root)
		self.frame1.pack(side="left", fill=tk.BOTH, expand=1)
		self.lb = tk.Listbox(self.frame1)
		self.lb['bg'] = "black"
		self.lb['fg'] = "lime"
		self.lb.pack(side="left", fill=tk.BOTH, expand=1)
		for file in glob.glob("*"):
			self.lb.insert(tk.END, file)

	def text(self):
		self.frame2 = tk.Frame(self.root)
		self.frame2.pack(side="left", fill=tk.BOTH, expand=1)
		self.txt = tk.Text(self.frame2)
		self.txt['bg'] = 'gold'
		self.txt.pack(fill=tk.BOTH, expand=1)

	def hide(self):
		if self.hidden == 0:
			self.frame1.destroy()
			self.hidden = 1
			print("Hidden", self.hidden)
		else:
			self.frame2.destroy()
			self.menu()
			self.text()
			self.hidden = 0
			print("Hidden", self.hidden)



root = tk.Tk()
app = App(root)
root.mainloop()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
import tkinter as tk
import glob
 
 
 
class App:
 
	def __init__(self, root):
		self.root = root
		self.menu()
		self.text()
		self.root.bind("<Control-l>", lambda x: self.hide())
		self.hidden = 0
 
	def menu(self):
		self.frame1 = tk.Frame(self.root)
		self.frame1.pack(side="left", fill=tk.BOTH, expand=1)
		self.lb = tk.Listbox(self.frame1)
		self.lb['bg'] = "black"
		self.lb['fg'] = "lime"
		self.lb.pack(side="left", fill=tk.BOTH, expand=1)
		for file in glob.glob("*"):
			self.lb.insert(tk.END, file)
 
	def text(self):
		self.frame2 = tk.Frame(self.root)
		self.frame2.pack(side="left", fill=tk.BOTH, expand=1)
		self.txt = tk.Text(self.frame2)
		self.txt['bg'] = 'gold'
		self.txt.pack(fill=tk.BOTH, expand=1)
 
	def hide(self):
		if self.hidden == 0:
			self.frame1.destroy()
			self.hidden = 1
			print("Hidden", self.hidden)
		else:
			self.frame2.destroy()
			self.menu()
			self.text()
			self.hidden = 0
			print("Hidden", self.hidden)
 
 
 
root = tk.Tk()
app = App(root)
root.mainloop()
