from MatrixClass import Matrix
from NeuralNetwork import NeuralNetwork
from operator import itemgetter
from GenAlg import GenAlgo
import copy
import statistics
import random



networks = GenAlgo(100, 3, [2, 4, 1])
possible = [[0, 0],[0, 1],[1, 0], [1, 1]]
solutions = [[0], [1], [1], [0]]

while(True):
    choice = random.randint(0, 3)
    output = networks.feedFoward(possible[choice])

    if choice == 1 or choice == 2:
        fit = [max(min(x[0], 1), 0) for x in output]
    else:
        fit = [1-min(max(x[0], 0), 1) for x in output]
    
    print("Average fitness: " + str(statistics.mean(fit)))
    print("Target output: " + str(solutions[choice]))
        
    networks.nextGen(fit)

    choice = input("Press a button")
    if choice == 'o':
       print(output)
