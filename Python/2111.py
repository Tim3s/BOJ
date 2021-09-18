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
                    ac[p] = True
                elif child[p] >= 2:
                    ac[p] = True
                while S[-1] != (p, q):
                    tmp.append(S.pop()[0])
                tmp.append(S.pop()[0])
                if len(tmp) >= 3:
                    BCC.append(tmp)
        elif dfn[p] > dfn[q]:
            low[p] = min(low[p], dfn[q])
            S.append((p, q))


N, M = map(int, sys.stdin.readline().split())
BCC = []
used = [False] * (N + 1)
low = [sys.maxsize] * (N + 1)
dfn = [0] * (N + 1)
child = [0] * (N + 1)
ac = [False] * (N + 1)
vnum = 1
S = []
V = [[] for _ in range(N + 1)]
for _ in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    for i in range(1, data[0]):
        V[data[i]].append(data[i + 1])
        V[data[i + 1]].append(data[i])
ans = 0
dfs(1)
for i in range(2, N + 1):
    if not dfn[i]:
        print(0)
        sys.exit(0)
if not BCC:
    print(1)
else:
    for i in range(len(BCC)):
        cur = set()
        for j in BCC[i]:
            if j in cur or (used[j] and not ac[j]):
                print(0)
                sys.exit(0)
            cur.add(j)
            used[j] = True
        BCC[i] = str(len(BCC[i]) + 1)
    print(eval('*'.join(BCC)))
