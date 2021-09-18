import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    global target
    visited[n] = idx
    SCCcost[idx] += currency[n]
    if n in dest:
        SCCdest[idx] = True
    if n == S:
        target = idx
    for v in backward[n]:
        if visited[v] == -1:
            dfs2(v)
        elif visited[v] != idx:
            connected[visited[v]].append(idx)


N, M = map(int, sys.stdin.readline().split())
forward = [[] for _ in range(N + 1)]
backward = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    forward[A].append(B)
    backward[B].append(A)
currency = [0]
for _ in range(N):
    currency.append(int(sys.stdin.readline()))
S, P = map(int, sys.stdin.readline().split())
dest = set()
dest.update(set(map(int, sys.stdin.readline().split())))
visited = [False] * (N + 1)
stack = []
for i in range(1, N + 1):
    if not visited[i]:
        dfs1(i)
visited = [-1] * (N + 1)
idx = 0
target = -1
SCCdest = []
SCCcost = []
connected = []
while stack:
    cur = stack.pop()
    if visited[cur] == -1:
        connected.append([])
        SCCdest.append(False)
        SCCcost.append(0)
        dfs2(cur)
        idx += 1
q = deque()
q.append(target)
ans = 0
dp = [0] * len(SCCcost)
dp[target] = SCCcost[target]
while q:
    cur = q.popleft()
    if dp[cur] > ans and SCCdest[cur]:
        ans = dp[cur]
    for v in connected[cur]:
        if dp[cur] + SCCcost[v] > dp[v]:
            dp[v] = dp[cur] + SCCcost[v]
            q.append(v)
print(ans)
