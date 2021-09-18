import sys


def dfs(p):
    vis[p] = True
    for q in V[p]:
        if b[q] == 0 or (not vis[b[q]] and dfs(b[q])):
            a[p] = q
            b[q] = p
            return True
    return False


N, M = map(int, sys.stdin.readline().split())
ans = 0
V = [[] for _ in range(2 * N + 1)]
for i in range(1, N + 1):
    V[i] = list(map(int, sys.stdin.readline().split()))[1:]
    V[i + N] = V[i]
a = [0] * (2 * N + 1)
b = [0] * (M + 1)
for i in range(1, 2 * N + 1):
    vis = [False] * (2 * N + 1)
    if dfs(i):
        ans += 1
print(ans)
