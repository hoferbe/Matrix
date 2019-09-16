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

    def __init__(self, matrixList, width, height):
        self.matrixList = matrixList
        self.width = width
        self.height = height

    @classmethod
    def newMatrix(cls, width, height, numbers: List[float]):
        matrixList = []
        if numbers == []:
            for i in range(height):
                temp = []
                for j in range(width):
                    temp.append(random.uniform(-1, 1))
                matrixList.append(temp)
        else:
            for i in range(height):
                matrixList.append(numbers[i*width : (i+1)*width])
        return cls(matrixList, width, height)

    @classmethod
    def fromFile(cls, inputString : str) -> 'Matrix':
        matrixList = []
        inputString = inputString.split(": ", 1)[1]
        width = int(inputString.split("\n", 1)[0])
        inputString = inputString.split(": ", 1)[1]
        height = int(inputString.split("\n", 1)[0])
        inputString = inputString.split("\n", 1)[1]
        for i in range(height):
            temp = []
            for j in range(width):
                temp.append(float(inputString.split(" ", 1)[0]))
                if j != height-1:
                    inputString = inputString.split(" ", 1)[1]
            matrixList.append(temp)
            inputString.split("\n", 1)[1]
            return cls(matrixList, width, height)



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

    def saveFunction(self):
        saveString = "Width: " + str(self.width) + "\nHeight: " + str(self.height) + "\n"
        for row in self.matrixList:
            for el in row:
                saveString += str(el) + " "
            saveString += "\n"
        return saveString