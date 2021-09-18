import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
length = N
network = [set() for _ in range(length)]
flow = [[0] * length for _ in range(length)]
s = 0
e = length - 1
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    network[u].add(v)
    network[v].add(u)
    flow[u][v] = w
tmp = 0
while True:
    q = deque()
    q.append(s)
    back = [-1] * length
    while q:
        u = q.popleft()
        for v in network[u]:
            if back[v] == -1 and flow[u][v]:
                back[v] = u
                q.append(v)
    if back[e] == -1:
        break
    cur = e
    val = sys.maxsize
    while cur != s:
        val = min(val, flow[back[cur]][cur])
        cur = back[cur]
    cur = e
    while cur != s:
        flow[back[cur]][cur] -= val
        flow[cur][back[cur]] += val
        cur = back[cur]
    tmp += val
print(tmp)
