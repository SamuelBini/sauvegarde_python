#   Dans ce script, nous modifions les composantes couleurs d’une image : le quart 
#   supérieur gauche du haut effacera la première composante de chaque triplet, le quart 
#   supérieur droit du haut effacera la deuxième composante de chaque triplet, le quart 
#   inférieur gauche du bas effacera la troisième composante, et le quart inférieur 
#   droit de l’image restera intact tel quel.


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
	
	img = cv.imread("img\Lena.png")
	img = img[..., ::-1]
	
	#   On accède au côté gauche de l'image
	for i in range(0, img.shape[0] // 2):
	    #   On accède au côté supérieur gauche de l'image
	    for j in range(0, img.shape[1] // 2):
	        img[i, j, 0] = 0
	    
	    #   On accède au côté inférieur gauche de l'image
	    for j in range(img.shape[1] // 2, img.shape[1]):
	        img[i, j, 2] = 0
	
	#	   On accède au côté droit de l'image
	for i in range(img.shape[0] // 2, img.shape[0]):
	    #   On accède au côté supérieur droit de l'image
	    for j in range(0, img.shape[1] // 2):
	        img[i, j, 1] = 0
	    
	
	#   On affiche enfin l'image obtenue
	
	plt.title("Photo de Lena modifiée")
	plt.imshow(img)
	plt.show()