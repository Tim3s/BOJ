import sys


def dp(left, right, cur):
    if cur == N - 1:
        return min(road[left][cur], road[right][cur])
    if memo[left][right] != -1:
        return memo[left][right]
    memo[left][right] = min(dp(left, cur, cur + 1) + road[cur][right], dp(right, cur, cur + 1) + road[cur][left])
    return memo[left][right]


N = int(sys.stdin.readline())
road = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [[-1] * N for _ in range(N)]
print(dp(0, 0, 1))
