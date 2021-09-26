nbre_test = int(input())

for t in range(1, nbre_test + 1):
    n = int(input())
    str_nbres = str(input()).split(" ")

    nbres = [int(i) for i in str_nbres]

    cout = 0

    for i in range(1, len(nbres)):
        
        n1 = nbres[i-1]
        n2 = nbres[i]

        if n2 <= n1:
            ajout = 0
            s1 = str(n1)
            s2 = str(n2)
            l1 = len(s1)
            l2 = len(s2)
            ecart = l1 - l2 
            new_s2 = s2[:]

            if ecart > 0:
                n2 = n2 * (10**ecart)
                ajout += ecart
            
            s2 = str(n2)

            if ajout and n2 <= n1:
                if n2 <= n1 and n1 - n2 > (10**ajout) - 2:
                    s2 += "0"
                    ajout += 1
                    n2 = int(s2)

                elif n2 <= n1 and n1 - n2 < (10**ajout) - 1 :
                    n2 += n1 - n2 + 2

                else :
                    pass

            elif not ajout and n2 <= n1:
                n2 = int(s2 + "0")
                ajout += 1
            
            else :
                pass
            
            cout += ajout
            nbres[i] = n2
           

    print("Case #{}: {}".format(t, cout))