# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:11:11 2018
Agent Framework for final model
@author: gy18kah
"""

import random

class agent():
   #A class for an agent that can moe in space and interact with other agents ands its environment     

    def __init__ (self,environment,agents, y = None, x = None):
        if (x == None):
            self._x = random.randint(0,299)
        else:
            self._x = x
            
        if (y == None):
            self._y = random.randint(0,299)
        else:
            self._y = y
        
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

#FIRST ADDITION: moveING agents randomly                
#    def move(self):
#        if random.random() < 0.5:
#            if random.random() < 0.5:
#                self._y = (self._y + 1) % 100
#            else:
#                self._y= (self._y - 1) % 100        
#        if random.random() < 0.5:
#            if random.random() < 0.5:
#                self._x = (self._x + 1) % 100
#            else:
#                self._x = (self._x - 1) % 100

#DEVELOPMENT FROM 'Move': Move faster enables agents to move faster if they have eaten more food 
#Shrunked addition of move faster 
    def mover(self, xory, distance, probabilityStayStill):
        if random.random() < probabilityStayStill:
            if random.random() < 0.5:
                xory = (xory + distance) % 300
            else:
                xory = (xory - distance) % 300
        return xory
    
    def move(self):
        self.sety(self.mover(self._y, 1, 0.5))
        self.setx(self.mover(self._x, 1, 0.5))        
 
    def move_faster(self):
        if self.store > 50:
            self.sety(self.mover(self._y, 2, 0.5))
            self.setx(self.mover(self._x, 2, 0.5))
        else:
            self.sety(self.mover(self._y, 1, 0.5))
            self.setx(self.mover(self._x, 1, 0.5))
 
#DEVELOPMENT FROM 'Move': Move faster enables agents to move faster if they have eaten more food 
#First unshrunken addition of move faster 
#    def move_faster(self):
#        if self.store > 50:
#            if random.random() < 0.5:
#                self._y = (self._y + 2) % 100
#            else:
#                self._y= (self._y - 2) % 100
#        else:
#            if random.random() < 0.5:
#                self._y = (self._y + 1) % 100
#            else:
#                self._y= (self._y - 1) % 100
#
#        if self.store > 50:
#             if random.random() < 0.5:
#                 self._x = (self._x + 2) % 100
#             else:
#                 self._x = (self._x - 2) % 100 
#        else:
#             if random.random() < 0.5:
#                 self._x = (self._x + 1) % 100
#             else:
#                 self._x = (self._x - 1) % 100 
            
                     
#Eating the environment           
    def eat(self): 
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
    
#    def printy(self):
#        print(self.agents)
#        # pritn another agents y or x to prove it 
#        
#
    def share_with_neighbourhood(self,neighbourhood):
        for agent in self.agents:
           if agent != self: #dont want to share with itself
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                   sum = self.store + agent.store
                   ave = sum / 2
                   self.store = ave 
                   agent.store = ave 
                   #print("sharing"+str(dist) + ""+ str(ave))
                
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5

#agent.getstore() and agent.setstore(ave)

#import sys
#sys.stdout.flush() = forces buffer to fluch to print out 
