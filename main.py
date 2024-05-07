import numpy as np

# Функция для вычисления определителя матрицы
def det(matrix):
    determinant = np.linalg.det(matrix)
    return determinant

# Функция для решения системы уравнений
def solve(matrix_A, matrix_b):
    solution = np.linalg.solve(matrix_A, matrix_b)
    return solution

matrix_A = np.array([[1, 2], [3, 4]])
matrix_b = np.array([5, 6])

determinant_result = det(matrix_A)
solution_result = solve(matrix_A, matrix_b)

print("Определитель матрицы А:")
print(determinant_result)

print("\nРешение системы уравнений:")
print(solution_result)