# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot
import operator
import random 
agents = []
agents.append([random.randint(0,99), random.randint(0,99)])
agents.append([random.randint(0,99), random.randint(0,99)])
agents.append([random.randint(0,99), random.randint(0,99)])
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

print(answer)

print(max(agents))
print (max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='red')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='blue')
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