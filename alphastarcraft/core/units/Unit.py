import numpy as np 

class Unit:
    '''
    Definition of all information about the unit

    + Construction Site Number
    + Requires
    + Cost: [Crystal, Gas, Supply]
    + Life
    + Abilities: [Attacks, Defenses] (Attacks: [Ground, Air])
    + Build Time
    + Equipments: [Attacks, Defenses]
    + Sight
    + Velocity, Maxvelocity, Acceleration
    + IsAirAttack, IsFly
    + Info
    '''
    def __init__(self,position,velocity,maxvelocity,life,
                cost,size,ability,
                is_attackair,
                is_fly):
        self.position = position
        self.velocity = velocity
        self.maxvelocity = maxvelocity

        self.life = life
        self.cost = cost # [Crystal, Gas, Food]

        self.size = size    # [Width, Hight]
        self.ability = ability # [Attack, Defend]

    def setPosition(self,position):
        self.position = position

    def getPosition(self):
        return self.position

    def setLife(self,life):
        self.life = life

    def getLife(self):
        return self.life

    def setVelocity(self,velocity):
        self.velocity = velocity

    def getVelocity(self):
        return self.velocity

    def getCost(self):
        return self.cost 

    def IsAttackAir(self):
        return self.is_attackair

    def IsFly(self):
        return self.is_fly