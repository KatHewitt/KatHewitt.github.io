# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:11:11 2018

@author: gy18kah
"""

import random

class agent():
        
    def __init__ (self,environment,agents): 
       self._x = random.randint(0,99) 
       self._y = random.randint(0,99)
       self.environment = environment
       self.store = 0
       self.agents = agents 
       
    def getx(self):
        return self._x
    def setx(self, value):
         self._x = value
    def delx(self):
         del self._x
    x = property(getx,setx, delx, "x-coordinate of agent")

    def gety(self):
         return self._y
    def sety(self, value):
         self._y = value
    def dely(self):
         del self._y
    y = property (gety, sety, dely, "y-coordinate of agents")
#
#    
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y= (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100           
#           
#            
    def eat(self): 
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
#    
#    def printy(self):
#        print(self.agents)
#        # pritn another agents y or x to prove it 
#        
#
    def share_with_neighbourhood(self,neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum / 2
                self.store = ave 
                agent.store = ave 
               # print("sharing"+str(dist) + ""+ str(ave))
                
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5

##agent.getstore() and agent.setstore(ave)

#move quicker if they have more resources 
#move def - define 1 as soemthign and when this is above 50 they move 2 

#add wolves to eat nearby sheep 
#change number of agents - loops lecture (removing things from lists)


#import sys
#sys.stdout.flush() = forces buffer to fluch to print out 