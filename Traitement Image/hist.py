#   Ce script permet de calculer l'histogamme de chaque image

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from luminance import luminance

def hist(img):
    hist = np.zeros(256)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            hist[img[i, j]] += 1

    return hist


if __name__=="__main__":

    image = cv.imread("img\Lena.png")

    ###     On transforme l'image en niveaux de gris
    y = luminance(image)


    ###     Fin de la transformation    ###


    histogramme = hist(y)
    plt.plot(histogramme)
    plt.show()
