from MatrixClass import Matrix


vec =  Matrix(1, 3, [1, 2, 3])
Mat = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
Mat.printMatrix()
vec.printMatrix()
vec2 = Matrix(1, 2, [])

vec2 = Mat*vec
vec2.printMatrix()