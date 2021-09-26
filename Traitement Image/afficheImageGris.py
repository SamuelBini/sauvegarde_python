import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def main():

	##  Affichage de la matrice image en couleur
	#matrice = cv.imread("Lena.png")
	#plt.imshow(matrice[..., ::-1])
	##   On peut aussi utiliser
	#plt.imshow(cv.cvtColor(matrice, cv.COLOR_BGR2RGB))
	#plt.title("Image de Lena")
	#plt.show()



	##  Affichage de la matrice image en blanc et noir
	matrice = cv.imread("img/Lena.png")
	print(matrice.shape)
	matrice = cv.cvtColor(matrice, cv.COLOR_BGR2GRAY)
	plt.imshow(matrice, cmap="gray")
	plt.show()


if __name__ == '__main__':
	main()