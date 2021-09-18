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
    global idx, start, end
    visited[n] = idx
    if n == S:
        start = idx
    elif n == T:
        end = idx
    for v in backward[n]:
        if visited[v] == -1:
            dfs2(v)
        elif visited[v] != idx:
            connected[visited[v]].add(idx)
    tmp.append(n)


N, M, S, T = map(int, sys.stdin.readline().split())
forward = [[] for _ in range(N + 1)]
backward = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    forward[A].append(B)
    backward[B].append(A)
visited = [False] * (N + 1)
stack = []
for i in range(1, N + 1):
    if not visited[i]:
        dfs1(i)
visited = [-1] * (N + 1)
idx = 0
connected = []
ans = []
start = 0
end = 0
while stack:
    cur = stack.pop()
    if visited[cur] == -1:
        tmp = []
        dfs2(cur)
        ans.append(tmp)
        connected.append(set())
        idx += 1
q = deque()
for i in range(len(ans)):
    ans[i] = len(ans[i])
q.append(start)
res = [0] * len(ans)
res[start] = ans[start]
while q:
    cur = q.popleft()
    for v in connected[cur]:
        if res[cur] + ans[v] > res[v]:
            res[v] = res[cur] + ans[v]
            q.append(v)
print(res[end])
