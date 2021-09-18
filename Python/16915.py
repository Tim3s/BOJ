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
    for v in forward[n]:
        if visited[v] == -1:
            dfs2(v)


M, N = map(int, sys.stdin.readline().split())
door = [0] + list(map(int, sys.stdin.readline().split()))
switch = [[] for _ in range(M + 1)]
forward = [[] for _ in range(2 * N + 1)]
for i in range(1, N + 1):
    tmp = list(map(int, sys.stdin.readline().split()))[1:]
    for j in tmp:
        switch[j].append(i)
for i in range(1, M + 1):
    a, b = switch[i]
    if door[i]:
        forward[-a].append(-b)
        forward[-b].append(-a)
        forward[a].append(b)
        forward[b].append(a)
    else:
        forward[-a].append(b)
        forward[-b].append(a)
        forward[b].append(-a)
        forward[a].append(-b)
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
