import sys

N = int(sys.stdin.readline())
dp = [[[sys.maxsize] * 3 for _ in range(3)] for _ in range(N)]
tmp = list(map(int, sys.stdin.readline().split()))
for i in range(3):
    dp[0][i][i] = tmp[i]
for i in range(1, N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(3):
        for k in range(3):
            dp[i][j][k] = min([dp[i][j][k]] + [dp[i - 1][j][l] + tmp[k] for l in range(k - 2, k)])
print(min([dp[-1][i][j] for i in range(3) for j in range(3) if i != j]))
