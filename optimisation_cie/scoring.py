# -*- coding: utf-8 -*-

import math
import sys
from random import randint 
import random


MINI_LOTS = 7
RAYON_TERRE = 6371




def parser(fi):
    with open(fi, 'r') as fichier :
        a = fichier.read().split('\n')
        split_and_convert = lambda der : [float(der[0]), float(der[1])]
        b = [ split_and_convert(i.split(",")) for i in a[1:-1] ]

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




def solution_parser(file_name, with_zero = False):
    lots = [ [] for _ in range(MINI_LOTS)]
    with open(file_name, 'r') as file :
        for i in file.readlines():
            a = i.split(" ")
            position = [float(a[0]), float(a[1]), int(a[2]), int(a[3])]
            try:
                index = position[3] if with_zero else position[3] - 1
                lots[index].append(position)
            except AttributeError as e:
                print(e)
                print('Erreur dans les données de lots')
                return None
    return lots


def degreeToRadian(degre):
    return degre * math.pi / 180



def distance(lat1, lng1, lat2, lng2, coordinates):

    lat1 = degreeToRadian(lat1)
    lat2 = degreeToRadian(lat2)
    lon1 = degreeToRadian(lng1)
    lon2 = degreeToRadian(lng2)
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1

    a = (math.sin(d_lat/2.0))**2 + math.cos(lat1) * \
        math.cos(lat2) * (math.sin(d_lon/2.0))**2
    c = 2 * math.asin(math.sqrt(a))
    total_distance = RAYON_TERRE * c


    return total_distance


def calcul_distance(pointA, pointB):
    coordinates = {"LatLong": True, "XY": False}
    if pointA[0] == 0:
        pointA[0] = pointB[0]
    if pointA[1] == 0:
        pointA[1] = pointB[1]
    mh_dist = distance(pointA[0], pointA[1], pointB[0], pointB[1], coordinates) * 3280.84
    
    return mh_dist



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
            score += ( 1000000000 / distance_lot) * (len(lot)) * (1000000000 / inertie["inertie_intra"][k])
            i += 1
        distance_totale = sum(distances_lots)
        return distances_lots, distance_totale, int(math.floor(score))
    except Exception as e:
        print('Erreur lors du calcul du score')
        print(e)
        return None





if __name__ == "__main__":
    
    #   Récupération de la solution
    #   output_filename = "output.txt"
    output_filename = sys.argv[1]
    try:
        with_zero = sys.argv[2]
        with_zero = True
    except:
        with_zero = False
    
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
