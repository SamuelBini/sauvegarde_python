
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decale_gauche(mot):
    n_mot = ""
    for i in mot:
        n_mot += alpha[alpha.index(i) - 1]

    return n_mot


def decale_droite(mot):
    n_mot = ""
    for i in mot:
        if i == "Z":
            n_mot += "A"
        else :
            n_mot += alpha[alpha.index(i) + 1]

    return n_mot

