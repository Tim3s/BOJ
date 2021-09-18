import sys
import copy
from collections import deque


def init(x):
    res = copy.deepcopy(base)
    _cur = N
    for _i in range(1, N + 1):
        for _j in range(last - N, last):
            _cur += 1
            res[_i][_cur] = x
    return res


N = int(sys.stdin.readline())
row = list(map(int, sys.stdin.readline().split()))
column = list(map(int, sys.stdin.readline().split()))
length = N ** 2 + 2 * N + 2
last = length - 1
base = [[0] * length for _ in range(length)]
network = [[] for _ in range(length)]
for i in range(1, N + 1):
    network[0].append(i)
    network[i].append(0)
    base[0][i] = row[i - 1]
    network[last].append(last - i)
    network[last - i].append(last)
    base[last - i][last] = column[-i]
cur = N
for i in range(1, N + 1):
    for j in range(last - N, last):
        cur += 1
        network[i].append(cur)
        network[cur].append(i)
        network[cur].append(j)
        network[j].append(cur)
        base[cur][j] = column[j - last]
# print(network)
# print(base)
tmpsum = sum(column)
left = 0
right = max(max(row), max(column))
ans = right
while right >= left:
    mid = (left + right) // 2
    flow = init(mid)
    tmp = 0
    while True:
        q = deque()
        q.append(0)
        back = [-1] * length
        while q:
            u = q.popleft()
            for v in network[u]:
                if back[v] == -1 and flow[u][v]:
                    back[v] = u
                    q.append(v)
        if back[last] == -1:
            break
        cur = last
        val = sys.maxsize
        while cur:
            val = min(val, flow[back[cur]][cur])
            cur = back[cur]
        cur = last
        while cur:
            flow[back[cur]][cur] -= val
            flow[cur][back[cur]] += val
            cur = back[cur]
        tmp += val
    if tmp != tmpsum:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid
print(ans)
flow = init(ans)
while True:
    q = deque()
    q.append(0)
    back = [-1] * length
    while q:
        u = q.popleft()
        for v in network[u]:
            if back[v] == -1 and flow[u][v]:
                back[v] = u
                q.append(v)
    if back[last] == -1:
        break
    cur = last
    val = sys.maxsize
    while cur:
        val = min(val, flow[back[cur]][cur])
        cur = back[cur]
    cur = last
    while cur:
        flow[back[cur]][cur] -= val
        flow[cur][back[cur]] += val
        cur = back[cur]
for i in range(N + 1, N ** 2 + N + 1, N):
    tmp = (i - 1) // N
    for j in range(i, i + N):
        print(flow[j][tmp], end=' ')
    print()
