import random
from collections import Counter
from math import exp

temperature = 10000


def recherche_voisinage(liste : list):
    """
    Cette fonction recherche les éléments du voisinage d'un point.
    Nous définissons les éléments du voisinage comme les cases ayant au plus 2 cases
    sur la même colonne. 
    """
    voisinage = []
    voisinage.append([ (i + 1) % 8 for i in liste ])     #   Haut 1 
    voisinage.append([ (i + 2) % 8 for i in liste ])     #   Haut 2
    voisinage.append([ (i - 1) % 8 for i in liste ])     #   Bas 1
    voisinage.append([ (i - 2) % 8 for i in liste ])     #   Bas 2
    return voisinage


def recherche_voisinage_permutation(liste : list):
    """
    Cette fonction recherche les éléments du voisinage d'un point.
    Nous définissons les éléments du voisinage comme les cases ayant au plus 2 cases
    sur la même colonne. 
    """
    voisinage = []
    voisinage.append([ (i + 1) % 8 for i in liste ])     #   Haut 1 
    voisinage.append([ (i + 2) % 8 for i in liste ])     #   Haut 2
    voisinage.append([ (i - 1) % 8 for i in liste ])     #   Bas 1
    voisinage.append([ (i - 2) % 8 for i in liste ])     #   Bas 2
    return voisinage


def calcul_cout(config : list):
    """
    Cette fonction permet de calculer le coût (le nombre de conflits sur le plateau) d'une configuration
    particulière
    """
    cout = 0
    
    #   Conflits sur les lignes
    liste_conflits_lignes = [i[1] if i[1] > 1 else 0 for i in Counter(config).most_common()]
    cout += sum(liste_conflits_lignes)

    #   Conflit sur les diagonales
    for i in range(len(config)):
        for j in range(len(config)):
            if abs(j-i) == (config[j] - config[i]) and i != j:
                cout += 1

    return cout

def P(T, cout_s, cout_s_prime):
    return exp((cout_s - cout_s_prime) / T )


if __name__ == "__main__":
    print("\n\n\n***************************************************************************************************************\n\n***************************************************************************************************************\n\tBienvenue dans le programme des huits reines avec les algorithmes génétiques \n***************************************************************************************************************\n\n***************************************************************************************************************\n\n\n")

    taille_pop_depart = 50

    #   Génération de la population de depart
    population = [[random.randint(0, 7) for _ in range(8)] for a in range(taille_pop_depart)]
    print("La population de départ a été générée.")


    nvelle_population = []

    first = True

    while population != nvelle_population :

        if first:
            first = False
        else :
            population = nvelle_population
            nvelle_population = []

        tableau_parent = [ [calcul_cout(parent), parent] for parent in population ]
        tableau_parent.sort(reverse=True)
            
        print("La population est : {}".format(population))
        while len(tableau_parent) != 0:
            #   Selection de deux parents
            parent1, parent2 = tableau_parent.pop()[1], tableau_parent.pop()[1]

            print("\nLes parents sont : {} et {}\n".format(parent1, parent2))
            #   Selection de l'indice de coupure
            longueur_config = len(parent1)
            indice_coupure = random.randint(0, longueur_config)
            print("\nL'indice de coupure est : {}".format(indice_coupure))

            #   Création des enfants
            enfant1, enfant2 = parent1[:indice_coupure] + parent2[indice_coupure:], parent2[:indice_coupure] + parent1[indice_coupure:]

            #   Mutations des enfants
            mutation = random.randint(0, 1)

            if mutation:
                indice1_mutation, indice2_mutation = random.randint(0, longueur_config - 1), random.randint(0, longueur_config - 1)
                enfant1[indice1_mutation], enfant1[indice2_mutation] = enfant1[indice2_mutation], enfant1[indice1_mutation]

            print("\nLes enfants sont : {} et {}".format(enfant1, enfant2))

            nvelle_population.append(enfant1)
            nvelle_population.append(enfant2)


            print("\n\n\n\n\n\n\n")

    print(population[0])
    #print("\n\nLa meilleur configuration est : {}".format(population[0]))





