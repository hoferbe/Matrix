from MatrixClass import Matrix

from typing import List
import random



class NeuralNetwork:
    def __init__(self, layers : int, amountPerLayer : List[int]):
        self.network = []
        for i in range(layers-1):
            self.network.append(Matrix(amountPerLayer[i], amountPerLayer[i+1], []))

    def feedForward(self, input : List[float]):
        for mat in self.network:
            input = mat * input
        return input

    def adjust(self):
        for mat in self.network:
            adjustList = []
            for i in range(mat.width * mat.height):
                adjustList.append(random.uniform(-0.1, 0.1))
            mat.adjust(adjustList)