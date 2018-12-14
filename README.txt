READ ME 

This read me text file contains information explaining what the code is and instructions on how to run it.

AGENT BASED MODELLING (ABM)

The code written in python builds an ABM which successfully represents individuals and captures both their interactions with each other and their environment 

The model builds up a series of agents in space which are able to communicate with each other and are able to query and change the environment based on the knowledge they have about the environment they are in.
The model simulates the random movement of agents around the environment from a given start location attained by scraping a web page. The agents then move around eating the environment, but first checking other agents are not already in the neighbourhood. 
Eating the environment involves checking the environment to see what’s in its location and changing it, along with other agents on a neighbourhood basis.Each agent will have a list of other agents so they can communicate 

The final model also has the added development of including a ‘move faster’ ability for the agents. This gives those agents who have consumed more food the opportunity to move faster within the environment, simulating the idea that more food equals more energy and faster movement.

The models runs by allowing agents to do their thing for each time step repeatedly until the number of steps has run or some stopping condition is reached. 

The code ultimately produces a new window in which the model is run and visualised. 

Where appropriate tests have been incorporated into the model to ensure the models validity and to prevent fatal issues.


INSTALLATION AND MODEL INSTRUCTIONS 

The following files are needed to run the model; 
-	Final Model 
-	Final Agent Framework 
They can be both downloaded via links on the following website https://kathewitt.github.io/#work

Python version 3 is needed to run the model, the best way to run Python scripts is using an install called Anaconda 

On opening the two files in python the model can be run
On completion a new blank window should appear in which in the top left corner there is a button to click run model. 
This will produce the final output a visual animation of agents moving around and eating the environment.
The number of agents is stated in the code (and is adaptable to change) and the agents will continue to move until a stopping condition has been reached. 


ROADMAP

Ideas for development of the code, in development of the code I would be introducing more potential interactions for the agents to have both with each other and with the environment;

1. Adding in a new type of agent, this would added factor would enable the number of agents to change.
2. The ability for agents to steal more from resources from others if they themselves are low  

AUTHORS

Kathryn Hewitt – https://github.com/KatHewitt

LICENCE 

See LICENSE.txt file for details

ACKNOWLEDGMENTS 

This project has been run with the module Programming for Geographical Information Analysis Core Skills
