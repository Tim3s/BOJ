import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
length = N + M + 2
s = N
e = N + 1
pig = [0] + list(map(int, sys.stdin.readline().split()))
network = [set() for _ in range(length)]
flow = [[0] * length for _ in range(length)]
customer = []
user = [[] for _ in range(M + 1)]
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    customer.append(tmp[1:-1])
    for j in customer[-1]:
        for k in user[j]:
            network[i].add(k)
            network[k].add(i)
            flow[i][k] = sys.maxsize
        user[j].append(i)
        network[i].add(length - j)
        network[-j].add(i)
        flow[i][-j] = sys.maxsize
    network[s].add(i)
    network[i].add(s)
    flow[s][i] = tmp[-1]
for i in range(1, M + 1):
    network[-i].add(e)
    network[e].add(length - i)
    flow[-i][e] = pig[i]
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
