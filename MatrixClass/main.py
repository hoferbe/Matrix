from MatrixClass import Matrix
from NeuralNetwork import NeuralNetwork
from operator import itemgetter
from GenAlg import GenAlgo
import copy
import statistics
import random
import keyboard
import sys

##TODO: Write a Startup Menu to choose to load networks, load a network or train new ones.
## Maybe as well to choose between training or just showing
## And add possibility to choose the values for the networks.

running = True

choice =  input("Do you want to load a specific file?[y][n] ")
networks = GenAlgo
if choice == "y":
    worked = False
    while not worked:
        name = input("What is the file name?(with  .txt) ")
        reader = open(name, "r")
        if reader.mode == "r":
            worked = True
        else:
            print("Opening file didn't work")
    content  = reader.read()
    networks = GenAlgo.fromFile(content)
else:
    networks = GenAlgo.newGenAlgo(100, 3, [2, 4, 1])

possible = [[0, 0],[0, 1],[1, 0], [1, 1]]
solutions = [[0], [1], [1], [0]]


while(running):
    choice = random.randint(0, 3)
    output = networks.feedFoward(possible[choice])


    if choice == 1 or choice == 2:
        fit = [max(min(x[0], 1), 0) for x in output]
        s = sum(1 for x in output if x[0] >= 0.5)
    else:
        fit = [1-min(max(x[0], 0), 1) for x in output]
        s = sum(1 for x in output if x[0] < 0.5)
    
    print("Average fitness: " + str(statistics.mean(fit)))
    print("Part that succeeded: " + str(s/len(output)))
    print("Target output: " + str(solutions[choice]))
        
    networks.nextGen(fit)


    if keyboard.is_pressed('o'):
        sys.stdout.flush()
        print(output)
        input("Press enter")
    elif keyboard.is_pressed('p'):
        sys.stdout.flush()
        input("Press enter")
    elif keyboard.is_pressed('s'):
        sys.stdout.flush()
        networks.saveFunction()
        input("Finished")