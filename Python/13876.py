import sys
from collections import deque
import copy

N = int(sys.stdin.readline())
length = 2 * N + 2
network = [set() for _ in range(length)]
base = [[0] * length for _ in range(length)]
s = 0
e = length - 1
vote = [[0, 0]]
voted = [0] * (N + 1)
for i in range(1, N + 1):
    u, v = map(int, sys.stdin.readline().split())
    vote.append([u, v])
    network[i].add(u + N)
    network[u + N].add(i)
    network[i].add(v + N)
    network[v + N].add(i)
    network[s].add(i)
    network[i].add(s)
    network[e].add(i + N)
    network[i + N].add(e)
    base[s][i] = 1
    voted[u] += 1
    voted[v] += 1
ans = 0
# print(voted)
for i in range(1, N + 1):
    # print('i:', i)
    tmp = 1
    flow = copy.deepcopy(base)
    for j in range(1, N + 1):
        if i == j:
            flow[j + N][e] = voted[i]
            continue
        if vote[j][1] != i:
            flow[j][vote[j][0] + N] = 1
        if vote[j][0] != i:
            flow[j][vote[j][1] + N] = 1
        if j in vote[i]:
            flow[j + N][e] = max(0, voted[i] - 2)
            continue
        flow[j + N][e] = max(0, voted[i] - 1)
    while True:
        # print(flow)
        q = deque()
        q.append(s)
        back = [-1] * length
        while q:
            u = q.popleft()
            for v in network[u]:
                if back[v] == -1 and flow[u][v]:
                    back[v] = u
                    q.append(v)
        # print(back)
        if back[e] == -1:
            break
        cur = e
        val = sys.maxsize
        while cur != s:
            val = min(val, flow[back[cur]][cur])
            cur = back[cur]
        cur = e
        # print(val)
        while cur != s:
            flow[back[cur]][cur] -= val
            flow[cur][back[cur]] += val
            cur = back[cur]
        tmp += val
    # print(tmp)
    if tmp != N:
        ans += 1
print(ans)
