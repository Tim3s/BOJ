import sys


def dfs(p):
    vis[p] = True
    for q in V[p]:
        if b[q] == 0 or (not vis[b[q]] and dfs(b[q])):
            a[p] = q
            b[q] = p
            return True
    return False


N, K = map(int, sys.stdin.readline().split())
ans = 0
V = [[] for _ in range(N + 1)]
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    V[i].append(j)
a = [0] * (N + 1)
b = [0] * (N + 1)
for i in range(1, N + 1):
    vis = [False] * (N + 1)
    if dfs(i):
        ans += 1
print(ans)
