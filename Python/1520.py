import sys
sys.setrecursionlimit(10 ** 9)


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < N and 0 <= ny < M and town[nx][ny] < town[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]


N, M = map(int, sys.stdin.readline().split())
town = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dp[-1][-1] = 1
print(dfs(0, 0))
