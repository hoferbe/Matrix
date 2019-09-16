from MatrixClass import Matrix
from NeuralNetwork import NeuralNetwork
from operator import itemgetter
from GenAlg import GenAlgo
import copy
import statistics
import random
import keyboard



networks = GenAlgo(100, 3, [2, 4, 1])
possible = [[0, 0],[0, 1],[1, 0], [1, 1]]
solutions = [[0], [1], [1], [0]]

while(True):
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
       print(output)
       input("Press enter")
    elif keyboard.is_pressed('p'):
        input("Press enter")