import sys


def dp(cur, time):
    if time >= r - n:
        return sys.maxsize
    if cur == m:
        return 0
    if memo[cur][time] != -1:
        return memo[cur][time]
    memo[cur][time] = trick[cur][1] * (dp(cur + 1, time) + trick[cur + 1][0] - trick[cur][0])
    memo[cur][time] += (1 - trick[cur][1]) * min(mid, trick[cur + 1][0] - trick[cur][0] + trick[cur][2] + dp(cur + 1, time + trick[cur][2]))
    return memo[cur][time]


n, r, m = map(int, sys.stdin.readline().split())
trick = [[0, 0, 0]]
for _ in range(m):
    t, p, d = sys.stdin.readline().split()
    trick.append([int(t), float(p), int(d)])
trick.append([n, 0, 0])
m += 1
left = 0
right = 10 ** 20
for _ in range(50):
    memo = [[-1] * (r - n) for _ in range(m)]
    mid = (left + right) / 2
    if dp(0, 0) < mid:
        right = mid
    else:
        left = mid
print(mid)
