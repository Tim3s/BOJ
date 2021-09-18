import sys

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))
    for i in range(1, K):
        C[i] += C[i - 1]
    dp = [[0] * K for _ in range(K)]
    for i in range(1, K):
        dp[0][i] = C[i]
    for i in range(1, K):
        for j in range(i + 1, K):
            dp[i][j] = C[j] - C[i - 1]
    for difference in range(2, K):
        for i in range(K - difference):
            j = i + difference
            dp[i][j] += min([dp[i][k] + dp[k + 1][j] for k in range(i, j)])
    print(dp[0][K - 1])
