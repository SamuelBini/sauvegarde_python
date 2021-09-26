import threading
import psutil
from random import randint, random
import time



#   Liste contenant les projets terminés
ended_processes = []



class Liste:
    """
    Cette classe instancie un objet représentant un élément de liste
    """

    def __init__(self, info=None, suivant=None):
        self.info = info
        self.suivant = suivant

    def __str__(self):
        return "Info : {}".format(self.info)


#   Méthode pour les différentes listes 
def afficherListe(liste):
    p = liste
    while p is not None:
        print(p.info)
        p = p.suivant


def enfiler(liste : Liste, element : Liste):
    p = liste
    if liste is None:
        return element
    else :
        element.suivant = None
        while p.suivant is not None:
            p = p.suivant
        p.suivant = element
        return liste


def defiler(liste : Liste):
    if liste is None:
        pass
    else :
        p = liste
        liste = liste.suivant
        return liste


def defiler_et_sauver(liste : Liste):
    if liste is None:
        pass
    else :
        p = liste
        liste = liste.suivant

        return liste, p





class Processus:
    "   Classe permettant la gestion des processus  "
    def __init__(self, process):
        self.pid = process.pid if process.pid else None
        self.name = process.name if process.name else None
        self.started = process.started if hasattr(process, 'started') else time.time()
        self.working_time = process.working_time if hasattr(process, 'working_time') else None
        self.end_time = None

    def setWorkingTime(self, time):
        "   Ajoute une durée d'exécution au proceessus  "
        self.working_time = time

    def setEndTime(self, time):
        "   Ajoute un temps de fin d'exécution au processus "
        self.end_time = time



class Serveur:
    "   Classe permettant la gestion des serveur de notre système   "
    def __init__(self, numero):
        self.numero = numero
        self.file = None
        self.quantum = 10

    def addProcess(self, process):
        "   Ajoute un processus au serveur"
        elemnt = Liste(process)
        print(elemnt)
        self.file = enfiler(self.file, elemnt)

    def run(self) :
        #   Exécution du serveur pendant 100 quantums de temps
        temps = 100

        print("Début d'un serveur")
        while self.file is not None :
            temps -= 10
            print(temps)
            self.file, element = defiler_et_sauver(self.file)
            print("Traitement")
            element.info.working_time = element.info.working_time - self.quantum if element.info.working_time > self.quantum else 0
            print("Vérif")
            if element.info.working_time == 0:
                print("Fini")
                element.info.setEndTime(time.time())
                ended_processes.append(element)
                #   processus_connus.remove(element)
            else :
                print("Not yet")
                #   print(self.file.suivant)
                self.file = enfiler(self.file, element)
                print("Fin enfilage")
            print("Next")
            print(temps)

        print("Fin d'un serveur")



def tri_processus(process_list: list, connus: list):
    "   Renvoie la liste des processus qui ne sont pas encore dans le système   "
    inconnus = [p if p not in connus else None for p in process_list]

    return inconnus


def format_process(processes):
    "   Renvoie une liste de processus formatés en les transformant avec la classe créée à cet effet"
    if type(processes) == list:
        new_list = []
        for i in processes:
            #   On ajoute un temps d'exécution
            Processus(i)
            new_list.append(Processus(i))
        return new_list
    else :
        return Processus(processes)


def attributionServeur(processus : list, serveurs : Serveur):
    "   Attribue une liste de processus aux différents serveurs du système  "
    print("Longeur du processus")
    
    for i in processus:
        r = random()
        if r < 0.25:
            serveurs[0].addProcess(i)
        elif r < 0.5:
            serveurs[1].addProcess(i)
        elif r < 0.75:
            serveurs[2].addProcess(i)
        else:
            serveurs[3].addProcess(i)
    
    print(serveurs[0].file)
    return serveurs






if __name__ == "__main__":


    #   Création de chaque seveur
    print("Début du programme")
    serveur_1 = Serveur(1)
    serveur_2 = Serveur(2)
    serveur_3 = Serveur(3)
    serveur_4 = Serveur(4)

    liste_serveurs = [serveur_1, serveur_2, serveur_3, serveur_4]


    #   Variables utiles
    processus_connus = []


    #   Début de la boucle

    #   Observatiopn du système pendant un certain temps
    fin = time.time() + 30

    while time.time() < fin :

        #   Récupération des processus en cours
        print("\n\nRécupération des processus en cours")
        process_list = [p for p in psutil.process_iter()]
        

        #   print(process_list)
        #   Formatage des processus
        print("\n\nFormatage des processus")
        process_list = format_process(process_list)

        #   Extraction des processus qui sont pas encore dans le système
        print("\n\nExtraction des processus qui sont pas encore dans le système")
        processus_inconnus = tri_processus(process_list, processus_connus)

        #   Attribution d'un temps de traitement à chauqe nouveau processus
        print("\n\nAttribution d'un temps de traitement à chauqe nouveau processus")
        for p in processus_inconnus:
            p.working_time = randint(1, 100000)

        processus_connus = processus_connus + processus_inconnus

        #   print("Inconnus")
        #   print(processus_inconnus)


        #   Attribution des processus à chaque serveur de manière aléatoire
        #   On génère un nombre de manière aléatoire et on la compare à un seuil pour l'assigner
        #   à chaque processus
        print("\n\nAttribution des processus au serveur")
        liste_serveurs = attributionServeur(processus_inconnus, liste_serveurs)

        print("\n\nFile du serveur 1")
        print(liste_serveurs[0].file)


        print("\n\nDébut du traitement")

        for serveur in liste_serveurs:
            serveur.run()

        print("\n\nFin d'un tour")

    print("\n\nFin du traitement")


    #   Calcul des différents indicateurs
    print("Début du calcul des indicateurs")


    #   On commence par calculer le temps moyen de traitement
    temps_traitement = 0
    for i in ended_processes:
        temps_traitement += i.end_time - i.started
    
    tmps_moyen_traitement = temps_traitement / len(ended_processes)


    print("\n\n\n\n\n\n\n")
    print("******************   CALCUL DES INDICATEURS  ******************")
    print("\n\n")

    print("Le temps moyen de traitement est de {} sécondes".format(tmps_moyen_traitement))


    #   Calcul du temps inter-arrivée
    list_arrivee = []
    for i in ended_processes:
        list_arrivee.append(i.started)
    list_arrivee.sort()
    temps_inter_arrivee = (list_arrivee[len(list_arrivee)] - list_arrivee[0]) / len(list_arrivee)
    print("\n\nLe temps moyen inter-arrivée est de {} sécondes".format(tmps_moyen_traitement))


    #   Calcul du taux d'utilisation de chaque serveur
    taux_utilisation = (temps_inter_arrivee / ( 4 * tmps_moyen_traitement )) * 100
    print("\n\nLe taux d'utilisation des serveur est {}%".format(taux_utilisation))


