from math import sqrt

n_test = int(input())

lst_prem = [2, 3]

def next_prime(n):
    np = []
    i = n
    while i < 500:
        i+=1
        j = n + i
        val_is_prime = True
        if j not in lst_prem and j > max(lst_prem):
            lst_p = []
            if int(sqrt(n)) + 1 < max(lst_prem):
                lst_p = lst_prem[:]
            else :
                lst_p = lst_prem + range(max(lst_prem) + 1, int(sqrt(n)) + 2)
            for x in lst_p:
                if j % x == 0:
                    val_is_prime = False
                    break
        elif j not in lst_prem and j < max(lst_prem):
            val_is_prime = False
            break

        if val_is_prime and j not in lst_prem:
            lst_prem.append(j)
            np.append(j)

    return min(np)


for t in range(n_test):
    n = int(input())
    number = int(input())

    i, j = 2, 3
    code = i*j
    last_code = None
    while True:
        if code > number:
            break
        elif code == number:
            last_code = code
            break
        else :
            last_code = code
            i, j = j, next_prime(j)
            code = i * j

    print("Case #{}: {}".format(t + 1, last_code))