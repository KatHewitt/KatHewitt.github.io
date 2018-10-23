# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot
import operator
import random 

agents = []
num_of_moves = 100
num_of_agents = 10

# Loop through adding agents
for i in range(num_of_agents):
    agents.append([random.randint(0,100), random.randint(0,100)])
print(agents)

#randomly changing the coordinates loop
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