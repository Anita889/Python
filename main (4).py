import random

def generate_random_matrix(rows, cols):
    matrix = [[random.randint(1, 100) for item in range(cols)] for item in range(rows)]
    return matrix

def get_column_sum(matrix, col_index):
    col_sum = sum(row[col_index] for row in matrix)
    return col_sum

def get_row_average(matrix, row_index):
    row = matrix[row_index]
    row_average = sum(row) / len(row)
    return row_average

row = 3
col = 4
my_matrix = generate_random_matrix(row, col)
print("Generated Matrix:")
for row in my_matrix:
    print(row)

column_index = 2
column_sum = get_column_sum(my_matrix, column_index)
print(f"Sum of column {column_index + 1}: {column_sum}")

row_index = 1
row_average = get_row_average(my_matrix, row_index)
print(f"Average of row {row_index + 1}: {row_average}")