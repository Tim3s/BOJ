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


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    forward = [[] for _ in range(N)]
    backward = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        forward[A].append(B)
        backward[B].append(A)
    stack = []
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    visited = [False] * N
    ans = []
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            tmp = []
            dfs2(cur)
            ans.append(sorted(tmp))
    onedegree = None
    for i in range(len(ans)):
        nodegree = True
        for v in ans[i]:
            for nv in backward[v]:
                if nv not in ans[i]:
                    nodegree = False
                    break
            if not nodegree:
                break
        if nodegree:
            if onedegree is not None:
                print("Confused")
                onedegree = None
                break
            else:
                onedegree = i
    if onedegree is not None:
        print('\n'.join(list(map(str, ans[onedegree]))))
    print()
    try:
        sys.stdin.readline()
    except:
        break
