import random
import math
from threading import Thread
from multiprocessing import Queue


from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=100)


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

def initier(nombre, maxi, taille):
    return [ random.choices(population = range(maxi), k = taille) for _ in range(nombre)]

def moyenne_fitness(ind, vehicules, steps, streets, bonus):
    total = 0
    for solution in ind :
        total = total + score(solution, vehicules, steps, streets, bonus)
    return total/len(ind)

def ranger_individus(ind, vehicules, steps, streets, bonus):
    rang = []
    queues = [None] * len(ind)
    calcul_scores = []
    len_ind = len(ind) 
    for i in range(len_ind):
        calcul_scores.append(Thread(target=score, args=(ind[i], vehicules, steps, streets, bonus, queues, i)))
    for i in calcul_scores:
        i.start()
    for i in calcul_scores:
        i.join()
    for i in range(len_ind):
        score_i = queues[i]
        #print("score_i", i,":", score_i)
        rang.append((ind[i], score_i))
    return sorted(rang, key = lambda x:x[1], reverse=True)

def evoluer_population(population, vehicules, steps, streets, bonus) :
    raw_population_rangee = ranger_individus(population, vehicules, steps, streets, bonus)
    rang_moyen = 0
    chance_retenu_bon = 0.3
    chance_retenu_mauvais= 0.05
    chance_mutation = 0.1
    taille = len(streets)
    nombre = len(raw_population_rangee)
    population_rangee = []
    maxi = min(100, steps)
    for individu, fitness in raw_population_rangee:
        rang_moyen += fitness
        population_rangee.append(individu)
    rang_moyen /= nombre
    solution = population_rangee[0]
    meilleur_fitness = raw_population_rangee[0][1]
    parents = population_rangee[: int(nombre * chance_retenu_bon)]

    for individu in population_rangee[int(nombre * chance_retenu_bon) :]:
        if random.random() < chance_retenu_mauvais :
            parents.append(individu)
    for individu in parents :
        if random.random() < chance_mutation:
            place_modifier = int(random.random() * taille)
            individu[place_modifier] = random.choice(range(maxi))
    taille_parent = len(parents)
    nombre_premiers = int(taille_parent * 0.3)
    taille_desire = nombre - taille_parent
    enfants = []
    while len(enfants) < taille_desire:
        pere = random.choice(parents)
        mere = random.choice(parents)
        taille_coupure = random.randint(0, taille - 1)
        if True: #pere != mere
            enfant = pere[:taille_coupure] + mere[taille_coupure :]
            enfants.append(enfant)
    parents.extend(enfants)
    return parents, rang_moyen, solution, meilleur_fitness
    

def solver(data) :
    rues = data['streets']
    b = algo_genetique(data['vehicules'], data['duration'], rues, data['bonus'])
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

def algo_genetique(vehicules, steps, streets, bonus):
    print("Start")
    population = initier(100, 4, len(streets))
    moyenne_score = moyenne_fitness(population, vehicules, steps, streets, bonus)
    print('moyenne fitness debut : {}'.format(moyenne_score))
    i = 0
    solution = None
    log_avg = []
    while i < 10000:
        population, moyenne_score, solution, meilleur_fitness = evoluer_population(population,vehicules,steps, streets, bonus)
        if i & 255 == 255:
            print('Moyenne fitness actuelle: %.2f' % moyenne_score, 'meilleure fitness %d' % meilleur_fitness, '(%d generations)' % i)
        if i & 31 == 31:
            log_avg.append(moyenne_score)
        i += 1

    """
    line_chart = pygal.Line(show_dots=False, show_legend=False)
    line_chart.title = 'Fitness evolution'
    line_chart.x_title = 'Generations'
    line_chart.y_title = 'Fitness'
    line_chart.add('Fitness', log_avg)
    line_chart.render_to_file('bar_chart.svg')
    """
    return solution

def score(solution, vehicules, steps, streets, bonus, queue = None, index = None):
    fin_rue= dict(zip(streets.keys(), solution))
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


a = ['e.txt']
for b in a:
    d = solver(parser(b))
    writer(d, b)

'''
d = parser('a.txt')
print(d)
solver(d)'''