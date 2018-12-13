# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:03:03 2018

@author: gy18kah
"""
import random
import operator
import matplotlib.pyplot as plt
import agentframework3
import csv 
import matplotlib.animation

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
neighbourhood = 20
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework3.agent(environment,agents))
    
for a in agents:
    print(a.getx(), a.gety())

#test
for a in agents:
    print(a.getx(), a.gety())
print ("----------",agents[0].getx())
print ("----------",agents[0].gety())

# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        #randomise the order in which agents are processed each iteration

        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbourhood(neighbourhood)

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
a = agentframework3.agent(environment,agents)
print (a.y, a.x)
a.move()
print (a.y, a.x)


fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])
agents = []
for i in range(num_of_agents):
    agents.append(agentframework3.agent(environment,agents))

carry_on = True

def update (frame_number):
    fig.clear()   

    for i in range(num_of_agents):
        agents[i].move()
#            if random.random() < 0.5:
#                agents[i][0]  = (agents[i][0] + 1) % 99 
#            else:
#                agents[i][0]  = (agents[i][0] - 1) % 99
#            
#            if random.random() < 0.5:
#                agents[i][1]  = (agents[i][1] + 1) % 99 
#            else:
#                agents[i][1]  = (agents[i][1] - 1) % 99
        
    if random.random()< 0.1:
        carry_on = False
        print("stopping condition")
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].x,agents[i].y)

def gen_function(b = [0]):
    a = 0
    global carry_on #not needed as were not assigning, but clearer
    while (a<10) & (carry_on) :
        yield a            #returns control and waits next call
        a = a+1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#moving it but not so its continuous 
matplotlib.pyplot.show()           
#produces animation 

