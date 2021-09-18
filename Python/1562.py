import sys


def dfs(n, cur, visited):
    if n == N:
        if visited == (1 << 10) - 1:
            return 1
        return 0
    if memo[n][cur][visited] != -1:
        return memo[n][cur][visited]
    memo[n][cur][visited] = 0
    if cur > 0:
        memo[n][cur][visited] += dfs(n + 1, cur - 1, visited | 1 << (cur - 1))
    if cur < 9:
        memo[n][cur][visited] += dfs(n + 1, cur + 1, visited | 1 << (cur + 1))
    return memo[n][cur][visited]


N = int(sys.stdin.readline())
memo = [[[-1] * (1 << 10) for _ in range(10)] for _ in range(N)]
ans = 0
for i in range(1, 10):
    ans += dfs(1, i, 1 << i)
print(ans % 1000000000)
