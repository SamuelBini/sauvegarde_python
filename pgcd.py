import math as math
def pgcd(a,b):
    if(b ==0 ):
        return a
    elif(b > a):
        return pgcd(b,a)
    else:
        return pgcd(b,mod(a,b))
def isprim(n):
    a=math.floor(n**0.5)
    p=True
    if(n!=2 and n!=3):
        for i in range(2,a+1):
            if(mod(n,i) == 0):
                p=False
        return p
    else:
        return True
def nexprime(N):
    p=False
    n=N+1
    while(p!= True):
        p=isprim(n)
        if(p== False):
            n=n+1
    return n
def mod(a,b):
    n=a/b
    return math.floor((n-math.floor(n))*b)


