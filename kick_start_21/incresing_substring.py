n_test = int(input())

for t in range(n_test):
    n = int(input())
    l = str(input())

    list_l = []
    nbre_l = 0
    for i in range(n):
        if i == 0:
            nbre_l = 1
        else :
            if ord(l[i-1]) < ord(l[i]):
                nbre_l += 1
            else :
                nbre_l = 1
        list_l.append(str(nbre_l))
    
    print("Case #{}: {}".format(t + 1, " ".join(list_l)))