# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from u_tools import UTools

class UApp(QtWidgets.QWidget, UTools):    
    def __init__(self, parent=None):        
        QtWidgets.QWidget.__init__(self, parent)        
        UTools.__init__(self)        
        self.start_qml()    
        
    def start_qml(self):        
        self.u_qml()
        
if __name__ == "__main__":    
    import sys    
    app = QtWidgets.QApplication(sys.argv)    
    uap = UApp()    
    # uap.show()    
    sys.exit(app.exec_())