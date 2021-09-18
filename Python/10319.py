import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    i, g, t = map(int, sys.stdin.readline().split())
    i -= 1
    length = N * (t + 1) + 2
    network = [[] for _ in range(length)]
    flow = [[0] * length for _ in range(length)]
    s = length - 2
    e = length - 1
    for start in range(i, s, N):
        network[s].append(start)
        network[start].append(s)
        flow[s][start] = g
    for i in range(0, t * N, N):
        for j in range(i, i + N):
            network[j].append(j + N)
            network[j + N].append(j)
            flow[j][j + N] = g
    M = int(sys.stdin.readline())
    for _ in range(M):
        x = int(sys.stdin.readline()) - 1
        for i in range(x, s, N):
            network[i].append(e)
            network[e].append(i)
            flow[i][e] = g
    r = int(sys.stdin.readline())
    for _ in range(r):
        a, b, p, k = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        for i in range(0, s, N):
            if i + N * k < s:
                network[i + a].append(i + N * k + b)
                network[i + N * k + b].append(i + a)
                flow[i + a][i + N * k + b] = p
                continue
            break
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
    print(min(tmp, g))
