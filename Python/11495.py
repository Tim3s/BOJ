import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    length = N * M + 2
    network = [set() for _ in range(length)]
    flow = [[0] * length for _ in range(length)]
    grids = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    allsum = sum([sum(grids[i]) for i in range(N)])
    s = length - 2
    e = length - 1
    for i in range(N):
        for j in range(M):
            cur = i * M + j
            if (i + j) % 2:
                network[s].add(cur)
                network[cur].add(s)
                flow[s][cur] = grids[i][j]
                if i:
                    network[cur].add(cur - M)
                    network[cur - M].add(cur)
                    flow[cur][cur - M] = grids[i][j]
                if j:
                    network[cur].add(cur - 1)
                    network[cur - 1].add(cur)
                    flow[cur][cur - 1] = grids[i][j]
                if i < N - 1:
                    network[cur].add(cur + M)
                    network[cur + M].add(cur)
                    flow[cur][cur + M] = grids[i][j]
                if j < M - 1:
                    network[cur].add(cur + 1)
                    network[cur + 1].add(cur)
                    flow[cur][cur + 1] = grids[i][j]
                continue
            network[cur].add(e)
            network[e].add(cur)
            flow[cur][e] = grids[i][j]
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
    print(allsum - tmp)
