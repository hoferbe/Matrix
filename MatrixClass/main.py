from MatrixClass import Matrix
from NeuralNetwork import NeuralNetwork
from operator import itemgetter
from GenAlg import GenAlgo
import copy
import statistics



networks = GenAlgo(100, 3, [2, 3, 1])

while(True):

    output = networks.feedFoward([0, 1])

    fit = [max(min(x[0], 1), 0) for x in output]
    print(statistics.mean(fit))
        
    networks.nextGen(fit)

    choice = input("Press a button")
    if choice == 'o':
       print(output)
