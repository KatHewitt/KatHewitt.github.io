# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:11:11 2018

@author: gy18kah
"""

import random

class agent():
    

    def __init__ (self,environment): 
       self.x = random.randint(0,99) 
       self.y = random.randint(0,99)
       self.environment = environment
       self.store = 0
       
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y= (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100           
           
   
       
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        