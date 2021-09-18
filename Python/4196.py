import sys
sys.setrecursionlimit(10 ** 9)


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    global indep
    visited[n] = idx
    for v in backward[n]:
        if not visited[v]:
            dfs2(v)
        elif visited[v] != idx:
            indep = False
    tmp.append(n)


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    forward = [[] for _ in range(N + 1)]
    backward = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        forward[A].append(B)
        backward[B].append(A)
    stack = []
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i]:
            dfs1(i)
    visited = [0] * (N + 1)
    ans = []
    cnt = 0
    idx = 1
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            indep = True
            tmp = []
            dfs2(cur)
            ans.append(tmp)
            if indep:
                cnt += 1
            idx += 1
    print(cnt)
