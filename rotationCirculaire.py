#   Programme qui détermine le plus petit entier auquel si on fait une 
#   permutation circulaire donne celui-ci multiplié par 1.5


i = 10

while True:
    i += 1
    s = str(i)
    k = s[1:] + s[0]
    k = int(k)
    if k == k * 1.5 :
        break 

print("L'entier recherché est : ", k)