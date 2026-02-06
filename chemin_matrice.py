import random

def creation_matrice():
    
    while True:
        try:
            hauteur = int(input("Combien de lignes voulez-vous dans la matrice ? : "))
            if 0 < hauteur <= 7:
                break
            print("Erreur.  Veuillez entrer un chiffre entre 1 et 7.")
        except ValueError:
            print("Erreur.  Veuillez entrer un nombre entier.")

    while True:
        try:
            largeur = int(input("Combien de colonnes voulez-vous dans la matrice ? : "))
            if 0 < largeur <= 7:
                break
            print("Erreur.  Veuillez entrer un chiffre entre 1 et 7.")
        except ValueError:
            print("Erreur.  Veuillez entrer un nombre entier.")

    while True:
        try:
            valeur_max = int(input("Quelle est la valeur maximale des éléments de la matrice : "))
            if valeur_max > 0:
                break
            print("Erreur.  Veuillez entrer un chiffre supérieur à 1.")
        except ValueError:
            print("Erreur.  Veuillez entrer un nombre entier.")


    matrice = []
    for i in range(hauteur):
        matrice.append([])
    for ligne in matrice:
        ligne.extend(random.randint(1, valeur_max) for j in range(largeur))
    
    return matrice

def afficher_matrice(matrice):
    print("==== VOICI LA MATRICE ====\n")
    for ligne in matrice:
        print("".join(f"{colonne:4}" for colonne in ligne))

def trouver_chemin(matrice):
    dict_chemin = {}

    liste_max = []
    for ligne in matrice:
        liste_max.append(max(ligne)) 
    point_depart = max(liste_max)
    # igne_depart = 
    dict_chemin.update({"1": point_depart})
    deuxieme_point = max(liste_max.pop(point_depart), )
    print(dict_chemin)


matrice = creation_matrice()
afficher_matrice(matrice)
trouver_chemin(matrice)

ligne.index(point_depart), matrice


