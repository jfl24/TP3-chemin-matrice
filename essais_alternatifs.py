import random
def chemin_matrice():
    
    matrice = []
        
    def creation_matrice():
        while True:
            try:
                hauteur = int(input("\nCombien de lignes voulez-vous dans votre matrice ? : "))
                if 0 < hauteur <= 7:
                    break
                print("Erreur.  Veuillez entrer un chiffre entre 1 et 7.")
            except ValueError:
                print("Erreur.  Veuillez entrer un nombre entier.")

        while True:
            try:
                largeur = int(input("Combien de colonnes voulez-vous dans votre matrice ? : "))
                if 0 < largeur <= 7:
                    break
                print("Erreur.  Veuillez entrer un chiffre entre 1 et 7.")
            except ValueError:
                print("Erreur.  Veuillez entrer un nombre entier.")

        while True:
            try:
                valeur_max = int(input("Quelle est la valeur maximale des éléments de votre matrice : "))
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
        print("\n==== VOICI LA MATRICE ====\n")
        for ligne in matrice:
            print("".join(f"{colonne:4}" for colonne in ligne))

    
    def suite_points(point_depart, position_depart):
    
        dict_chemin = {}
        
        
        def trouver_depart():
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
                    if position[1] < len(ligne) - 1:
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
        print(dict_chemin)
        return dict_chemin
        

    def afficher_resultat():
        liste_affichage = []
        for cle in dict_gagnant.keys():
            liste_affichage.append(cle)
        suite =  " -> ".join(str(n) for n in liste_affichage)
        print("\nVoici le chemin le plus long dans la matrice : ")
        if len(liste_affichage) == 1:
            print("Pas de déplacement possible.")
        else:
            print(f"{suite}")
            print(f"Longueur : {len(liste_affichage)}")
        for ligne in matrice:
            ligne.clear()
        matrice.clear()   
            
        
    # Boucle principale
    liste_chemins = []
    while True:
    
        print("\n====== RECHERCHE DU CHEMIN LE PLUS LONG DANS UNE MATRICE ======")
        # try:
        choix = input("\nVoulez-vous essayez une matrice personnalisée? (o/n)? : ")
        
        if choix.lower() == "n":
            print("Merci d'avoir essayé le chemin le plus long.  Au revoir.")
            break
        
        print("\n== Exemple de chemin dans une matrice ==")
        matrice_exemple = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for ligne in matrice_exemple:
            print("".join(f"{colonne:4}" for colonne in ligne))
        print("\nChemin le plus long : 9 -> 8 -> 7 -> 4 -> 1")
        print("Longueur : 5")
        creation_matrice()
        afficher_matrice()
        for index1, i in enumerate(matrice):
            for index2, j in enumerate(i):
                dict_result = suite_points(j, (index1, index2))
                liste_chemins.append(dict_result)
        dict_gagnant = liste_chemins[0]
        for chemin in liste_chemins:
            if len(chemin) > len(dict_gagnant):
                dict_gagnant = chemin
        afficher_resultat()

        # except Exception as e:
        #     print(f"\nErreur inattendue : {e}")

if __name__ == "__main__":    
    chemin_matrice()