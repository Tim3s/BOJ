import sys
sys.setrecursionlimit(10 ** 9)


def dfs(p, mp=-1):
    global vnum
    dfn[p] = vnum
    low[p] = vnum
    vnum += 1
    for q in v[p]:
        if q == mp:
            continue
        if not dfn[q]:
            child[p] += 1
            S.append((p, q))
            dfs(q, p)
            low[p] = min(low[p], low[q])
            if dfn[p] <= low[q]:
                if dfn[p] < low[q]:
                    ans.append(sorted([p, q]))
                tmp = []
                if mp != -1:
                    ac[p] = True
                elif child[p] >= 2:
                    ac[p] = True
                while S[-1] != (p, q):
                    tmp.append(S.pop())
                tmp.append(S.pop())
                BCC.append(tmp)
        elif dfn[p] > dfn[q]:
            low[p] = min(low[p], dfn[q])
            S.append((p, q))


V, E = map(int, sys.stdin.readline().split())
BCC = []
low = [sys.maxsize] * (V + 1)
child = [0] * (V + 1)
dfn = [0] * (V + 1)
vnum = 1
ac = [False] * (V + 1)
S = []
v = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B = map(int, sys.stdin.readline().split())
    v[A].append(B)
    v[B].append(A)
ans = []
dfs(1)
ans.sort()
print(len(ans))
for i in ans:
    print(*i)
