#   Convertion d'une image en niveau de gris en utilisant la luminance

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



def luminance(img):
    
    #   La formule de la luminance est : Y = 0,299*R + 0,587*V + 0,114*B

    #   On recupère les 3 matrices et nous appliquons la formule
    b,v,r = cv.split(img)
    y = 0.299*r + 0.587*v + 0.114*b

    #   On transforme les réels en octets
    y = y.astype(np.uint8)

    return y


if __name__ == "__main__":

    image = cv.imread("img\Lena.png")

    Y = luminance(image)

    plt.title("Luminance Y")
    plt.imshow(Y, cmap="gray")
    plt.show()
