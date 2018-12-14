# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:11:11 2018
Kathryn Hewitt 

Agent Framework 
define inside it an Agent class, with an __init__ method
define move

"""

import random

class agent():

    def __init__ (self): 
       self.x = random.randint(0,99) 
       self.y = random.randint(0,99)
       
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y= (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
           
