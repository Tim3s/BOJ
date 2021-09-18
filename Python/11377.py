import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
length = N + M + 3
network = [set() for _ in range(length)]
flow = [[0] * length for _ in range(length)]
s = length - 2
s1 = 0
network[s].add(s1)
network[s1].add(s)
flow[s][s1] = K
e = length - 1
for i in range(1, N + 1):
    network[s1].add(i)
    network[i].add(s1)
    flow[s1][i] = 1
    network[s].add(i)
    network[i].add(s)
    flow[s][i] = 1
    works = list(map(lambda x: int(x) + N, sys.stdin.readline().split()))[1:]
    for j in works:
        network[i].add(j)
        network[j].add(i)
        flow[i][j] = 1
for j in range(N + 1, N + M + 1):
    network[j].add(e)
    network[e].add(j)
    flow[j][e] = 1
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
