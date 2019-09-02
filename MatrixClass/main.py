from MatrixClass import Matrix
from NeuralNetwork import NeuralNetwork
from operator import itemgetter
import copy
import statistics

def getMean(numbers):
    sum = 0
    for el in numbers:
        sum += el
    sum /= len(numbers)
    return sum

networks = [NeuralNetwork(3, [2, 3, 1]) for _ in range(10)]

while(True):
    output = []
    for network in networks:
        output.append(network.feedForward([0, 1]))

    fit = [max(min(1-abs(1-x[0]), 1), 0) for x in output]
    print(statistics.mean(fit))

    maxi = max(fit)
    ind = []
    for i in range(5):
        mini =  min(fit)
        ind.append(fit.index(mini))
        fit[ind[-1]] = maxi
        
    ind.sort()
    for i in range(5):
        del networks[ind[-i-1]]

    for i in range(5):
        networks.append(copy.deepcopy(networks[i]))
        networks[-1].adjust()

    choice = input("Press a button")
    if choice == 'o':
        print(output)
