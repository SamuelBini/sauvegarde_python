def reversort(L : list):
    cost = 0
    for i in range(1, len(L)):
        j = L.index(min(L[i-1:])) + 1
        L[i-1 : j] = reversed(L[i-1 : j])
        cost += j - i + 1
        if L == reversed(L):
            break
    return cost

if __name__=="__main__":
    nbre_test = int(input(""))

    for n in range(nbre_test):
        nbre_elements, cout = input("").split(" ")
        nbre_elements, cout = int(nbre_elements), int(cout)
        
        if cout < nbre_elements - 1 :
            solution = []
        elif cout > (nbre_elements - 2 + 1) * (nbre_elements + 2) / 2 :
            solution = []
        else :
            i = 0
            tab_int = [j for j in range(1, nbre_elements + 1)]
            solution = tab_int[:]
            cout_rest = cout - (nbre_elements - 1)
            ind_deb = 1
            ind_fin = nbre_elements
            fin = False
            while i < nbre_elements and cout_rest > 0:
                cout_rest += 1
                if cout_rest > nbre_elements - i:
                    tab_int[ind_deb - 1 : ind_fin ] = reversed(tab_int[ind_deb - 1 : ind_fin])
                    if not fin:
                        ind_fin -= 1
                    else :
                        ind_deb += 1
                    cout_rest = cout_rest - (nbre_elements - i)
                else :
                    if fin:
                        j = ind_fin - cout_rest
                        tab_int[j : ind_fin] = reversed(tab_int[j : ind_fin]) 
                    else :
                        j = ind_deb + cout_rest - 1
                        tab_int[ind_deb - 1 : j] = reversed(tab_int[ind_deb - 1 : j]) 
                    l_ = tab_int[:]
                    solution = tab_int[:]
                    #print(cout, " ==> ", reversort(l_))
                    break

                    

                fin = not fin
                i += 1




        if len(solution) != 0:
            tab_ = [str(i) for i in solution]
            tab_ = " ".join(tab_)
        else :
            tab_ = "IMPOSSIBLE"
        print("Case #{}: {}".format(n + 1, tab_))

