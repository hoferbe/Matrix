from MatrixClass import Matrix

from typing import List
import random
import math



class NeuralNetwork:
    def __init__(self, layers : int, amountPerLayer : List[int]):
        self.network = []
        for i in range(layers-1):
            self.network.append(Matrix(amountPerLayer[i]+1, amountPerLayer[i+1], []))

    def feedForward(self, input : List[float]):
        for mat in self.network:
            input.append(1.0)
            input = mat * input
            input = list(map(self.activationFunction, input))
        return input

    def adjust(self):
        for mat in self.network:
            adjustList = []
            for i in range(mat.width * mat.height):
                adjustList.append(random.uniform(-1, 1))
            mat.adjust(adjustList)

    def activationFunction(self, inp):
         return 1/(1+math.exp(-inp))