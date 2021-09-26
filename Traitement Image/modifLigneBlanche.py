import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

	matrice = cv.imread("img\Lena.png")
	
	for i in range(0, matrice.shape[0]):
	    matrice[i, 100] = [255, 255, 255]
	
	plt.imshow(matrice[..., ::-1])
	plt.show()

