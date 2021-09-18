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
        elif visited[v] != idx:
            valid[visited[v]] = False
    tmp.append(n)


while True:
    tmp = list(map(int, sys.stdin.readline().split()))
    if len(tmp) == 1:
        break
    V, E = tmp
    forward = [[] for _ in range(V + 1)]
    backward = [[] for _ in range(V + 1)]
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(0, len(tmp), 2):
        A = tmp[i]
        B = tmp[i + 1]
        forward[A].append(B)
        backward[B].append(A)
    stack = []
    visited = [False] * (V + 1)
    for i in range(1, V + 1):
        if not visited[i]:
            dfs1(i)
    visited = [-1] * (V + 1)
    res = []
    idx = 0
    valid = []
    while stack:
        cur = stack.pop()
        if visited[cur] == -1:
            tmp = []
            dfs2(cur)
            valid.append(True)
            res. append(tmp)
            idx += 1
    ans = []
    for i in range(len(res)):
        if valid[i]:
            ans += res[i]
    print(*sorted(ans))
