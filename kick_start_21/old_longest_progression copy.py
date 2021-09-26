n_test = int(input())

for t in range(n_test):
    n = int(input())
    l_s = str(input()).split(" ")

    l = [int(i) for i in l_s]

    longest = 1
    has_change = False
    old_s = None

    i = 1
    change_indice = None
    d_l = l[:]
    set_longest = set()
    while i < n:
        s = l[i-1] - l[i]
        if old_s is None:
            old_s = s
        else :
            if not has_change and old_s != s:
                l[i] = l[i-1] - old_s
                has_change = True
                change_indice = i
            elif has_change and old_s != s :
                has_change = False
                i = change_indice + 1
                set_longest.add(longest)
                longest = 1
                old_s = None
                l = d_l[:]
                continue
            else :
                pass
        longest += 1
        i += 1
    set_longest.add(longest)
    y = max(set_longest)
    print("Case #{}: {}".format(t + 1, y))