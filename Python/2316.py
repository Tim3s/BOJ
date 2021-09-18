import sys
from collections import deque

N, P = map(int, sys.stdin.readline().split())
network = [set() for _ in range(2 * N)]
flow = [[0] * (2 * N) for _ in range(2 * N)]
for i in range(N):
    flow[i][i + N] = 1
    network[i].add(i + N)
    network[i + N].add(i)
for _ in range(P):
    u, v = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    network[u + N].add(v)
    network[v].add(u + N)
    network[v + N].add(u)
    network[u].add(v + N)
    flow[u + N][v] += 1
    flow[v + N][u] += 1
ans = 0
while True:
    q = deque()
    q.append(N)
    back = [-1] * (2 * N)
    while q:
        u = q.popleft()
        for v in network[u]:
            if back[v] == -1 and flow[u][v]:
                back[v] = u
                q.append(v)
    if back[1] == -1:
        break
    cur = 1
    while cur != N:
        flow[back[cur]][cur] -= 1
        flow[cur][back[cur]] += 1
        cur = back[cur]
    ans += 1
print(ans)
