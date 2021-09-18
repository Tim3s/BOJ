import sys


def dp(left, right, pos):
    global cost
    if memo[left][right][pos] < sys.maxsize:
        return memo[left][right][pos]
    if left == 0 and right == N - 1:
        return 0
    loc = right if pos else left
    if left != 0:
        tmp = cost * (light[loc][0] - light[left - 1][0])
        cost -= light[left - 1][1]
        memo[left][right][pos] = dp(left - 1, right, 0) + tmp
        cost += light[left - 1][1]
    if right < N - 1:
        tmp = cost * (light[right + 1][0] - light[loc][0])
        cost -= light[right + 1][1]
        memo[left][right][pos] = min(memo[left][right][pos], dp(left, right + 1, 1) + tmp)
        cost += light[right + 1][1]
    return memo[left][right][pos]


N, M = map(int, sys.stdin.readline().split())
light = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cost = sum([light[i][1] for i in range(N)])
cost -= light[M - 1][1]
memo = [[[sys.maxsize] * 2 for _ in range(N)] for _ in range(N)]
print(dp(M - 1, M - 1, 0))
