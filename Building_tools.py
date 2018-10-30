# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot
import operator
import random 

def distance_between(agents_row_a, agents_row_b):
    answer = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    return answer
# define it

agents = []
num_of_moves = 100
num_of_agents = 10

# Loop through adding agents
# Make agents
for i in range(num_of_agents):
    agents.append([random.randint(0,100), random.randint(0,100)])
print(agents)

#randomly changing the coordinates loop
# Move agents
for i in range(num_of_agents):
    for k in range(num_of_moves):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
#torus stops it going off the graph think of clock anaology   

print(agents)

            
#agents.append([random.randint(0,99),random.randint(0,99)])
#agents.append([random.randint(0,99),random.randint(0,99)])
#agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)
print(agents[0])
print(agents[0][0])
print(agents[0][1])
print(agents[1])
print(agents[1][0])
print(agents[1][1])
#print(agents[2])
#print(agents[2][0])
#print(agents[2][1])


answer = (((agents[0][0] - agents[1][0]) ** 2) + ((agents[0][1] - agents[1][1]) ** 2)) ** 0.5
#finding the difference
print(answer)

minx = min(agents, key=operator.itemgetter(0))
print(minx)
maxx = max(agents, key=operator.itemgetter(0))
print(maxx)

miny = min(agents, key=operator.itemgetter(1))
print(miny)
maxy = max(agents, key=operator.itemgetter(1))
print(maxy)
#finding the minimum and maximum 
#print(max(agents))

"""
matplotlib.pyplot.ylim(-1, 100)
matplotlib.pyplot.xlim(-1, 100)
#plotting
#matplotlib.pyplot.ylim(miny[1], maxy[1])
#matplotlib.pyplot.xlim(minx[0], maxx[0])
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0], color='red')
#loop for plotting
matplotlib.pyplot.scatter(minx[1],minx[0], color='blue')
matplotlib.pyplot.scatter(maxx[1],maxx[0], color='pink')
matplotlib.pyplot.scatter(miny[1],miny[0], color='green')
matplotlib.pyplot.scatter(maxy[1],maxy[0], color='orange')
#plotting the highest, lowest, right and left
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='blue')
#make sure plots are within range
matplotlib.pyplot.show()

"""

# call it 
distance = distance_between(agents[0], agents[1])
print(distance)

# loop testing each agent against each other, abcd - aa ab ac ad - bb ba bc bd..
distlist =[]
for j in range(num_of_agents):
    for l in range(j+1, num_of_agents):
        distance = distance_between(agents[j], agents [l])
        distlist.append(distance)
        #print (j,l,distance)
print(distlist)   
# j+1 is are current position plus 1 to get rid of duplicates and stop running itself
# range is whole thing, just add another parameter to change that 
#distlist is name oflist square brackets equal mean empty list

max(distlist)
min(distlist)
#min and max just find min and max 

#try a variety of different order of magnitude of agent numbers, record the times and plot them as a scattergraph
# make list of all the times take to run code for bigger numbers and plot as a scatter graph


import time 
start = time.clock()
#finding time  
end = time.clock()
print ("time = " + str(end - start))

min_agents = min(distance)
print (min_agents)
        
'''

y0 = 50 
x0 = 50 
if random.random() < 0.5:
    y0 += 1
    x0 += 1
else:
    y0 -= 1
    x0 -= 1
import random 
y1 = 50
x1 = 50
if random.random() < 0.5:
    y1 += 1
    x1 += 1
else: 
    y1 -= 1
    x1 -= 1
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum **0.5
print(answer)
answer2 = (((y0 - y1) ** 2) + ((x0 - x1) ** 2)) **  0.5
print (answer2)


# randomise starting points is 100x100 grid 
# integer values between 0 and 99 

import random 
y0 = 50
x0 = 50
if random.randint(0,99) < 50:
    y0 += 1
    x0 += 1
else: 
    y0 -= 1
    x0 -= 1
import random
y1 = 50
x1 = 50
if random.randint(0,99) < 50:
    y1 += 1
    x1 += 1
else:
    y1 -= 1
    x1 -= 1
answer = (((y0 - y1) ** 2) + ((x0 - x1) ** 2)) ** 0.5
print (answer)
'''