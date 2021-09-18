import sys
sys.setrecursionlimit(10 ** 9)


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    visited[n] = idx
    for v in backward[n]:
        if visited[v] == -1:
            dfs2(v)


N, M = map(int, sys.stdin.readline().split())
forward = [[] for _ in range(2 * N + 1)]
backward = [[] for _ in range(2 * N + 1)]
for _ in range(M):
    a1, b1, a2, b2, a3, b3 = sys.stdin.readline().split()
    a1 = int(a1)
    a2 = int(a2)
    a3 = int(a3)
    if b1 == 'R':
        a1 *= -1
    if b2 == 'R':
        a2 *= -1
    if b3 == 'R':
        a3 *= -1
    forward[-a1].append(a2)
    forward[-a2].append(a1)
    forward[-a1].append(a3)
    forward[-a3].append(a1)
    forward[-a2].append(a3)
    forward[-a3].append(a2)
    backward[a1].append(-a2)
    backward[a2].append(-a1)
    backward[a1].append(-a3)
    backward[a3].append(-a1)
    backward[a2].append(-a3)
    backward[a3].append(-a2)
stack = []
visited = [False] * (2 * N + 1)
for i in range(-N, 0):
    if not visited[i]:
        dfs1(i)
for i in range(1, N + 1):
    if not visited[i]:
        dfs1(i)
idx = 0
ans = ['R'] * (N + 1)
visited = [-1] * (2 * N + 1)
while stack:
    cur = stack.pop()
    if visited[cur] == -1:
        dfs2(cur)
        idx += 1
for i in range(1, N + 1):
    if visited[i] == visited[-i]:
        print(-1)
        sys.exit(0)
    if visited[i] > visited[-i]:
        ans[i] = 'B'
print(''.join(ans[1:]))
