# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlApplicationEngine

class UTools():    
    def __init__(self):
        self.us1 = "QML with Python."
        
    def u_qml(self):       
        self.qwid = QQmlApplicationEngine()        
        self.qwid.load(QUrl('u_qml.qml'))
        

if __name__ == "__main__":    

    ut = UTools()