import sys

N, M = map(int, sys.stdin.readline().split())
num = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        if j < M - 2:
            long = num[i][j] + num[i][j + 1] + num[i][j + 2]
            if i != 0:
                res = max(res, long + num[i-1][j], long + num[i-1][j+1], long + num[i-1][j+2],\
                          num[i][j] + num[i][j+1] + num[i-1][j+1] + num[i-1][j+2])
            if i != N - 1:
                res = max(res, long + num[i+1][j], long + num[i+1][j+1], long + num[i+1][j+2],\
                          num[i][j] + num[i][j+1] + num[i+1][j+1] + num[i+1][j+2])
            if j < M - 3:
                res = max(res, long + num[i][j + 3])
        if i < N - 2:
            long = num[i][j] + num[i + 1][j] + num[i + 2][j]
            if j != 0:
                res = max(res, long + num[i][j - 1], long + num[i + 1][j - 1], long + num[i + 2][j - 1], \
                          num[i][j] + num[i + 1][j] + num[i + 1][j - 1] + num[i + 2][j - 1])
            if j != M - 1:
                res = max(res, long + num[i][j + 1], long + num[i + 1][j + 1], long + num[i + 2][j + 1], \
                          num[i][j] + num[i + 1][j] + num[i + 1][j + 1] + num[i + 2][j + 1])
            if i < N - 3:
                res = max(res, long + num[i + 3][j])
        if i != N - 1 and j != M - 1:
            res = max(res, num[i][j] + num[i + 1][j + 1] + num[i][j + 1] + num[i + 1][j])
print(res)
