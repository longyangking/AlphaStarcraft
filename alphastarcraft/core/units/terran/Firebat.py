from ..Unit import Unit
import numpy as np 

class Firebat(Unit):
    def __init__(self,position,velocity,maxvelocity,
                life=50,
                cost=[50,255,1],
                size=[1,1],
                ability=[16,1],
                is_attackair=False,
                is_fly=False)
        Unit.__init__(self,position,velocity,maxvelocity,
                    life,cost,size,ability,is_attackair,is_fly)

        

