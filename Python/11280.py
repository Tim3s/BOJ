import sys
sys.setrecursionlimit(10 ** 9)


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    visited[n] = idx
    for v in backward[n]:
        if visited[v] == -1:
            dfs2(v)


N, M = map(int, sys.stdin.readline().split())
forward = [[] for _ in range(2 * N + 1)]
backward = [[] for _ in range(2 * N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    forward[-a].append(b)
    forward[-b].append(a)
    backward[b].append(-a)
    backward[a].append(-b)
stack = []
visited = [False] * (2 * N + 1)
for i in range(-N, 0):
    if not visited[i]:
        dfs1(i)
for i in range(1, N + 1):
    if not visited[i]:
        dfs1(i)
idx = 0
visited = [-1] * (2 * N + 1)
while stack:
    cur = stack.pop()
    if visited[cur] == -1:
        dfs2(cur)
        idx += 1
for i in range(1, N + 1):
    if visited[i] == visited[-i]:
        print(0)
        sys.exit(0)
print(1)
