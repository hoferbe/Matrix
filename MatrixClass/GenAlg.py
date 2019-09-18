from NeuralNetwork import NeuralNetwork
from typing import List
import random
import copy
import json

class GenAlgo:
    def __init__(self, neuralNetworks):
        self.Neurals = neuralNetworks
        self.output = []
        self.maxAdjust = 1  #Maybe adjust to gauss variation instead
        self.genCounter = 1
        self.correctionCounter = 1
        self.mutationsRate = 0.5

    @classmethod
    def newGenAlgo(cls, amountOfNetworks, amountOfLayers, layerVec : List[int]) -> 'GenAlgo':
        Neurals = [NeuralNetwork.newNeuralNetwork(amountOfLayers, layerVec) for _ in range(amountOfNetworks)]
        return cls(Neurals)

    @classmethod
    def fromFile(cls, inputString : str) -> 'GenAlgo':
        listForNetworks = inputString.split("Next Network:")
        Neurals = []
        for element in listForNetworks:
            Neurals.append(NeuralNetwork.fromFile(element))
        return cls(Neurals)
    
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


        length = len(self.Neurals)/2
        tempNeurals = random.choices(self.Neurals, fit, k=int(len(self.Neurals)/2))
        self.Neurals = tempNeurals


        tempVec = []
        for net in self.Neurals:
            tempVec.append(copy.deepcopy(net))
            tempVec[-1].adjust(self.maxAdjust, self.mutationsRate)
        self.Neurals += tempVec

    def saveFunction(self):
        #have to add somehow the current adjustMax, Mutationchance, change in mutationchance and so on to be able to keep training at a later point in time
        saveString = ""
        first = True
        for network in self.Neurals:
            if first:
                first  = False
            else:
                saveString += "\nNext Network:\n\n"
            saveString += network.saveFunction()
        filename = input("Choose file name: ")
        writer = open(filename + ".txt", "w+")
        writer.write(saveString);
        writer.close();