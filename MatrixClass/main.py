from MatrixClass import Matrix
from NeuralNetwork import NeuralNetwork
from operator import itemgetter
from GenAlg import GenAlgo
import copy
import statistics



networks = GenAlgo(10, 3, [2, 3, 1])

while(True):

    output = networks.feedFoward([0, 1])

    fit = [max(min(1-abs(1-x[0]), 1), 0) for x in output]
    print(statistics.mean(fit))

    maxi = max(fit)
    fit2 = copy.deepcopy(fit)
    ind = []
    for i in range(5):
        mini =  min(fit)
        ind.append(fit.index(mini))
        fit[ind[-1]] = maxi
        
    networks.nextGen(fit2)

    choice = input("Press a button")
    if choice == 'o':
       print(output)
