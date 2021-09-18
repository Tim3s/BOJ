import sys


def mul(mat1, mat2):
    C = [[0] * len(mat2[0]) for i in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            mysum = 0
            for k in range(len(mat2)):
                mysum += mat1[i][k] * mat2[k][j]
            C[i][j] = mysum % 1000
    return C


def I(n):
    mat = [[0] * n for i in range(n)]
    for i in range(n):
        mat[i][i] = 1
    return mat


def exp(mat, n):
    a = I(len(mat))
    while n > 0:
        if n % 2:
            a = mul(a, mat)
        mat = mul(mat, mat)
        n //= 2
    return a


N, B = [int(i) for i in sys.stdin.readline().split()]
A = [[int(i) for i in sys.stdin.readline().split()] for j in range(N)]
res = exp(A, B)
for i in range(N):
    print(' '.join([str(i) for i in res[i]]))
