import sys
from collections import deque

N, P = map(int, sys.stdin.readline().split())
network = [set() for _ in range(N)]
flow = [[0] * N for _ in range(N)]
for _ in range(P):
    u, v = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    network[u].add(v)
    network[v].add(u)
    flow[u][v] += 1
ans = 0
while True:
    q = deque()
    q.append(0)
    back = [-1] * N
    while q:
        u = q.popleft()
        for v in network[u]:
            if back[v] == -1 and flow[u][v]:
                back[v] = u
                q.append(v)
    if back[1] == -1:
        break
    cur = 1
    val = sys.maxsize
    while cur:
        val = min(val, flow[back[cur]][cur])
        cur = back[cur]
    cur = 1
    while cur:
        flow[back[cur]][cur] -= val
        flow[cur][back[cur]] += val
        cur = back[cur]
    ans += val
print(ans)
