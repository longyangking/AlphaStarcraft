import numpy as np 
import threading
from . import nativeUI

import sys
from PyQt5.QtWidgets import QApplication
#from PyQt5.QtCore import * 
#from PyQt5.QtGui import *

class UI(threading.Thread):
    def __init__(self,pressaction,area,sizeunit=30):
        threading.Thread.__init__(self)
        self.UI = None
        self.app = None

        self.area = area
        self.sizeunit = sizeunit
        self.pressaction = pressaction
    
    def run(self):
        print('Init UI...')
        self.app = QApplication(sys.argv)
        self.UI = nativeUI.nativeUI(pressaction=self.pressaction,area=self.area,sizeunit=self.sizeunit)
        self.app.exec_()

    def setarea(self,area):
        return self.UI.setarea(area=area)
    
    def gameend(self,score):
        self.UI.gameend(score=score)