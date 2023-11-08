class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def printMatrix(self):
        for i in range(n):
          for j in range(m):
             print(self.matrix[i][j], end=" ")
          print()

    def calculateAverag(self):
        total = sum(sum(row) for row in self.matrix)
        return total / (self.n * self.m)

    def calculateRowSum(self, row_idx):
        if 0 <= row_idx < self.n:
            return sum(self.matrix[row_idx])
        return None

    def calculateColumnAverage(self, col_idx):
        if 0 <= col_idx < self.m:
            col_sum = sum(row[col_idx] for row in self.matrix)
            return col_sum / self.n
        return None

    def printSubmatrix(self, col1, col2, row1, row2):
        if 0 <= col1 < self.m and 0 <= col2 < self.m and 0 <= row1 < self.n and 0 <= row2 < self.n:
            for i in range(row1, row2 + 1):
                for j in range(col1, col2 + 1):
                    print(self.matrix[i][j], end=" ")
                print()
        else:
            print("Invalid submatrix coordinates")

n = 3
m = 4
matrix = Matrix(n, m)

matrix.matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Matrix:")
matrix.printMatrix()

mean = matrix.calculateAverag()
print("Mean of the matrix:", mean)

row_sum = matrix.calculateRowSum(1) 
print("Sum of row 2:", row_sum)

column_avg = matrix.calculateColumnAverage(2) 
print("Average of column 3:", column_avg)

print("Submatrix:")
matrix.printSubmatrix(1, 3, 0, 2) 
