from MatrixClass import Matrix

from typing import List
import random
import math
import copy



class NeuralNetwork:
    def __init__(self, layers : int, amountPerLayer : List[int]):
        self.network = []
        self.fitness = 0
        for i in range(layers-1):
            self.network.append(Matrix(amountPerLayer[i]+1, amountPerLayer[i+1], []))

    def saveFit(self, fitn):
        self.fitness = fitn

    ##TODO: writer function to save and load a NeuralNetwork

    def feedForward(self, input : List[float]):
        current = copy.deepcopy(input)
        for mat in self.network:
            current.append(1.0)
            current = mat * current
            current = [self.activationFunction(listEl) for listEl in current]
        return current

    def adjust(self, maxAdjust, mutationRate):
        for mat in self.network:
            adjustList = []
            for i in range(mat.width * mat.height):
                if random.random() <= mutationRate:
                    adjustList.append(random.uniform(-maxAdjust, maxAdjust))
                else: 
                    adjustList.append(0)
            mat.adjust(adjustList)

    def activationFunction(self, inp):
         return 1/(1+math.exp(-inp))