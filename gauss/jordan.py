import numpy as np
import sys

a = np.array([[10, 2, -1],
              [-3, -6, 2],
              [1, 1, 5]], float)
b = np.array([27, -61.5, 21.5], float)
aug = np.column_stack((a, b.T))
n = aug.shape[0]
print(n)
x = np.zeros(n)

for i in range(n):
    print(i)
    if aug[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(n):
        if i != j:
            ratio = aug[j][i]/aug[i][i]

            for k in range(n+1):
                aug[j][k] = aug[j][k] - ratio * aug[i][k]

for i in range(n):
    x[i] = aug[i][n]/aug[i][i]

print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')
