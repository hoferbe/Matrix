from NeuralNetwork import NeuralNetwork
from typing import List
import random
import copy

class GenAlgo:

    def __init__(self, amountOfNetworks, amountOfLayers, layerVec : List[int]):
        self.Neurals = [NeuralNetwork(amountOfLayers, layerVec) for _ in range(amountOfNetworks)]
        self.output = []
        self.maxAdjust = 1
        self.genCounter = 1
        self.correctionCounter = 1
        self.mutationsRate = 0.5
    ##TODO: Writer funciton to save a NN or to save the whole Set and load accordingly
    
    def feedFoward(self, input : List[float]):
        output = []
        for net in self.Neurals:
            output.append(net.feedForward(input))
        return output

    def nextGen(self, fit : List[float]):
        self.genCounter += 1
        if self.genCounter % 100**self.correctionCounter == 0:
            self.correctionCounter += 1
            self.mutationsRate -= 0.1
            self.mutationsRate = max([0.1, self.mutationsRate])
            #self.maxAdjust /= 10
            #ToDo: Potentially do adjust of mutationrate instead.

        for i in range(len(fit)):
            self.Neurals[i].saveFit(fit[i])

        sumOfVec = sum(fit)

        length = len(self.Neurals)/2
        tempNeurals = random.choices(self.Neurals, fit, k=int(len(self.Neurals)/2))
        self.Neurals = tempNeurals

        #ind = []
        #ind.sort()
        #while len(ind) < len(self.Neurals)/2:
        #    randchoice = random.randint(0, len(fit)-1)
        #    if not randchoice in ind and random.uniform(0, 1) < fit[randchoice]:
        #        ind.append(randchoice)

        #ind2 = []
        #for  i in range(len(self.Neurals)):
        #    if not i in ind:
        #        ind2.append(i)

        #for i in range(len(ind2)):
        #   self.Neurals.pop(ind2[-i - 1])

        tempVec = []
        for net in self.Neurals:
            tempVec.append(copy.deepcopy(net))
            tempVec[-1].adjust(self.maxAdjust, self.mutationsRate)
        self.Neurals += tempVec