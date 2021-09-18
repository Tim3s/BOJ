import sys
sys.setrecursionlimit(10 ** 9)


def dfs(p, mp=-1):
    global vnum
    dfn[p] = vnum
    low[p] = vnum
    vnum += 1
    for q in V[p]:
        if q == mp:
            continue
        if not dfn[q]:
            child[p] += 1
            S.append((p, q))
            dfs(q, p)
            low[p] = min(low[p], low[q])
            if dfn[p] <= low[q]:
                tmp = []
                if mp != -1:
                    ac[p] += 1
                elif child[p] >= 2:
                    ac[p] = 1
                while S[-1] != (p, q):
                    tmp.append(S.pop())
                tmp.append(S.pop())
                BCC.append(tmp)
        elif dfn[p] > dfn[q]:
            low[p] = min(low[p], dfn[q])
            S.append((p, q))


while True:
    P, C = map(int, sys.stdin.readline().split())
    if P == C == 0:
        sys.exit(0)
    if C == 0:
        print(P - 1)
        continue
    V = [[] for _ in range(P)]
    for _ in range(C):
        p1, p2 = map(int, sys.stdin.readline().split())
        V[p1].append(p2)
        V[p2].append(p1)
    BCC = []
    low = [sys.maxsize] * P
    child = [0] * P
    dfn = [0] * P
    vnum = 1
    ac = [0] * P
    S = []
    component = 0
    for i in range(P):
        if not dfn[i]:
            component += 1
            dfs(i)
    print(component + max(ac))
