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
    print("\n\n\n***************************************************************************************************************\n\n***************************************************************************************************************\n\tBienvenue dans le programme des huits reines avec la méthode de récuit simulé\n***************************************************************************************************************\n\n***************************************************************************************************************\n\n\n")

    #   Génération aléatoire de la configuration de depart
    config = [random.randint(0, 7) for _ in range(8)]
    print("La configuration de départ est : {}".format(config))
    val_min = calcul_cout(config)
    print("Son coût est : {}\n\n".format(val_min))

    while temperature > 0:
        #   print("Les voisins sont : ")
        voisins = recherche_voisinage(config)

        voisin = random.choice(voisins)
        
        cout_config = calcul_cout(config)
        cout_voisin = calcul_cout(voisin)

        if cout_config <= cout_voisin :
            
            p_voisin = P(temperature, cout_config, cout_voisin)
            r = random.random()

            if r < p_voisin :
                config = voisin
        
        #   print("La configuration est : {} avec un coût de {}.".format(config, calcul_cout(config)))
        #   print("La temperature est : {}.\n\n\n".format(temperature))
        
        temperature -= 0.01

    print("\n\nLa configuration actuelle est la meilleur : {}".format(config))
    print("Son coût est : {}".format(calcul_cout(config)))
    print("La température finale est :", temperature)

