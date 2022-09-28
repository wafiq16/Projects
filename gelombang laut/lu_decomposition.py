from triang import forsub, backsub, testcreate, testsolve
import numpy as np
import math


def ludec(A):
    n = A.shape[0]
    U = np.copy(A)
    L = np.identity(n)

    for j in range(n-1):
        for i in range(j+1, n):
            coeff = U[i, j]/U[j, j]
            U[i, j:] -= coeff*U[j, j:]
            L[i, j] = coeff

    return L, U


def lusolve(A, bs):
    L, U = ludec(A)
    ys = forsub(L, bs)
    xs = backsub(U, ys)
    return xs


if __name__ == '__main__':
    N = 8
    O = 3
    Z = [[5], [8], [14], [21], [30], [36], [45], [60]]
    T = [[21.75], [22.68], [25.62], [30.87], [40.5], [48.72], [63.75], [96]]
    G = [[0 for x in range(O)] for y in range(N)]
    for i in range(N):
        # print(i)
        G[i][0] = 1
        G[i][1] = Z[i][0]
        G[i][2] = math.pow(Z[i][0], 2)
    d = T
    G_T = np.transpose(G)
    # print(G)
    A = np.dot(G_T, G)
    b = np.dot(G_T, d)
    m = lusolve(A, b)
    a = len(m)
    print("+===========++===========+")
    print("| konstanta m | Nilai  |")
    print("+-----------++-----------+")
    for i in range(a):
        print("| m"+str(i+1) + "          |  " +
              str(round(m[i], 5)) + "  |")
        print("+-----------++-----------+")
    print("+===========++===========+")
# print("m"+str(i+1))
# print(m[i])
# A, bs = testcreate(4, 21)

# testsolve(lusolve, A, bs)
