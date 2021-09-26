#   Affichage de l'image avec la librairie opencv

import cv2 as cv

def main():
	matrice = cv.imread("img/Lena.png")

	matG = cv.cvtColor(matrice, cv.COLOR_BGR2GRAY)  #   Conversion des triplets BVR en gris

	cv.imshow("Image de Lena", matrice)
	cv.waitKey(0)
	cv.destroyAllWindows()


if __name__ == '__main__':
	main()
