import math
import condition_number

def matrix_multiply(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]

def matrix_transpose(A):
    return [list(row) for row in zip(*A)]

def is_symmetric(A):
    return all(row1 == row2 for row1, row2 in zip(A, matrix_transpose(A)))

def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0
    for j in range(n):
        submatrix = [row[:j] + row[j+1:] for row in A[1:]]
        sign = (-1) ** j
        det += sign * A[0][j] * determinant(submatrix)
    return det

def is_positive_definite(A):
    n = len(A)
    for i in range(1, n + 1):
        submatrix = [row[:i] for row in A[:i]]
        if determinant(submatrix) <= 0:
            return False
    return True

def check_determinants(A):
    n = len(A)
    for i in range(1, n + 1):
        submatrix = [row[:i] for row in A[:i]]
        det = determinant(submatrix)
        print(f"Det({i}) = {det:.2f}")
        if det <= 0:
            return False
    return True

A = [
    [5.18, 1.12, 0.95, 1.32, 0.83],
    [1.12, 6.28, 2.12, 0.57, 0.91],
    [0.95, 2.12, 6.13, 1.29, 1.57],
    [1.32, 0.57, 1.29, 5.67, 1.25],
    [0.83, 0.91, 1.57, 1.25, 5.21]
]

b = [8.64, 3.21, 1.83, 3.25, 7.4 ]

# A = [
#     [ 3, -1,  1],
#     [-1,  2,0.5],
#     [ 1,0.5,  3]
# ]

# b = [1,1.75, 2.5]

print("\nПеревірка умов збіжності методу Зейделя:")

print("\n1. A = A^T (симетричність):")
if is_symmetric(A):
    print("Матриця A є симетричною")
else:
    print("Матриця A не є симетричною")



print("\n2. Перевірка визначників головних мінорів:")
if check_determinants(A):
    print("Всі головні мінори додатні")
else:
    print("Не всі головні мінори додатні")

n = len(A)

x = [0] * n

epsilon=1e-4

max_iterations=1000

for iteration in range(max_iterations):
        x_new = x.copy()  
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))  
            sum2 = sum(A[i][j] * x[j] for j in range(i+1, n))  
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        print(f'{iteration} ітерація: {x_new}')      
          
        if all(abs(x_new[i] - x[i]) < epsilon for i in range(n)):
            print(f"Метод Зейделя зійшовся за {iteration + 1} ітерацій.")
            print(x_new,'\n')
            x = x_new
            break
        x = x_new

inverse = condition_number.inverse_matrix(A)

for row in inverse:
    print(row)
    
max_inverse = max([sum(row) for row in inverse])
print(max_inverse)
    
max_matrix = max([sum(row) for row in A])
print(max_matrix)

print(max_matrix * max_inverse)