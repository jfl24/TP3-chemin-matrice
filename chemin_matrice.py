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

    point_depart = matrice[0][0]
    for index_ligne, ligne in enumerate(matrice):
        for index_colonne, element in enumerate(ligne):
            if element > point_depart:
                point_depart = element
                position_depart = (index_ligne, index_colonne)
    
    dict_chemin.update({"1": point_depart})
    
    prochain_point = max((matrice[index_ligne -1 if (index_ligne - 1) >= 0 else 0][index_colonne]), matrice[index_ligne][index_colonne - 1 if (index_colonne - 1) >= 0 else 0], matrice[index_ligne + 1 if (index_ligne + 1) <= (len(matrice)- 1) else 0][index_colonne], matrice[index_ligne][index_colonne + 1 if (index_colonne + 1) <= (len(matrice[0])-1) else 0]) 
    if prochain_point:
        dict_chemin.update({"2": prochain_point})
    
    # Voir comment trouver les positions des point adjacents au premier point
    

    print(dict_chemin)
    print(prochain_point)
    print(position_depart)


matrice = creation_matrice()
afficher_matrice(matrice)
trouver_chemin(matrice)




