from MatrixClass import Matrix

from typing import List
import random
import math
import copy



class NeuralNetwork:
    def __init__(self, matrices):
        self.network = matrices

    @classmethod
    def newNeuralNetwork(cls, layers : int, amountPerLayer : List[int]) -> 'NeuralNetwrok':
        network = []
        for i in range(layers-1):
            network.append(Matrix.newMatrix(amountPerLayer[i]+1, amountPerLayer[i+1], []))
        return cls(network)

    @classmethod
    def fromFile(cls, inputString : str) -> 'NeuralNetwork':
        listForMatrices = inputString.split("Next Matrix:")
        network = []
        for element in listForMatrices:
            network.append(Matrix.fromFile(element))
        return cls(network)

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
                    #Change to use gaussion variation instead
                    adjustList.append(random.uniform(-maxAdjust, maxAdjust))
                else: 
                    adjustList.append(0)
            mat.adjust(adjustList)

    def activationFunction(self, inp):
         return 1/(1+math.exp(-inp))

    def saveFunction(self):
        saveString = ""
        first = True
        for matrix in self.network:
            if first:
                first = False
            else:
                saveString +=  "\nNext Matrix:\n"
            saveString += matrix.saveFunction()
        return saveString