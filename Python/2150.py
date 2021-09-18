import sys
sys.setrecursionlimit(10 ** 9)


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    visited[n] = True
    for v in backward[n]:
        if not visited[v]:
            dfs2(v)
    tmp.append(n)


V, E = map(int, sys.stdin.readline().split())
forward = [[] for _ in range(V + 1)]
backward = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B = map(int, sys.stdin.readline().split())
    forward[A].append(B)
    backward[B].append(A)
stack = []
visited = [False] * (V + 1)
for i in range(1, V + 1):
    if not visited[i]:
        dfs1(i)
visited = [False] * (V + 1)
ans = []
while stack:
    cur = stack.pop()
    if not visited[cur]:
        tmp = []
        dfs2(cur)
        ans.append(sorted(tmp))
print(len(ans))
for cur in sorted(ans):
    print(*cur, -1)
