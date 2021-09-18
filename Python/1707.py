import sys
from collections import deque


def bfs(start):
    q = deque()
    visited[start] = 1
    q.append((start, 1))
    while q:
        v, cur = q.popleft()
        cur = 3 - cur
        for vertex in e[v]:
            if not visited[vertex]:
                visited[vertex] = cur
                q.append((vertex, cur))
                continue
            if visited[vertex] != cur:
                return False
    return True


K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    e = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        e[a].append(b)
        e[b].append(a)
    visited = [0] * (V + 1)
    Bipartite = True
    for i in range(1, V + 1):
        if not visited[i]:
            if not bfs(i):
                Bipartite = False
                break
    print('YES' if Bipartite else 'NO')
