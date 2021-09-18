import sys
sys.setrecursionlimit(100001)


def dfs(p, mp=-1):
    global vnum, cactus
    dfn[p] = vnum
    vnum += 1
    res = 0
    for q in V[p]:
        if q == mp:
            continue
        if not dfn[q]:
            tmp = dfs(q, p)
            if res and tmp:
                cactus = False
            elif tmp:
                res = tmp
        elif dfn[p] > dfn[q]:
            if res:
                cactus = False
            res = q
    return 0 if res == p else res


N, M = map(int, sys.stdin.readline().split())
dfn = [0] * (N + 1)
vnum = 1
V = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    V[x].append(y)
    V[y].append(x)
cnt = 0
for i in range(1, N + 1):
    if not dfn[i]:
        cactus = True
        dfs(i)
        if cactus:
            cnt += 1
print(cnt)
