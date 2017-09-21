import numpy as np 

class Particle:
    def __init__(self,position,velocity,color,life):
        self.position = position
        self.velocity = velocity
        self.color = color
        if (life > 0):
            self.life = life

    def update(self,elapsedTime,ratio=0.2):
        self.velocity = (1+0.2)*self.velocity
        self.position += self.velocity
        self.life += 1

    def getlife(self):
        return self.life

    def setlife(self,life):
        self.life = life

    def getPosition(self):
        return self.position

    def setPosition(self,position):
        self.position = position

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

    def getVelocity(self):
        return velocity

    def setVelocity(self,velocity):
        self.velocity = velocity