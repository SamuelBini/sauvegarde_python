#   Ce script permet d'égaliser un histogramme de sorte à 
#   corriger une image qui manque de constraste

from os import system
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from luminance import luminance
from hist import hist


def histCumulNorm(img):
    """ Calcul l'histogramme cumulé et le normalise
        Retourne les histogrammes normal et cumulé
    """
    h = hist(img)

    hc = np.zeros(256)
    for i in range(0, 256):
        hc[i] = h[i] + hc[i-1]

    nbpixels = img.size
    hc = (hc / nbpixels) * 255

    return h, hc


def transforHistCumule(img):
    "   Transforme une image avec les bonnes proportions de gris en egalisant son histogramme de pixels"
    #   Transformation de l'image avec l'histogramme cumulé

    #   Calcul des histogrammes
    histo, histoCumul = histCumulNorm(img)

    #   Affichage des graphes
    plt.plot(histo)
    plt.show()

    plt.plot(histoCumul)
    plt.show()

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            img[i, j] = histoCumul[ img[i, j] ]

    return img

    


if __name__=="__main__":
    image = cv.imread("img\mountain.png")

    #plt.imshow(image)
    #plt.title("Image originale")
    #plt.show()

    #   Affichage de l'image transformée par luminescence
    image = luminance(image)
    cv.imshow("Image modifiée par luminance", image)

    #   Tranformation de l'image avec l'histogramme cumulé
    image = transforHistCumule(image)

    cv.imshow("Image après égalisation de l'histogramme", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    

