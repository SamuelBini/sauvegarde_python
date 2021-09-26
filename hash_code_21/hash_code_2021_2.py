import random
import math
from threading import Thread
from multiprocessing import Queue



def parser(fi):
    with open(fi, 'r') as fichier :
        a = fichier.read().split('\n')
        streets = {}
        vehicules = []
        [duree, intersects, street, cars_numb, bonus] = a[0].split(' ')
        for line in a[1:int(street)+1]:
            [start_intersec, end_intersec, street_name, time_to_cross] = line.split(' ')
            s = {'name' : street_name, 'start':int(start_intersec), 'end':int(end_intersec), 'cross' : int(time_to_cross)}
            streets[street_name] = s
        for line in a[int(street) +1: int(cars_numb)+1+int(street)]:
            dat = line.split(' ')
            v = {'number_streets': int(dat[0]), 'streets_names':dat[1:]}
            vehicules.append(v)
    return({'duration':int(duree), 'intersections' : int(intersects), 'bonus':int(bonus), 'vehicules':vehicules, 'streets': streets })



def writer(data, name):
    lines = []
    lines.append(str(data['scheduled']))
    for k, val in data['intersections'].items():
        lines.append(str(k))
        lines.append(str(val["incomming_streets"]))
        for j in val["streets"] :
            lines.append(j["name"] + " " + str(j["secondes"]))
    lines = "\n".join(lines)
    with open(name +'_w','w') as fichier:
        fichier.writelines(lines)

'''writer({'scheduled' : 1, 'intersections':[{"intersection_numb": 1, "incomming_streets": 2,
         'streets' : [{"street" :"rue-d-athenes", "secondes" : 2}, {"street" :"rue-d-amsterdam", "secondes" : 1}] }]}, 'a.txt')
'''

def initier(maxi, taille):
    return [ random.randint(0, maxi) for _ in range(taille)]


def solver(data) :
    rues = data['streets']
    b = recuit_simule(data['vehicules'], data['duration'], rues, data['bonus'])
    s = 0
    intersections = {}
    for index, (key, c) in enumerate(rues.items()) :
        if b[index] != 0 :
            try:
                intersections[str(c['end'])]
            except :
                intersections[str(c['end'])] = {}
                intersections[str(c['end'])]['streets'] = []     
            intersections[str(c['end'])]['streets'].append({'name': c['name'], 'secondes' : b[index]})
            intersections[str(c['end'])]['incomming_streets'] = len(intersections[str(c['end'])]['streets'])
            s = s + 1

    solution  = {'scheduled' : len(intersections), 'intersections':intersections}
    return(solution)


def recuit_simule(vehicules, steps, streets, bonus):
    print("Start")
    solution = initier(5, len(streets))
    temperature = 10000

    i = 0
    while temperature > 0:
        nbre_voisins = 20
        voisins = recherche_voisins(solution, nbre_voisins, 5)
        voisin_ideal = random.choice(voisins)
        cout_s = score(solution, vehicules, steps, streets, bonus)
        cout_v = score(voisin_ideal, vehicules, steps, streets, bonus)
        
        p_voisin = P(temperature, cout_s, cout_v)
        r = random.random()

        if r < p_voisin :
            solution = voisin_ideal

        if i % 1000 == 0:
            cout_s = cout_s if cout_s < cout_v else cout_s
            #print("\n\nLa configuration actuelle est : {}".format(solution))
            print("Son coût est : {}".format(cout_s))
            print("La température est :", temperature)
            print("\n\n")
        temperature -= 0.01
        i += 1

    return solution

             

def P(T, cout_s, cout_s_prime):
    return math.exp((cout_s - cout_s_prime) / T )

def recherche_voisins(config, nbre_voisins, max):
    #   Génération de voisins
    len_config = len(config)
    voisins = [random.sample(config, len_config) for _ in range(nbre_voisins)]

    #   Mutation sur des voisins
    mutants = 0.5
    voisins_mutants = [ random.randint(0, nbre_voisins - 1) for _ in range(int(nbre_voisins * mutants) - 1) ]

    for i in voisins_mutants:
        taux_mutation = 0.4
        index_mutations = [ random.randint(0, len(config    ) - 1) for _ in range(int(taux_mutation * len_config) - 1)]
        for j in index_mutations:
            voisins[i][j] = random.randint(0, max)

    return voisins



def score(solution, vehicules, steps, streets, bonus, queue = None, index = None):
    fin_rue = dict(zip(streets.keys(), solution))
    score = 0
    for v in vehicules:
        time = 0
        for rue in v['streets_names']:
            if(fin_rue[rue] == 0):
                time = math.inf
                break
            time = time + streets[rue]['cross']
            tour = time // fin_rue[rue]
            rouge = tour % 2
            if(rouge):
                time = (tour+1)*fin_rue[rue]
        if(time<steps):
            score = score + 1000 + (steps - time)
    if queue is not None:
        queue[index] = score
    else :
        return score

if __name__=="__main__":
    a = ['e.txt']
    for b in a:
        d = solver(parser(b))
        writer(d, b)

    '''
    d = parser('a.txt')
    print(d)
    solver(d)'''



