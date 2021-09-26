#   Ce script permet de passer d'une image à son négatif

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
	main()

def main():
	#   Image en couleur
	image = cv.imread("img\Lena.png")

	img = 255 - image

	plt.imshow(img, cmap="gray")
	plt.show()


	#   Image en noir et blanc
	image = cv.imread("img\Lena.png", 0)
	img = 255 - image

	plt.imshow(img, cmap="gray")
	plt.show()