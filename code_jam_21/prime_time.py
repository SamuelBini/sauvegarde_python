import itertools
  
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

nbre_test = int(input())

for t in range(1, nbre_test + 1):
    m = int(input())

    deck = {}
    set_pions = []
    for _ in range(m):
        p, n = tuple(input().split(" ")) 
        p, n = int(p), int(n)
        set_pions.append(p)
        deck[p] = n

    set_pions = set(set_pions)

    for i in range(1, len(deck)):
        liste_sousens_g = findsubsets(set_pions, i)
        liste_sousens_d = []
        for j in liste_sousens_g:
            liste_sousens_d.append(set_pions - set(j))

        print("\n\n\nSous ensemble gauche : ")
        print(liste_sousens_g)

        print("\nSous ensemble droit : ")
        print(liste_sousens_d)

    """
    total_somme = 0
    total_produit = 0

    g1 = []
    g2 = []
    for i in deck:



    print("Case #{}: {}".format(t, cout))
    """