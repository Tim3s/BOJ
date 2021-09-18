import sys
sys.setrecursionlimit(1000000)


def dfs(p, mp=-1):
    global vnum, newvnum
    dfn[p] = vnum
    low[p] = vnum
    vnum += 1
    cnt = 0
    for q in V[p]:
        if q == mp:
            if cnt == 0:
                cnt += 1
                continue
            else:
                cnt += 1
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
                    reversing[unused] = q
                    newvnum += 1
        elif dfn[p] > dfn[q]:
            low[p] = min(low[p], dfn[q])
            S.append((p, q))


def dfs2(x):
    visited[x] = True
    if len(newv[x]) == 1:
        leaf.append(x)
    for node in newv[x]:
        if not visited[node]:
            dfs2(node)


N, M = map(int, sys.stdin.readline().split())
V = [[] for _ in range(N + 1)]
for _ in range(M):
    C1, C2 = map(int, sys.stdin.readline().split())
    V[C1].append(C2)
    V[C2].append(C1)
dfn = [0] * (N + 1)
low = [0] * (N + 1)
used = [-1] * (N + 1)
cuts = []
S = []
reversing = [0] * (N + 1)
vnum = 1
newvnum = 0
dfs(1)
if used[1] == -1:
    used[1] = newvnum
    reversing[newvnum] = 1
    newvnum += 1
newv = [[] for _ in range(newvnum)]
if len(newv) == 1:
    print(0)
    sys.exit(0)
for u, v in cuts:
    left = used[u]
    right = used[v]
    if left == right:
        continue
    newv[left].append(right)
    newv[right].append(left)
leaf = []
visited = [False] * newvnum
dfs2(0)
# print(used)
# print(leaf)
print((len(leaf) + 1) // 2)
if len(leaf) % 2:
    left = 0
    right = len(leaf) // 2 + 1
    while right != len(leaf):
        print(reversing[leaf[left]], reversing[leaf[right]])
        left += 1
        right += 1
    print(reversing[leaf[len(leaf) // 2]], reversing[leaf[0]])
else:
    left = 0
    right = len(leaf) // 2
    while right != len(leaf):
        print(reversing[leaf[left]], reversing[leaf[right]])
        left += 1
        right += 1
