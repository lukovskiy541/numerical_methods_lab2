from functools import reduce

import condition_number


matrix = [
    [5.18, 1.12, 0.00, 0.00, 0.00],
    [1.12, 4.28, 2.12, 0.00, 0.00],
    [0.00, 2.12, 6.13, 1.29, 0.00],
    [0.00, 0.00, 1.29, 4.57, 1.25],
    [0.00, 0.00, 0.00, 1.25, 5.21]
]

f = [8.64, 3.21, 1.83, 6.25, 7.40]


n = len(matrix)
a = [0] * n
b = [0] * n
c = [0] * n

for i in range(n):
    c[i] = matrix[i][i]
    if i > 0:
        a[i] = matrix[i][i-1]
    if i < n-1:
        b[i] = matrix[i][i+1]


n = len(c)
stable = True
strict_condition_met = False

for i in range(n):
    sum_ab = abs(a[i]) + abs(b[i])
    if abs(c[i]) < sum_ab:
        stable = False
        print(f"|{c[i]}| < |{a[i]}| + |{b[i]}| -> метод нестійкий")
    elif abs(c[i]) == sum_ab:
        print(f"|{c[i]}| = |{a[i]}| + |{b[i]}| -> умова виконується")
    else:
        strict_condition_met = True
        print(f"|{c[i]}| > |{a[i]}| + |{b[i]}| -> умова виконується")

if stable and strict_condition_met:
    print("Метод стійкий.")
else:
    print("Метод нестійкий.")
    
c,f = [(-c_i) for c_i in c], [(-f_i) for f_i in f]

print(c,f)

alpha = [0]*n

beta = [0]*n

z = [0]*(n-1)


for i in range(n-1):
    if i == 0:
        alpha[i] = b[i]/c[i]
        beta[i] = f[i]/c[i]
        print(f'alpha_1 = {alpha[i]}')
        print(f'beta_1 = {beta[i]}')
        z[i] = c[1] - alpha[i]*a[1]
        print(f'z_1 = {z[i]}')
    else:
        alpha[i] = b[i]/z[i-1]
        print(f'alpha_{i+1} = {alpha[i]}')
        beta[i] =(f[i] + a[i]*beta[i-1])/z[i-1]
        print(f'beta_{i+1}= {beta[i]}')
        z[i] = c[i+1] - alpha[i]*a[i+1]
        print(f'z_{i+1} = {z[i]}')

y = [0]*n

for j in reversed(range(n)):
    if j == n-1:
        y[n-1] = (f[n-1] + a[n-1]*beta[n-1])/z[n-2]
        print(f'y_{j} = {y[n-1]}')
    else:
        y[j] = alpha[j]*y[j+1] + beta[j]
        print(f'y_{j} = {y[j]}')
        

z_sum = reduce(lambda x, y: x * y, z)
print(f'Det A = {-c[0] * z_sum}')
print(f'Solution: ({y})')

inverse = condition_number.inverse_matrix(matrix)

for row in inverse:
    print(row)
    
max_inverse = max([sum(row) for row in inverse])
print(max_inverse)
    
max_matrix = max([sum(row) for row in matrix])
print(max_matrix)

print(max_matrix * max_inverse)