import sys
from collections import deque


def bfs(x, p):
    visited[x] = True
    q = deque()
    q.append((x, p))
    res = 1
    while q:
        x, p = q.popleft()
        for v in edge[x]:
            if v != p:
                if visited[v]:
                    return 0
                visited[v] = True
                q.append((v, x))
    return 1


idx = 0
while True:
    idx += 1
    n, m = map(int, sys.stdin.readline().split())
    if n == m == 0:
        break
    edge = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        edge[a].append(b)
        edge[b].append(a)
    visited = [False] * (n + 1)
    tree = 0
    for i in range(1, n + 1):
        if not visited[i]:
            tree += bfs(i, -1)
    print('Case ' + str(idx) + ':', 'A forest of ' + str(tree) + ' trees.' if tree > 1 else 'There is one tree.' if tree == 1 else 'No trees.')
