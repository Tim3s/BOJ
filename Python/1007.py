import sys
import math


def dfs(x, y, cnt, n):
    if cnt == N // 2:
        return math.sqrt((xsum - 2 * x) ** 2 + (ysum - 2 * y) ** 2)
    if N == 2 * (n - cnt):
        x += sum(dots[i][0] for i in range(n, N))
        y += sum(dots[i][1] for i in range(n, N))
        return math.sqrt((xsum - 2 * x) ** 2 + (ysum - 2 * y) ** 2)
    return min(dfs(x, y, cnt, n + 1), dfs(x + dots[n][0], y + dots[n][1], cnt + 1, n + 1))


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    xsum = sum(dots[i][0] for i in range(N))
    ysum = sum(dots[i][1] for i in range(N))
    print(dfs(0, 0, 0, 0))
