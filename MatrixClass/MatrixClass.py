import itertools
import copy
import random
from typing import List


def dotProduct(a : List[float], b : List[float]):
    if len(a) != len(b): return
    k = 0
    for (i, j) in zip(a, b):
        k += i*j
    return k

def transpose(matrixList):
    height = len(matrixList)
    width = len(matrixList[0])
    temp = [[0 for x in range(height)] for y in range(width)]
    for i in range(height):
        for j in range(width):
            temp[j][i] = matrixList[i][j]
    return temp


class Matrix:

    def __init__(self, widthI, heightI, numbers: List[float]):
        self.matrixList = [[]]
        self.width = widthI
        self.height = heightI
        if numbers == []:
            for i in range(self.height):
                temp = []
                for j in range(self.width):
                    temp.append(random.random())
                self.matrixList.append(temp)
        else:
            for i in range(self.height):
                self.matrixList.append(numbers[i*self.width : (i+1)*self.width])
        self.matrixList.pop(0)

    def transpose(self):
        temp = [[0 for x in range(self.height)] for y in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                temp[j][i] = self.matrixList[i][j]
        x = self.width
        self.width = self.height
        self.height = x
        self.matrixList = temp

    def adjust(self, correction : List[float]):
        for i in range(self.height):
            for j in range(self.width):
                self.matrixList[i][j] += correction[i*self.width + j]

    def __add__(self, other: 'Matrix'):
        temp = Matrix(self.width,  self.height, [])
        if self.width == other.width and self.height == other.height :
            for i in range(self.height):
                for j in range(self.width):
                    temp.matrixList[i][j] = self.matrixList[i][j] + other.matrixList[i][j]
        return temp

    def __mul__(self, other):
        tempM = copy.deepcopy(other)
        tempM.transpose()
        newWidth = other.width
        newHeight = self.height
        tempVector = []
        if self.width == tempM.width:
            for i in range(newHeight):
                for j in range(newWidth):
                    tempVector.append(dotProduct(self.matrixList[i], tempM.matrixList[j]))

        ret = Matrix(newWidth, newHeight, tempVector)
        return ret

    def __mul__(self, vec):
        tempVec = []
        for vecM in self.matrixList:
            tempVec.append(dotProduct(vecM, vec))
        return tempVec


    def printMatrix(self):
        for line in self.matrixList:
            print(line)
        print('\n')