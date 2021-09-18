import sys
from collections import deque

N = int(sys.stdin.readline())
pipe = [set() for _ in range(52)]
flow = [[0] * 52 for _ in range(52)]
for _ in range(N):
    u, v, r = sys.stdin.readline().split()
    if u.isupper():
        u = ord(u) - 65
    else:
        u = ord(u) - 71
    if v.isupper():
        v = ord(v) - 65
    else:
        v = ord(v) - 71
    pipe[u].add(v)
    pipe[v].add(u)
    flow[u][v] += int(r)
    flow[v][u] += int(r)
while True:
    q = deque()
    q.append(0)
    back = [-1] * 52
    while q:
        u = q.popleft()
        for v in pipe[u]:
            if back[v] == -1 and flow[u][v]:
                back[v] = u
                q.append(v)
    if back[25] == -1:
        break
    cur = 25
    val = sys.maxsize
    while cur:
        val = min(val, flow[back[cur]][cur])
        cur = back[cur]
    cur = 25
    while cur:
        flow[back[cur]][cur] -= val
        flow[cur][back[cur]] += val
        cur = back[cur]
ans = 0
for i in range(52):
    ans += max(0, (flow[25][i] - flow[i][25]) // 2)
print(ans)
