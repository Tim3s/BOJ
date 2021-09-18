import sys

N = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[2147483647] * i for i in range(N, 0, -1)]
for i in range(N):
    dp[i][0] = 0
for j in range(1, N):
    for i in range(N - j):
        dp[i][j] = min([dp[i][k] + dp[i + k + 1][j - 1 - k] + mat[i][0] * mat[i + k][1] * mat[i + j][1] for k in range(j)])
print(dp[0][N - 1])
