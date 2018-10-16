# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random 
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
