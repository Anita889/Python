class Matrix:
    def __init__(self, rows, cols, values=None):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

        if values:
            if len(values) == rows and all(len(row) == cols for row in values):
                self.data = values
            else:
                raise ValueError("Smth went wrong")

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Smth went wrong")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Smth went wrong")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Error")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

product_matrix = matrix1 * matrix2
print("\nProduct of matrices:")
print(product_matrix)
print("\n")

matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix(2, 3, [[5, 6, 7], [2, 3, 1]])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

sum_matrix = matrix1 + matrix2
print("\nSum of matrices:")
print(sum_matrix)
print("\n")

difference_matrix = matrix1 - matrix2
print("\nDifference of matrices:")
print(difference_matrix)