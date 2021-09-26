import sys
from PySide2.QtCore import *
from PySide2.QtGui import *


if __name__ == "__main__":
    
    #   Création de l'application principale
    myApp = QGuiApplication(sys.argv)

    #   Création d'une étiquette et de ses propriétés
    appLabel = QLabel()
    appLabel.setText("Salut le monde!!! \nVoici ma première appliation avec PySide")
    appLabel.setAlignement(Qt.AlignCenter)
    appLabel.setWindowsTitle("Ma Première App")
    appLabel.setGeometry(300, 300, 250, 175)

    #   On montre l'étiquette
    appLabel.show()

    #   Exécution de l'app et on quitte
    myApp.exec_()
    sys.exit()
