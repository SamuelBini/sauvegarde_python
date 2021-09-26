# # Algorithmes de cryptographie
import math as math


def pgcd(a,b):
    " Calcule le PGCD de deux nombres "
    if(b == 0 ):
        return a
    elif(b > a):
        return pgcd(b,a)
    else:
        return pgcd(b, a % b)


def isprim(n):
    " Vérifie si un nombre est premier "
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
    " Retrouve le 1er nombre premier plus grand que le nombre donné en paramètre "
    p=False
    n=N+1
    while(p!= True):
        p=isprim(n)
        if(p== False):
            n=n+1
    return n


def mod(a,b):
    " Retourne me restre de la division de a par b "
    n=a//b
    return a-n*b



class Ell:
    """ Classe permettant de définir et faire des opérations sur les courbes elliptiques """
    def __init__(self, a: int, b: int, n:int):
        """ Permet de définir une courbe élliptique à partir des paramètres a, b et n qui sont ous des entiers. On la défini selon la formule suivante : y2 = x3 + ax + b (mod p)
        """
        self.a = a
        self.b = b
        self.n = n

    def __repr__(self):
        return "E({}, {}, Z/{}Z)".format(self.a, self.b, self.n)

    def is_on_curve(self, p : tuple):
        " Retourne un boolen qui dit si un point appartient ou non à une courbe elliptique"
        y2 = p[1]**2 
        tamp = (p[0]**3 + self.a*p[0] + self.b) % self.n
        return y2 % self.n == tamp
    
    def add(self, p:tuple, q:tuple):
        " Additionne deux points sur une courbe élliptique "
        if p != q:
            alpha = (p[1] - q[1]) / (p[0] - q[0])
            x3 = (alpha ** 2 - p[0] - q[0]) % self.n
            y3 = ( -p[1] - alpha * (x3 - p[0])) % self.n
            return (x3, y3)
        elif p == q and p[0] != 0 :
            alpha = (3 * (p[0]**2) + self.a) / (2 * p[1])
            x3 = (alpha ** 2 - 2 * p[0]) % self.n
            y3 = ((alpha * ( p[0] - x3)) - p[1]) % self.n
            return (x3, y3)
        else:
            return (math.inf, math.inf)


    def mul(self, n : int, p : tuple):
        " Multiplie un point par un entier "
        for _ in range(1, n):
            p = self.add(p, p)
        return p




def chinese(x : int, p : int, y : int, q : int):
    " Retourne la solution n du système n = x (mod p) et n = y (mod q)"

    r, u, v = gcdex(q, p)
    if (x - y) % r != 0:
        #   Il n'y a pas de solutions
        return None
    return ((x * q * u + y * p * v) % (p * q)) // r



def eulerphi(n : int):
    " Retourne l'indicateur d'Euler d'un nombre "
    
    nbre = 1
    for i in range(2, n):
        if pgcd(i, n) == 1:
            nbre += 1
    return nbre


def gcdex(a : int, b : int) :
    " Calcule le PGCD r de a et b et retourne ce PGCD ainsi que les couples u et v tels que au+bv = r"
    c, x, y, c_prime, x_prime, y_prime = a, 1, 0, b, 0, 1
    
    while c_prime != 0:
        q = c // c_prime
        c, x, y, c_prime, x_prime, y_prime = c_prime, x_prime, y_prime, c - q * c_prime, x - q*x_prime, y - q * y_prime
    
    return (c, x, y)




def liste_premier_miroir_inf(n):
    lst_inf = []
    for i in range(1, n):
        if isprim(i) :
            mir = int(str(i)[::-1])
            if isprim(mir) and mir not in lst_inf :
                lst_inf.append(i)

    return lst_inf


def premier_miroir_sup(n):
    while True:
        nbre = nexprime(n)
        mir = int(str(nbre)[::-1])
        if isprim(mir) :
            return nbre
        else :
            n += 1

