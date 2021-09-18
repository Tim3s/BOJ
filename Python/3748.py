import sys
sys.setrecursionlimit(10 ** 9)


def dfs(p, mp=-1):
    global vnum, BCC, valid, ans, num, bccnum
    dfn[p] = vnum
    res = vnum
    vnum += 1
    for q in V[p]:
        if q == mp:
            continue
        if not dfn[q]:
            S.append((p, q))
            ret = dfs(q, p)
            if dfn[p] <= ret:
                cnt = 1
                root[bccnum] = q
                while S[-1] != (p, q):
                    cnt += 1
                    BCC[bccnum].update(S.pop())
                BCC[bccnum].update(S.pop())
                if cnt >= 3:
                    todo[bccnum] = True
                bccnum += 1
                continue
            res = min(res, ret)
            continue
        if dfn[p] > dfn[q]:
            res = min(res, dfn[q])
            S.append((p, q))
    return res


def check(p, seq):
    global valid
    current.add(p)
    visited[p] = i
    num[p] = seq
    seq += 1
    for v in V[p]:
        if v not in BCC[i]:
            continue
        if visited[v] != i:
            check(v, seq)
            continue
        if not (num[p] - num[v]) % 2:
            valid = True


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    if N <= 2:
        print(0)
        continue
    V = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        V[a].append(b)
        V[b].append(a)
    BCC = [set() for _ in range(N + 1)]
    root = [0] * N
    S = []
    vnum = 1
    bccnum = 1
    dfn = [0] * (N + 1)
    ans = [False] * (N + 1)
    num = [0] * (N + 1)
    todo = [False] * (N + 1)
    for i in range(1, N + 1):
        if not dfn[i]:
            dfs(i)
    cnt = 0
    visited = [0] * (N + 1)
    for i in range(1, bccnum):
        if todo[i]:
            current = set()
            valid = False
            check(root[i], 1)
            if valid:
                for v in current:
                    ans[v] = True
    for i in range(1, N + 1):
        if ans[i]:
            cnt += 1
    print(cnt)
