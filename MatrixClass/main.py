from MatrixClass import Matrix

first = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
second = Matrix(2, 3, [6, 5, 4, 3, 2, 1])
first.printMatrix()
second.printMatrix()


for i in range(first.height):
    for j in range(first.width):
        print(first.matrixList[i][j])