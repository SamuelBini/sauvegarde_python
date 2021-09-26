from random import randint
import copy
from collections import Counter


def pop_depart(config_depart : list ):
    """
    Génère une population de départ à partir de la liste des cases fixes. 
    On considère les cases ayant 0 comme valeur comme vides
    """

    pop = copy.deepcopy(config_depart)

    #   Parcours des lignes
    for i in range(9):
        #   Parcours des colonnes
        for j in range(9):
            if pop[i][j] == 0 :
                pop[i][j] = randint(1, 9)

    return pop




def fitness(config : list):
    """ 
    Cette fonction de fitness calcule le nombre de doublons par ligne et par colonne et le conserve dans un tableau
    """

    pop = copy.deepcopy(config)

    # Calcule selon les lignes
    nbre_double_ligne = [ 0 for _ in range(9)]
    for i in range(9):
        lst = Counter(pop[i]).most_common()
        for j in lst:
            if j[1] > 1:
                nbre_double_ligne[i] += 1

    # Calcule selon les colonnes
    nbre_double_col = [ 0 for _ in range(9)]
    for i in range(9):
        lst = Counter([pop[k][i] for k in range(9)]).most_common()
        for j in lst:
            if j[1] > 1:
                nbre_double_col[i] += 1


    return nbre_double_ligne, nbre_double_col





def selection (nbre_double_ligne, nbre_double_col):
    """ 
    Sélectionne la zone ayant le plus de doublons
    """
    zones = [ 0 for _ in range(3)]
    zones[0] = sum(nbre_double_ligne[:3]) + sum(nbre_double_col[:3])
    zones[1] = sum(nbre_double_ligne[3:6]) + sum(nbre_double_col[3:6])
    zones[2] = sum(nbre_double_ligne[6:]) + sum(nbre_double_col[6:])

    score_max = max(zones)

    return zones.index(score_max), score_max 




def generation_nvlle_pop(config : list, zone : int):
    """ 
    Génère une nouvelle population en modifiant les chiffres d'une zone et renvoie le resultat
    """
    if zone == 0:
        index = [0, 1, 2]
    elif zone == 1 :
        index = [3, 4, 5]
    else :
        index = [6, 7, 8]
    
    pop = copy.deepcopy(config)

    for i in index:
        for j in index:
            pop[i][j] = randint(1, 9)
    
    return pop




if __name__== "__main__" :
    
    sudoku = [  [0, 0, 2, 9, 5, 6, 0, 0, 0], 
                [0, 4, 0, 7, 0, 0, 9, 0, 1],
                [0, 7, 0, 0, 8, 4, 0, 3, 2],
                [4, 0, 6, 5, 0, 0, 3, 2, 0],
                [0, 9, 0, 0, 2, 0, 0, 4, 0],
                [0, 2, 0, 0, 4, 7, 8, 0, 0],
                [8, 0, 0, 2, 7, 0, 0, 1, 0],
                [7, 5, 3, 0, 0, 8, 0, 6, 9],
                [0, 0, 0, 3, 6, 5, 7, 0, 0] ]
    
    new_pop = pop_depart(sudoku)


    print("La polulation de départ est : ")
    print(new_pop)
    print("\n\n\n")

    score_lignes, score_cols = fitness(new_pop)

    old_sum_score = sum(score_lignes) + sum(score_cols)
 
    if old_sum_score != 0 :
        while True :
            zone, score_zone = selection(score_lignes, score_cols)
            new_population = generation_nvlle_pop(new_pop, zone)
            score_lignes, score_cols = fitness(new_population)
            new_sum_score = sum(score_lignes) + sum(score_cols)


            if new_sum_score < old_sum_score :
                new_pop = copy.deepcopy(new_population)
                old_sum_score = new_sum_score

                print("\n\n\nUne meilleure population est {} doublons est : ".format(old_sum_score))
                print(new_pop)

            if new_sum_score == 0:
                break

    
    print("\n\n\n\nLa meilleure configuration pour le SUDOKU est : ")
    print(new_pop)
