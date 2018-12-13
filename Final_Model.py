# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:03:03 2018

ABM: Creates agents with starting locations from scraped web page. Agents move randonly eating the environment
and sharing with neighbours.
Development = agents move quicker if they have eaten more of the environmnet. 
@author: gy18kah
"""

#agents created with starting locations scraped from web page (data scraping) 

import random
import operator
import matplotlib.pyplot as plt
import agentframework3
import csv 
import matplotlib.animation
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import requests
import bs4


environment = []
with open('in.txt') as f:
    reader = csv.reader(f)

    for row in reader:
        rowlist = []
        for value in row:
            #print (value)
            rowlist.append(int(value))
        environment.append(rowlist)

matplotlib.use('TkAgg')
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()


#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.x - agents_row_b.x)**2) + 
#    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


#scrape a web page to get the agent starting locations 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)


# Make the agents.
for i in range(num_of_agents):
    #instead of random starting positions, use locations from scraped web page
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework3.agent(environment,agents, y, x))
    

fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])

#agents = []
#for i in range(num_of_agents):
#    agents.append(agentframework3.agent(environment,agents))

carry_on = True

def update (frame_number):
    global carry_on
    fig.clear() 
    
    #Make axes
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment)

    for i in range(num_of_agents):
        agents[i].move_faster() #development from just 'move' agents 'moves faster' with more food
        agents[i].eat()
        agents[i].share_with_neighbourhood(neighbourhood) #share with other agents that are within units
#            if random.random() < 0.5:
#                agents[i][0]  = (agents[i][0] + 1) % 99 
#            else:
#                agents[i][0]  = (agents[i][0] - 1) % 99
#            
#            if random.random() < 0.5:
#                agents[i][1]  = (agents[i][1] + 1) % 99 
#            else:
#                agents[i][1]  = (agents[i][1] - 1) % 99
        
    if random.random()< 0.01:
        carry_on = False
        print("stopping condition")
        
    for i in range(num_of_agents):
        #plot
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].x,agents[i].y)


def gen_function(b = [0]):
    a = 0
    global carry_on #not needed as were not assigning
    while (a<1000) & (carry_on) :
        yield a            #returns control and waits next call
        a = a+1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
##animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#moving it but not so its continuous 
##matplotlib.pyplot.show()           
#produces animation 

def run():
    global animation
    #called by the GUI menu item run
    animation = matplotlib.animation.FuncAnimation (fig, update, frames=gen_function, repeat=False)
    canvas.show()

#set up GUI usign tkinter, creates window and a menu
root = tkinter.Tk() #main window
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 


tkinter.mainloop()

model_menu.entryconfig("Run model", state="disabled") 
# Until the user has chosen files, then:
#model_menu.entryconfig("Run model", state="normal") 


    














