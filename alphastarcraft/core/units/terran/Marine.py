from ..Unit import Unit
import numpy as np 

class Marine(Unit):
    def __init__(self,position,velocity,maxvelocity,
                life=40,
                cost=[50,0,1],
                size=[1,1],
                ability=[6,0],
                is_attackair=False,
                is_fly=False)
        Unit.__init__(self,position,velocity,maxvelocity,
                    life,cost,size,ability,is_attackair,is_fly)

        

