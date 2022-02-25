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
            S.append((p, q))
            dfs(q, p)
            low[p] = min(low[p], low[q])
            if dfn[p] <= low[q]:
                tmp = set()
                tmpmax = cost[S[-1]]
                while S[-1] != (p, q):
                    tmp.add(S.pop())
                    tmpmax = max(tmpmax, cost[S[-1]])
                tmp.add(S.pop())
                if len(tmp) >= 3:
                    BCC.append(tmp)
                    BCCMAX.append(tmpmax)
        elif dfn[p] > dfn[q]:
            low[p] = min(low[p], dfn[q])
            S.append((p, q))


N, M, Q = map(int, sys.stdin.readline().split())
# BCC
BCC = []
low = [sys.maxsize] * (N + 1)
dfn = [0] * (N + 1)
vnum = 1
S = []
V = [[] for _ in range(N + 1)]
cost = dict()
allsum = 0
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    V[A].append(B)
    V[B].append(A)
    cost[(A, B)] = C
    cost[(B, A)] = C
    allsum += C
BCCMAX = []
dfs(1)

mincost = allsum - sum(BCCMAX)
print(mincost)
for _ in range(Q):
    u, v, d = map(int, sys.stdin.readline().split())
    # cost[(u, v)] = cost[(v, u)] = d
    modified = False
    for i in range(len(BCC)):
        if (u, v) in BCC[i] or (v, u) in BCC[i]:
            if d > BCCMAX[i]:
                mincost += BCCMAX[i] - cost[(u, v)]
                cost[(u, v)] = cost[(v, u)] = d
                BCCMAX[i] = d
            elif BCCMAX[i] == cost[(u, v)]:
                mincost += d
                cost[(u, v)] = cost[(v, u)] = d
                BCCMAX[i] = max([cost[cur] for cur in BCC[i]])
                mincost -= BCCMAX[i]
            else:
                mincost += d - cost[(u, v)]
                cost[(u, v)] = cost[(v, u)] = d
            modified = True
            break
    if not modified:
        mincost += d - cost[(u, v)]
        cost[(u, v)] = cost[(v, u)] = d
    print(mincost)
