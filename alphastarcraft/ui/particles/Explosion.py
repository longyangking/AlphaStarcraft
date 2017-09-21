import numpy as np

class Explosion:
    def __init__(self,x,y,numofparticles=2,maxlife=15,maxvelocity=1.0):
        self.position = (x,y)
        self.particles = list()
        self.numofparticles = numofparticles
        self.maxlife = maxlife
        self.maxvelocity = maxvelocity

        self.endstate = False

        self.__generateParticles()

    def __generateParticles(self):
        ratio = np.random.random(self.numofparticles)
        velocities = self.maxvelocity*ratio

        ratio = np.random.random((self.numofparticles,3))
        ratio[:,2] = 0
        ratio[:,1] = 1- ratio[:,0]
        ratio = np.sqrt(ratio)
        for i in range(self.numofparticles):
            position = self.position
            velocity = velocities[i]*ratio[i,:]
            color = 1
            life = 0
            self.particles.append(Particle.Particle(position,velocity,color,life))

    def update(self,elapsedTime):
        if self.endstate:
            return False

        isAlldead = True
        for i in range(len(self.particles)):
            particle = self.particles[i]
            if (particle.getLife()<self.maxlife):
                particle.update(elapsedTime)
                isAlldead = False

        if isAlldead:
            self.endstate = True

        return True