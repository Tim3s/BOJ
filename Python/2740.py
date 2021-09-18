import sys

N, M = [int(i) for i in sys.stdin.readline().split()]
A = [[int(i) for i in sys.stdin.readline().split()] for j in range(N)]
K = int(sys.stdin.readline().split()[1])
B = [[int(i) for i in sys.stdin.readline().split()] for j in range(M)]
C = [[0] * K for i in range(N)]
for i in range(N):
    for j in range(K):
        mysum = 0
        for k in range(M):
            mysum += A[i][k] * B[k][j]
        C[i][j] = mysum
for i in range(N):
    print(' '.join([str(i) for i in C[i]]))
