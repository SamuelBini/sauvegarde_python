

def calcul_frequence(mot : str):
    
    mot = mot.capitalize()
    dict_freq = [0 for _ in range(26)]
    for i in set(mot):
        dict_freq[i] = mot.count(i) / len(mot)
    
