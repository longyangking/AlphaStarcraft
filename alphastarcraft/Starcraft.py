import numpy as np 
import core
import ui

class Starcraft:
    def __init__(self)：
        self.core = core.GameCore()


    def start(self):
        self.core.start()