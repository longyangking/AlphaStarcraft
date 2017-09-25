import sys  
from PyQt5 import QtWidgets,QtGui 

import numpy as np 
import sys
from PyQt5.QtWidgets import QWidget, QApplication,QDesktopWidget,QLabel
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

class nativeUI(QWidget):
    playsignal = pyqtSignal(int) 

    def __init__(self,pressaction,size):
        super(nativeUI,self).__init__(None)

        self.area = None        
        self.size = size

        self.pressaction = pressaction
        self.playsignal.connect(self.pressaction) 

        self.isgameend = False
        self.score = 0
        self.initUI()

    def initUI(self):
        (Nx,Ny) = self.size
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()

        self.setGeometry((screen.width()-size.width())/2, 
                        (screen.height()-size.height())/2,
                        Nx, Ny)
        self.setWindowTitle("Starcraft")

        label = QLabel('', self)
        movie = QtGui.QMovie("./resources/images/unit/0_firebat_atk0.gif")
        label.setMovie(movie)
        movie.start() 

        
        # set Background color
        palette =  QPalette()
        palette.setColor(self.backgroundRole(), QColor(255,255,255))
        self.setPalette(palette)
        
        #self.setMouseTracking(True)
        self.show()

    def setarea(self,area):
        self.area = area
        self.update()

    def paintEvent(self, e):
        
        
        qp = QPainter()
        qp.begin(self)
        

        qp.drawPixmap(0,0,256,256,QtGui.QPixmap('./resources/images/background.jpg'))
        qp.end()
        
         
    def resizeEvent(self,e):
        pass

    def gameend(self,score):
        pass
        self.update()

    def drawresult(self,qp):
        pass

    def drawArea(self,qp):
        pass

    def closeEvent(self,e):
        pass

    def keyPressEvent(self, e):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    area = np.random.randint(-1,2,size=(10,10))
    size = [300,300]
    ex = nativeUI(pressaction=lambda x:x,size=size)
    
    sys.exit(app.exec_())
