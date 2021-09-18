import sys


def dp(cur, used):
    if memo[cur][used] != -1:
        return memo[cur][used]
    res = 0
    for v in V[cur]:
        res = max(res, dp(v, 0), dp(v, 1))
    if used:
        res = (res / 2) + enjoyment[cur]
    memo[cur][used] = res
    return res


n, m = map(int, sys.stdin.readline().split())
enjoyment = list(map(int, sys.stdin.readline().split()))
ans = 0
V = [[] for _ in range(n)]
for _ in range(m):
    s, t = map(int, sys.stdin.readline().split())
    V[s].append(t)
memo = [[-1] * 2 for _ in range(n)]
print(format(max(dp(0, 1), dp(0, 0)), '.10f'))
