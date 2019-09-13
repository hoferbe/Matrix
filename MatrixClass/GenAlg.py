from NeuralNetwork import NeuralNetwork
from typing import List
import random
import copy

class GenAlgo:

    def __init__(self, amountOfNetworks, amountOfLayers, layerVec : List[int]):
        self.Neurals = [NeuralNetwork(amountOfLayers, layerVec) for _ in range(amountOfNetworks)]
        self.output = []
    
    def feedFoward(self, input : List[float]):
        output = []
        for net in self.Neurals:
            output.append(net.feedForward(input))
        return output

    def nextGen(self, fit : List[float]):
        sumOfVec = sum(fit)

        ind = []
        ind.sort()
        while len(ind) < len(self.Neurals)/2:
            randchoice = random.randint(0, len(fit)-1)
            if not randchoice in ind and random.uniform(0, 1) < fit[randchoice]:
                ind.append(randchoice)

        ind2 = []
        for  i in range(len(self.Neurals)):
            if not i in ind:
                ind2.append(i)

        for i in range(len(ind2)):
           self.Neurals.pop(ind2[-i - 1])

        tempVec = []
        for net in self.Neurals:
            tempVec.append(copy.deepcopy(net))
            tempVec[-1].adjust()
        self.Neurals += tempVec