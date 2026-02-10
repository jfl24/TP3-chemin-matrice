import random
def chemin_matrice():
    print("====== RECHERCHE DU CHEMIN LE PLUS LONG DANS UNE MATRICE ======")
    dict_chemin = {}
    matrice = []

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

        
        for i in range(hauteur):
            matrice.append([])
        for ligne in matrice:
            ligne.extend(random.randint(1, valeur_max) for j in range(largeur))
    
    

    def afficher_matrice():
        print("==== VOICI LA MATRICE ====\n")
        for ligne in matrice:
            print("".join(f"{colonne:4}" for colonne in ligne))

    
        
    
    def suite_points():
        
        def trouver_depart():
            point_depart = matrice[i][j]
            position_depart = (index1, index2)
            dict_chemin.update({point_depart: position_depart})
            
    
        trouver_depart()
        point = list(dict_chemin.keys())[-1]
        position = list(dict_chemin.values())[-1]
        while True:
            liste_prochains_points = []
            liste_index_points = []
            for index_ligne, ligne in enumerate(matrice):
                for index_colonne, element in enumerate(ligne):
                    if position[0] > 0:
                        voisin_haut = matrice[position[0] - 1][position[1]]
                        position_voisin_haut = (position[0] - 1, position[1])
                        break
                    else:
                        voisin_haut = None
            if voisin_haut:
                liste_prochains_points.append(voisin_haut)
                liste_index_points.append(position_voisin_haut)

            for index_ligne, ligne in enumerate(matrice):
                for index_colonne, element in enumerate(ligne):
                    if position[0] < len(matrice) - 1:
                        voisin_bas = matrice[position[0] + 1][position[1]]
                        position_voisin_bas = (position[0] + 1, position[1])
                        break
                    else:
                        voisin_bas = None
            if voisin_bas:
                liste_prochains_points.append(voisin_bas)
                liste_index_points.append(position_voisin_bas)

            for index_ligne, ligne in enumerate(matrice):
                for index_colonne, element in enumerate(ligne):
                    if position[1] > 0:
                        voisin_gauche = matrice[position[0]][position[1] - 1]
                        position_voisin_gauche = (position[0], position[1] - 1)
                        break
                    else:
                        voisin_gauche = None
            if voisin_gauche:
                liste_prochains_points.append(voisin_gauche)
                liste_index_points.append(position_voisin_gauche)

            for index_ligne, ligne in enumerate(matrice):
                for index_colonne, element in enumerate(ligne):
                    if position[1] < len(matrice) - 1:
                        voisin_droite = matrice[position[0]][position[1] + 1]
                        position_voisin_droite = (position[0], position[1] + 1)
                        break
                    else:
                        voisin_droite = None
            if voisin_droite:
                liste_prochains_points.append(voisin_droite)
                liste_index_points.append(position_voisin_droite)
                        

            prochains_points_valides = []
            index_prochains_points_valides = []
            for index, point_liste in enumerate(liste_prochains_points):
                    if point_liste < point:
                        prochains_points_valides.append(point_liste)
                        index_prochains_points_valides.append(liste_index_points[index])
            
            if prochains_points_valides:
                prochain_point = prochains_points_valides[0]
            else:
                break
            for index, point_valide in enumerate(prochains_points_valides):
                if point_valide > prochain_point:
                    prochain_point = point_valide
                    index_prochain_point = index
            position_prochain_point = index_prochains_points_valides[prochains_points_valides.index(prochain_point)]

            if prochain_point:
                dict_chemin.update({prochain_point: position_prochain_point})
                point = prochain_point
                position = position_prochain_point
            else:
                break
    liste_chemins = []
    for index1, i in enumerate(matrice):
        for index2, j in enumerate(i):
            suite_points()
            liste_chemins.append(dict_chemin)
    print(liste_chemins)
    dict_max = max(liste_chemins, key=len)

    def afficher_resultat():
        liste_affichage = []
        for cle in dict_max.keys():
            liste_affichage.append(cle)
        suite =  " -> ".join(str(n) for n in liste_affichage)
        print("\nVoici le chemin le plus long dans la matrice : ")
        print(f"{suite}")
            
        
    creation_matrice()
    afficher_matrice()
    afficher_resultat()
    

chemin_matrice()