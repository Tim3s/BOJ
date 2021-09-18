import sys
sys.setrecursionlimit(1000000)


def dp(x):
    yet[x] = False
    memo[x][1] = 1
    memo[x][0] = 0
    for i in friend[x]:
        if yet[i]:
            dp(i)
            memo[x][0] += memo[i][1]
            memo[x][1] += min(memo[i][0], memo[i][1])


N = int(sys.stdin.readline())
friend = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    friend[u].append(v)
    friend[v].append(u)
memo = [[0] * 2 for _ in range(N + 1)]
yet = [True] * (N + 1)
dp(1)
print(min(memo[1][0], memo[1][1]))
