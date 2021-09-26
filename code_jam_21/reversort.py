nbre_test = int(input(""))

def reversort(L : list):
    cost = 0
    for i in range(1, len(L)):
        j = L.index(min(L[i-1:])) + 1
        L[i-1 : j] = reversed(L[i-1 : j])
        cost += j - i + 1
        if L == reversed(L):
            break
    return cost

for i in range(nbre_test):
    nbre_elements = input()
    tab_ = input("").split(" ")
    tab_int = [ int(k) for k in tab_]
    cost = reversort(tab_int)
    print("Case #{}: {}".format(i + 1, cost))

    