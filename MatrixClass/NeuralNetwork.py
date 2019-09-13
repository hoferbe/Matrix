from MatrixClass import Matrix

from typing import List
import random



class NeuralNetwork:
    def __init__(self, layers : int, amountPerLayer : List[int]):
        self.network = []
        self.adjustvalue = 0.1
        self.counter = 0
        for i in range(layers-1):
            self.network.append(Matrix(amountPerLayer[i], amountPerLayer[i+1], []))

    def feedForward(self, input : List[float]):
        for mat in self.network:
            input = mat * input
        return input

    def adjust(self):
        self.counter += 1
        for mat in self.network:
            adjustList = []
            for i in range(mat.width * mat.height):
                adjustList.append(random.uniform(-self.adjustvalue, self.adjustvalue))
            mat.adjust(adjustList)
        if self.counter > 10:
            self.adjustvalue *= 0.9
            self.counter = 0
