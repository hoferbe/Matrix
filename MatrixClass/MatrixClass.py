import itertools
import copy
from typing import List


def dotProduct(a : List[float], b : List[float]):
    if len(a) != len(b): return
    k = 0
    for (i, j) in zip(a, b):
        k += i*j
    return k

def invert(matrixList):
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
                    temp.append(0)
                self.matrixList.append(temp)
        else:
            for i in range(self.height):
                self.matrixList.append(numbers[i*self.width : (i+1)*self.width])
        self.matrixList.pop(0)

    def invert(self):
        temp = [[0 for x in range(self.height)] for y in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                temp[j][i] = self.matrixList[i][j]
        x = self.width
        self.width = self.height
        self.height = x
        self.matrixList = temp


    def __add__(self, other: 'Matrix'):
        temp = Matrix(self.width,  self.height, [])
        if self.width == other.width and self.height == other.height :
            for i in range(self.height):
                for j in range(self.width):
                    temp.matrixList[i][j] = self.matrixList[i][j] + other.matrixList[i][j]
        return temp

    def __mul__(self, other: 'Matrix'):
        tempM = copy.deepcopy(other)
        tempM.invert()
        newWidth = other.width
        newHeight = self.height
        tempVector = []
        if self.width == tempM.width and self.height == tempM.height :
            for i in range(newHeight):
                for j in range(newWidth):
                    tempVector.append(dotProduct(self.matrixList[i], tempM.matrixList[j]))

        ret = Matrix(newWidth, newHeight, tempVector)
        return ret


    def printMatrix(self):
        for line in self.matrixList:
            print(line)
        print('\n')