import sys
sys.setrecursionlimit(10 ** 9)


def dfs(p, mp=-1):
    global vnum, newvnum
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
                if dfn[p] < low[q]:
                    cuts.append((p, q))
                tmp = []
                while S[-1] != (p, q):
                    tmp.append(S.pop()[1])
                tmp.append(S.pop()[1])
                unused = newvnum
                for node in tmp:
                    if used[node] >= 0:
                        unused = used[node]
                        break
                for node in tmp:
                    used[node] = unused
                if unused == newvnum:
                    newvnum += 1
        elif dfn[p] > dfn[q]:
            low[p] = min(low[p], dfn[q])
            S.append((p, q))


def final(node, parent=-1):
    res = [-1, node]
    for newnode in newv[node]:
        if newnode == parent:
            continue
        res = max(res, final(newnode, node))
    res[0] += 1
    return res


n, m = map(int, sys.stdin.readline().split())
V = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    V[u].append(v)
    V[v].append(u)
used = [-1] * n
dfn = [0] * n
low = [0] * n
ans = -1
for i in range(n):
    if used[i] == -1:
        S = []
        ans += 1
        vnum = 1
        cuts = []
        newvnum = 0
        dfs(i)
        # print(S)
        # print(cuts)
        # print(BCC)
        if newvnum:
            if used[i] == -1:
                used[i] = newvnum
                newvnum += 1
            newv = [[] for _ in range(newvnum)]
            for u, v in cuts:
                newv[used[u]].append(used[v])
                newv[used[v]].append(used[u])
            # print('almost')
            # print(final(0))
            ans += final(final(0)[1])[0]
            continue
        used[i] = 0
# print(used)
print(ans)
