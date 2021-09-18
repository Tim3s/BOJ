import sys

while True:
    n = int(sys.stdin.readline())
    if not n:
        break
    w = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        if abs(w[i] - w[i + 1]) <= 1:
            dp[i][i + 1] = 2
    for diff in range(2, n):
        for i in range(n - diff):
            if dp[i + 1][i + diff - 1] == diff - 1:
                if abs(w[i] - w[i + diff]) <= 1:
                    dp[i][i + diff] = diff + 1
                else:
                    dp[i][i + diff] = diff - 1
            tmp = max([dp[i][j] + dp[j + 1][i + diff] for j in range(i, i + diff)])
            dp[i][i + diff] = max(dp[i][i + diff], tmp)
    print(dp[0][n - 1])
