#coding:utf-8

#Projet : Lecture et traitement de fichier CSV 

# Import :--------------------------------------------------------------------------------------------------------

from csv import*
#importer la biblihotèque csv

# Fonctions :---------------------------------------------------------------------------------------------------

def ouverture(root) :
#fonction d'ouverture de la table de nom

    with open(root,"r",encoding="utf-8") as fichier :
#ouverture du fichier 

        lecteur = reader(fichier,delimiter=";")
#lecteur est affectation reader ...

        table = []
#la table est affectation liste vide

        for i in lecteur :
#pour i dans lecteur 
            
            table.append(i)
#ajouter i à la liste table

        return table
#retourner table


def requete1(donné,prenom,genre,année) :
#fonction requete 1 

    trouvé = False
#trouvé est égale faux

    i=0
#i est affecté 0

    if genre == "m" :
#si le genre est égale à "m"

        genre = "1"
#genre est affectation "1"

    if genre == "f" :
#si le genre est égale à "f"

        genre = "2"
#genre est affectation "2"

    while trouvé == False :
#temps que trouvé est égale à false faire ...

        if i == len(donné) :
#si i est égale taille des donné

            trouvé = True
#trouvé est affecté à vrai

            return
#retourner

            continue
#continue

        if prenom == donné[i][1] and année == donné[i][2] and genre == donné[i][0] :
#si prenom est égale i soit le deuxième item de la liste (prenom)
#et année est égale i soit troisième item de la liste (année)
#et genre est égale i soit le primier item de la liste (genre)

            trouvé = True
#trouver est affecté à vrai

            return donné[i][3]
#retouner donnée i soit le quatrième item de la liste (effectif)

            continue
#continue


        i = i + 1
#i est affecté à i plus 1


def requete2(donné,année) :
#fonction requete 2
    
    donnéG = [i for i in donné if i[0]=="1" if i[2]==année if i[1] != "_PRENOMS_RARES"]
#donné garçon est affecté i pour i dans donné si i soit premier item (sexe) est égale "1"
#si i soit troisième item (année) est égale à année 
#si i soit deuxième item (prenom) est différent de "prenoms_rares"

    donnéF = [i for i in donné if i[0]=="2" if i[2]==année if i[1] != "_PRENOMS_RARES"]
#donné fille est affecté i pour i dans donné si i soit premier item (sexe) est égale "2"
#si i soit troisième item (année) est égale à année 
#si i soit deuxième item (prenom) est différent de "prenoms_rares"

    garcon = ()
#garcon est affecté à tuple vide

    fille = ()
#fille est affecté à tuple vide

    best = 0
#best est affecté 0

    for i in donnéG :
#pour i dans donné garçon
        
        if int(i[3]) > best :
#si l'entier i soit le quatrième item (effectif) est strictement supérieur à best

            best = int(i[3])
#best à pour affectation l'entier i soit le quatrième item (effectif)

            garcon = (i[1],best)
#garçon à pour affectation i soit le deuxième item (prenom) et best

    best = 0
#best à pour affectation

    for i in donnéF :
#pour i dans donné fille 

        if int(i[3]) > best :
#si l'entier i soit le quatrième item (effectif) est strictement supérieur à best

            best = int(i[3])
#best à pour affectation l'entier i soit le quatrième item (effectif)

            fille = (i[1],best)
#fille à pour affectation i soit le deuxième item (prenom) et best

    return garcon , fille
#retourn garçon et fille


def requete3(donne,prenom) :
#fonction requete 3

    maxi = ()
#maxi est affecté à un tuple vide

    best = 0
#best à pour affectation 0

    for i in donne :
#pour i dans donne

        if i[1] == prenom and int(i[3]) > best :
#si i soit le deuxième item (prenom) est égale à prenom  
#et à l'entier i soit le quatrième item (effectif) supérieur à best
           
            best = int(i[3])
#best à pour affectation l'entier i soit quatrième item (effectif)

            maxi = (i[2],best,i[0])
#maxi à pour affectation i soit le troisième item (prenom), best est i le premier item (genre)

    if maxi == () :
#si maxi est égale au tuple vide

        return None
#retouner None

    else :
#sinon
      
      return maxi    
#retourn maxi

def menu() :
    print("╔═════════════════════════════════════════════════════════════════════════════════╗")
    print("║                        ▲♠▲            MENU DES TACHES.           ▲♠▲            ║")
    print("║                        ▲♠▲        Que voulez-vous faire ?        ▲♠▲            ║")
    print("╠═════════════════════════════════════════════════════════════════════════════════╣")
    print("║1 ► Nombre d'individus qui portent un prénom donné pour une année donnée. ˃      ║")
    print("║2 ► Prénoms les plus courant pour une année donnée. ˃                            ║")
    print("║3 ► Année qui correspond au maximum d'un prénom donné. ˃                         ║")
    print("║4 ► Afficher les options. ˃                                                      ║")
    print("║5 ► Quitter le programme. ˃                                                      ║")
    print("╚═════════════════════════════════════════════════════════════════════════════════╝\n")
#menu pour faciliter le mode à choisir
                
# Programme :---------------------------------------------------------------------------------------

print("Hello world")

source = ouverture("nat2020.csv")
print("Fichier chargé :",len(source),"ligne.\n")

menu()

Lock = True
while Lock == True :    #Boucle principal

    choix = input("> ")

    if choix == "5" :       #Quitter la boucle
        Lock = False
        continue

    if choix == "4" :       #Afficher le menu
        menu()
        continue    

    if choix == "1" :
        prenom = input("Prénom :")
        année = input("Année :")
        sexe = input("Prénom masculin ou féminin ,m/f :")

        print(requete1(source,prenom.upper(),sexe.lower(),année),"personnes ont été nommées",prenom.lower(),"en",année,"\n")
        continue

    if choix == "2" :
        année = input("Année :")

        resultat = requete2(source,année)
        print("Masculin :",resultat[0][0],"Effectif :",resultat[0][1],"\n","Féminin :",resultat[1][0],"Effectif :",resultat[1][1],"\n")
        continue

    if choix == "3" :
        prenom = input("Prénom :")
        
        resultat = requete3(source,prenom.upper())
        print("En",resultat[0],",",resultat[1],"personnes ont été nommées",prenom,"(",resultat[2],")\n")
        continue

    else :                  #Si choix n'est pas valide
        print("Erreur")