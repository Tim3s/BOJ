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
                if dfn[p] < low[q]:
                    cuts.append([p, q])
                tmp = set()
                if mp != -1:
                    ac[p] = True
                elif child[p] >= 2:
                    ac[p] = True
                while S[-1] != (p, q):
                    tmp.add(S.pop()[1])
                tmp.add(S.pop()[1])
                BCC.append(tmp)
        elif dfn[p] > dfn[q]:
            low[p] = min(low[p], dfn[q])
            S.append((p, q))


N, M = map(int, sys.stdin.readline().split())
# BCC
BCC = []
low = [sys.maxsize] * (N + 1)
child = [0] * (N + 1)
dfn = [0] * (N + 1)
vnum = 1
# cut vertex
ac = [False] * (N + 1)
S = []
V = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    V[A].append(B)
    V[B].append(A)
# cut edge
cuts = []
dfs(1)
