import random

liste1 = [1, 2, 3, 4]
liste2 = ['a', 'b', 'c', 'd']

liste = [ (a, b) for a, b in zip(liste1, liste2)]

print("Liste 2 : {}\n".format(liste))
