import numpy as np 

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def add(self,vector):
        if vector is None:
            return self

        x = self.x + vector.getX()
        y = self.y + vector.getY()
        z = self.z + vector.getZ()
        return Vector(x,y,z)
    
    def multiply(self,alpha):
        x = alpha*self.x 
        y = alpha*self.y 
        z = alpha*self.z 
        return Vector(x,y,z)

    def getX(self):
        return self.x 

    def getY(self):
        return self.y 

    def getZ(self):
        return self.z 
