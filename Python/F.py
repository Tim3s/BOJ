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
        if not visited[v]:
            dfs2(v)
        elif visited[v] != idx:
            newv[visited[v] - 1].add(idx - 1)
    tmp.append(n)


def dfs(n):
    if joy2[n] != [0, 0]:
        return joy2[n]
    minval = 10 ** 18
    maxval = 0
    for v in ans[n]:
        minval = min(minval, C[v])
        maxval = max(maxval, C[v])
    for v in newv[n]:
        tmpmin, tmpmax = dfs(v)
        minval = min(minval, tmpmin)
        maxval = max(maxval, tmpmax)
    res = maxval - minval
    for v in ans[n]:
        joy[v] = res
    return minval, maxval


V = int(sys.stdin.readline())
C = [0] + list(map(int, sys.stdin.readline().split()))
D = [0] + list(map(int, sys.stdin.readline().split()))
forward = [[] for _ in range(V + 1)]
backward = [[] for _ in range(V + 1)]
for _ in range(V - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    if D[u] >= w:
        forward[u].append(v)
        backward[v].append(u)
    if D[v] >= w:
        forward[v].append(u)
        backward[u].append(v)
stack = []
visited = [False] * (V + 1)
for i in range(1, V + 1):
    if not visited[i]:
        dfs1(i)
visited = [0] * (V + 1)
ans = []
idx = 0
newv = []
while stack:
    cur = stack.pop()
    if not visited[cur]:
        # SCC
        idx += 1
        tmp = []
        newv.append(set())
        dfs2(cur)
        ans.append(tmp)
joy = [0] * (V + 1)
joy2 = [[0, 0] for _ in range(idx)]
print(newv)
print(ans)
for i in range(idx):
    if joy2[0] == [0, 0]:
        dfs(i)
print(joy)
