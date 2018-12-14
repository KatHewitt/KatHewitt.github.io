# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:03:03 2018
Import data to use as out agents environment and get them to interact with it 
@author: gy18kah
"""
import random
import operator
import matplotlib.pyplot
import agentframework
import csv 
environment = []
with open('in.txt') as f:
    reader = csv.reader(f)

    for row in reader:
        rowlist = []
        for value in row:
            #print (value)
            rowlist.append(int(value))
        environment.append(rowlist)


matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()



def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.agent(environment))

# Move and eat
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()
        agents[i].eat()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
a = agentframework.agent(environment)
print (a.y, a.x)
a.move()
print (a.y, a.x)

        
