import sys


def dfs(p, mp=-1):
    global vnum, ans
    dfn[p] = vnum
    low[p] = vnum
    vnum += 1
    for q in V[p]:
        if q == mp:
            continue
        if not dfn[q]:
            S.append((p, q))
            dfs(q, p)
            low[p] = min(low[p], low[q])
            if dfn[p] <= low[q]:
                tmp = 0
                while S[-1] != (p, q):
                    S.pop()
                    tmp += 1
                S.pop()
                tmp += 1
                if tmp >= 3:
                    ans = max(ans, tmp)
        elif dfn[p] > dfn[q]:
            low[p] = min(low[p], dfn[q])
            S.append((p, q))


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    used = [False] * (N + 1)
    low = [sys.maxsize] * (N + 1)
    dfn = [0] * (N + 1)
    vnum = 1
    ans = 0
    S = []
    V = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        V[a].append(b)
        V[b].append(a)
    dfs(1)
    print(ans)
