#coding:utf-8

nom = input("nom >")
prenom = input("prenom >")
initiales = prenom[0] + nom[0]
initiales = initiales.upper()

print(f"Votre nom est {nom}\nVotre prénom est {prenom}\nVos initiales sont {initiales}")
