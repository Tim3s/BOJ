import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
network = [set() for _ in range(n)]
flow = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    network[a].add(b)
    network[b].add(a)
    flow[a][b] += c
    flow[b][a] += c
ans = 0
while True:
    q = deque()
    q.append(0)
    back = [-1] * n
    while q:
        u = q.popleft()
        for v in network[u]:
            if back[v] == -1 and flow[u][v]:
                back[v] = u
                q.append(v)
    if back[n - 1] == -1:
        break
    cur = n - 1
    val = sys.maxsize
    while cur:
        val = min(val, flow[back[cur]][cur])
        cur = back[cur]
    cur = n - 1
    while cur:
        flow[back[cur]][cur] -= val
        flow[cur][back[cur]] += val
        cur = back[cur]
    ans += val
print(ans)
