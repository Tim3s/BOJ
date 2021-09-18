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


N, M = map(int, sys.stdin.readline().split())
length = N + M
museum = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
forward = [[] for _ in range(2 * length + 1)]
for i in range(N):
    for j in range(M):
        if museum[i][j] == '#':
            a = 1 + i
            b = N + j + 1
            forward[-a].append(-b)
            forward[-b].append(-a)
            forward[a].append(b)
            forward[b].append(a)
        elif museum[i][j] == '*':
            a = 1 + i
            b = N + j + 1
            forward[-a].append(b)
            forward[-b].append(a)
            forward[b].append(-a)
            forward[a].append(-b)
stack = []
visited = [False] * (2 * length + 1)
for i in range(-length, 0):
    if not visited[i]:
        dfs1(i)
for i in range(1, length + 1):
    if not visited[i]:
        dfs1(i)
idx = 0
visited = [-1] * (2 * length + 1)
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
