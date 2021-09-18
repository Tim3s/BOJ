import sys


def dfs(cur, visited):
    if visited == (1 << N) - 1:
        if not cost[cur][0]:
            return sys.maxsize
        return cost[cur][0]
    if dp[cur][visited] != sys.maxsize:
        return dp[cur][visited]
    for i in range(N):
        tmp = 1 << i
        if cost[cur][i] and not tmp & visited:
            dp[cur][visited] = min(dp[cur][visited], dfs(i, tmp | visited) + cost[cur][i])
    return dp[cur][visited]


N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[sys.maxsize] * (1 << N) for _ in range(N)]
print(dfs(0, 1))
