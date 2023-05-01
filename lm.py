#coding:utf-8


class Graph :

	def __init__(self) :
		self.graphe = self.graphe={	"Bar Le Duc":	{"Nancy":83,"Metz":101},
									"Nancy":		{"Metz":55,"Bar Le Duc":83,"Lunéville":36},
									"Metz":			{"Nancy":55,"Bar Le Duc":101,"Thionville":30,"Sarrebourg":96},
									"Lunéville":	{"Nancy":36,"Sarrebourg":54,"Saint-Die":52},
									"Sarrebourg":	{"Lunéville":54,"Metz":96,"Saint-Die":71},
									"Thionville":	{"Metz":30},
									"Saint-Die":	{"Lunéville":52,"Sarrebourg":71}
									}

	def profondeur(self,depart) :

		sommet = ""
		pile = []
		decouvert = []
		sommet_suivant = ""

		pile.insert(0,depart)

		while len(pile)> 0 :
			sommet = pile.pop(0)

			if sommet not in decouvert :
				decouvert.append(sommet)

			for i in self.graphe[sommet] :
				if i not in decouvert :
					pile.insert(0,i)

		return decouvert

	def largeur(self,depart) :

		sommet = ""
		file = []
		decouvert = []
		sommet_suivant = ""

		file.insert(0,depart)

		while len(file)> 0 :
			sommet = file.pop(len(file)-1)

			if sommet not in decouvert :
				decouvert.append(sommet)

			for i in self.graphe[sommet] :
				if i not in decouvert :
					file.insert(0,i)

		return decouvert

	def cycle(self,depart) :

		pile = []
		decouvert = []

		pile.insert(0,depart)

		while len(pile)>0 :
			sommet = pile.pop(0)

			if sommet not in decouvert :
				decouvert.append(sommet)

			else :
				return True

			for i in self.graphe[sommet] :
				if i not in decouvert :
					pile.insert(0,i)

		return False


	def existence_chemin(self,sommet1,sommet2) :

		if sommet2 in self.largeur(sommet1) :
			return True
		else :
			return False

	def chemin(self,depart,sommet2) :

		sommet = ""
		file = []
		decouvert = []
		sommet_suivant = ""
		chemin = []

		

		file.insert(0,depart)

		while len(file)> 0 :
			sommet = file.pop(len(file)-1)

			chemin.append(sommet)

			if sommet == sommet2 :
				return chemin

			if sommet not in decouvert :
				decouvert.append(sommet)

			for i in self.graphe[sommet] :
				if i not in decouvert :
					file.insert(0,i)

		return False


a = Graph()
print(a.chemin("Nancy","Thionville"))