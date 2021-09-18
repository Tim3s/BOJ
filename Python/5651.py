import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    length = N + 1
    network = [set() for _ in range(length)]
    flow = [[0] * length for _ in range(length)]
    E = []
    s = 1
    e = N
    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        if w:
            E.append([u, v])
            network[u].add(v)
            network[v].add(u)
            flow[u][v] += w
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
    ans = 0
    for s, e in E:
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
            ans += 1
    print(ans)
