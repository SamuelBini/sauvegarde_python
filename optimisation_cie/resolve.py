# -*- coding: utf-8 -*-

import math
from random import randint 
import random


MINI_LOTS = 7
RAYON_TERRE = 6371




def parser(fi):
    with open(fi, 'r') as fichier :
        a = fichier.read().split('\n')
        split_and_convert = lambda der : [float(der[0]), float(der[1])]
        b = [ split_and_convert(i.split("|")) for i in a[1:-1] ]

    return b



def naive_solver(data):
    #   Décomposition en 7 listes
    lot = 0
    for i in range(len(data)):
        position = i % 3000
        if position == 0:
            lot += 1
        data[i] = data[i] + [position + 1, lot]

    return data




"""
def generate_population(individu):
    " Génère une population à partir d'un individu de départ"

    population = []
    
    for _ in range(2):
        new_indiv = [[] for _ in range(MINI_LOTS)]
        for i in individu:
            index = randint(1, 7)
            new_indiv[index - 1].append(i + [None, index])
        for i in range(len(new_indiv)):
            for j in range(len(new_indiv[i])):
                lon = [k for k in range(1, len(new_indiv[i]) + 1)]
                new_indiv[i][j][2] = lon.pop(random.choice(lon) - 1)

        population.append(new_indiv)    

    return population



def order_lot(lots) : 
    ordored_lots = [None for _ in range(MINI_LOTS)] 
    for i in range(len(lots)):
        ordored_lots[i] = sorted(lots[i], key = lambda x: x[2])
    return ordored_lots



def genetic_solver(positions):

    population = generate_population(positions)

    #   On ordonne chaque élément de la population
    for i in range(len(population)):
        population[i] = order_lot(population[i])
 
    #   Calcul du coût de chaque enfant
    for i in range(len(population)):
        res = calcul_inertie(population[i])
        m = [population[i], scoring(population[i], res)[2]]
        population[i] = m 
    
    population = sorted(population, key = lambda x: x[1], reverse=True)

    return population


"""


def output_parser(data):
    convertToStr = lambda i : "{} {} {} {}".format(str(i[0]), str(i[1]), str(i[2]), str(i[3]))
    output_filename = "output.txt"
    with open(output_filename, "w") as f:
        data = "\n".join([convertToStr(i) for i in data])
        f.writelines(data)
    


def solution_parser(file_name):
    lots = [ [] for _ in range(MINI_LOTS)]
    with open(file_name, 'r') as file :
        for i in file.readlines():
            a = i.split(" ")
            position = [float(a[0]), float(a[1]), int(a[2]), int(a[3])]
            try:
                lots[position[3] - 1].append(position)
            except AttributeError as e:
                print(e)
                print('Erreur dans les données de lots')
                return None
    return lots


def degreeToRadian(degre):
    return degre * math.pi / 180


def calcul_distance(pointA, pointB):
    lon = degreeToRadian(pointB[0] - pointA[0])
    lat = degreeToRadian(pointB[1] - pointA[1] )

    lon = degreeToRadian(lon)
    lat = degreeToRadian(lat)

    a = math.sin(lat/2) * math.sin(lat/2) + math.sin(lon/2) * math.sin(lon/2) * math.cos(pointA[1]) * math.cos(pointB[1])
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)); 
    return RAYON_TERRE * c



def calcul_inertie(data):

    max = 0

    centres = [None for _ in range(MINI_LOTS)]

    intra = []

    #   Calcul des inerties intra
    for lot in range(len(data)):
        longueur = len(data[lot])
        long_ = sum(x[0] for x in data[lot]) / longueur
        lat_ = sum(x[1] for x in data[lot]) / longueur

        centres[lot] = [long_, lat_]

        inertie_intra = 0
        for i in data[lot]:
            new_distance = calcul_distance(i, [long_, lat_])
            inertie_intra += new_distance
            if new_distance > max:
                max = new_distance

        intra.append(inertie_intra)

    #   Calcul des inerties inter
    inter = 0
    long_ = sum(x[0] for x in centres) / MINI_LOTS
    lat_ = sum(x[1] for x in centres) / MINI_LOTS

    for centre in centres:
        inter += calcul_distance(centre, [long_, lat_])

    return {"inertie_intra" : intra, "inertie_inter" : inter, "max" : max}



def scoring(ordoned_lots, inertie):
    try:
        distance_totale = 0
        distances_lots = [None for _ in range(MINI_LOTS)]
        score = 0
        k = 0
        for lot in ordoned_lots:
            distance_lot = 0
            for i in range(len(lot) - 1):
                distance_lot += calcul_distance(lot[i], lot[i+1])
            distances_lots[lot[i][3] - 1] = distance_lot
            score += ( 1000 / distance_lot) * (len(lot)) * (1000 / inertie["inertie_intra"][k])
            i += 1
        distance_totale = sum(distances_lots)
        return distances_lots, distance_totale, int(math.floor(score))
    except Exception as e:
        print('Erreur lors du calcul du score')
        print(e)
        return None





if __name__ == "__main__":
    
    """
    namefile = "GPS_points.csv"

    gps_positions = parser(namefile)

    #   naive_solution = naive_solver(gps_positions)

    genetic_solution = genetic_solver(gps_positions)

    #   print(genetic_solution)

    #   output_parser(naive_solution)

    """

    #   Récupération de la solution
    output_filename = "output.txt"
    lots = solution_parser(output_filename)

    #   Ordre des points en fonction des étiquettes
    ordored_lots = [None for _ in range(MINI_LOTS)] 

    for i in range(len(lots)):
        ordored_lots[i] = sorted(lots[i], key = lambda x: x[2])


    #   On a maintenant une liste de mini-lots ordonés
    
    #   Nous mésurons l'inertie inter du groupe et les inertiesintra de chaque lot

    res = calcul_inertie(ordored_lots)


    #   Calcul du score 
    distances_lots, distance_totale, score = scoring(ordored_lots, res)

    
    print("Les détails de distance sont : ")
    print(res)

    print("\n\n")
    print("Le score est", score)
