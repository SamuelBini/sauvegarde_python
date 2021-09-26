nbre_test = int(input())

for t in range(1, nbre_test + 1):
    n = int(input())
    str_nbres = str(input()).split(" ")

    nbres = [int(i) for i in str_nbres]

    cout = 0
    for i in range(len(nbres)):
        if i == 0 :
            pass
        else :
            if nbres[i] <= nbres[i - 1]:
                ajout = 0
                n1 = nbres[i-1]
                n2 = nbres[i]
                s1 = str(nbres[i-1])
                s2 = str(nbres[i])
                l1 = len(s1)
                l2 = len(s2)
                ecart = l1 - l2 

                new_s2 = s2[:]
                if ecart > 0:
                    for j in range(ecart):
                        j_ = ecart - j
                        j_moins = -j_
                        for_add = int(s1[:j_moins]) // (10 ** j_)
                        if j_ == 1 and for_add == 1:
                            for_add = 0
                        new_s2 += str(for_add)
                        ajout += 1

                n2 = int(new_s2)
                s2 = new_s2[:]

                if ajout and n2 <= n1 and n1 - n2 > (10**(ajout - 1)) - 2:
                    new_s2 += "0"
                    ajout += 1
                    n2 = int(new_s2)
                elif ajout and n2 <= n1 and n1 - n2 <= (10**(ajout - 1)) - 2:
                    n2 = n1 - n2 + 2
                elif not ajout and n2 <= n1:
                    s2 += "0"
                    n2 = int(s2)
                    ajout += 1
                else :
                    pass
                
                cout += ajout
                nbres[i] = n2
           

    print("Case #{}: {}".format(t, cout))