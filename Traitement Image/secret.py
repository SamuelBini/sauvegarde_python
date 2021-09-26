#   Ce script permt de cache une image dans une autre
#   Pour cela l'image à cacher est un nuances de gris et
#   on modifie le dernier bit du plan B

import cv2 as cv
import numpy as np


def cacherImage(img, imgToHide):

    #   Redimensionnement de l'image à cacher en cas de différence de taille
    imgToHide = cv.resize(imgToHide, (img.shape[1], img.shape[0]))

    #   On vérifie si l'image est en couleur ou en niveaux de gris
    if len(img.shape) == 3:
        #   On separe les composantes et on supprime le bit de poids faible
        b, v, r = cv.split(img)
        b = b & 0b11111110


        #   On ajoute le bit de l'image à cacher dans le plan b
        b = b | (imgToHide > 0) ^ (v&1)

        #   Sauvegarde de la nouvelle image
        img = cv.merge((b, v, r))
    
    else:
        #   On supprime le dernier bit et on ajoute celui de l'image à cacher
        img = img & 0b11111110
        img = img | imgToHide > 0

    return img



def decouvrirImage(img):
    
    #   On vérifie si l'image est en couleur ou en niveau de gris
    if len(img.shape) == 3:
        #   On separe les composantes et on recupère le bit de poids faible
        b, v, r = cv.split(img)
        b = (b & 1) ^ (v & 1)

        img = b * 255

    else:
        #   On supprime le dernier bit et on ajoute celui de l'image à cacher
        img = img & 1

        img = img * 255

    return img




if __name__=="__main__":
    
    print("\n\n**********\t-----\tBienvenue à l'infoSecrete\t-----\t**********\n\n\n\n")
    
    while True:
    
        print("\tVoulez-vous :\n\t\t1-\tCrypter une image\n\t\t2-\tDecypter une image\n\t\t3-\tQuitter")
    
        choix = input("\n\n\t==> ")
        if choix != "1" and choix != "2":
            print("Veuillez entrer un caractère valide")
            continue
    
        choix = int(choix)

        if choix == 1:
            #imageAcacher = input("\n\tVeuillez entrer le lien de l'image à crypter : ")
            #imageAcacher = imageAcacher.split("\\")
            #print(imageAcacher)
            #image = input("\n\tVeuillez entrer le lien de l'image de couverture : ")
            #repImageDef = input("\n\tVeuillez entrer le repertoire où enregistrer #l'image cryptée (Ne rien rentrer si c'est le repertoire courant) : ")
            #nomImageDef = input("\n\tVeuillez entrer le nom de l'image cryptée : ")
            #pathDef = repImageDef + "\\" + nomImageDef
            
            #del(repImageDef, nomImageDef)
            
            image = "img\\Lena.png"
            imageAcacher = "img\\messageAcacher.png"
            image = cv.imread(image)
            imageAcacher = cv.imread(imageAcacher, 0)

            newImage = cacherImage(image, imageAcacher)

            cv.imwrite("zazaza.png", newImage)

            print("CRYPTAGE REUSSI")

        else:
            image = input("\n\tVeuillez entrer le lien de l'image à decrypter : ")
            repImageDef = input("\n\tVeuillez entrer le repertoire où enregistrer l'image décryptée (Ne rien rentrer si c'est le repertoire courant) : ")
            nomImageDef = input("Veuillez entrer le nom de l'image décryptée : ")

            image = decouvrirImage(image)

            print("DECRYPTAGE REUSSI")
