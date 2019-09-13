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
        sumOfVec = 0
        for el in fit:
            sumOfVec += el

        saveFit = copy.deepcopy(fit)
        #for ind in range(len(fit)-1):
            #fit[ind] /= sumOfVec
        
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
        ind2.sort()
        sumSurvive = 0
        sumDead = 0

        for index in range(len(saveFit)):
            if index in ind:
                sumSurvive += saveFit[index]
            elif index in ind2:
                sumDead += saveFit[index]
            else: print("WTF?")

        print("Max fitness: " + str(max(saveFit)))
        print("Min fitness: " + str(min(saveFit)))
        print("Average survived fitness: " + str(sumSurvive/len(ind)) + " with a langth of " + str(len(ind)))
        print("Average dead fitness: " + str(sumDead/len(ind2)) + " with a langth of " + str(len(ind2)))

        for i in range(len(ind2)):
           self.Neurals.pop(ind2[-i - 1])

        tempVec = []
        for net in self.Neurals:
            tempVec.append(copy.deepcopy(net))
            tempVec[-1].adjust()
        self.Neurals += tempVec