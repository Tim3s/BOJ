import sys
sys.setrecursionlimit(10 ** 9)


def dfs(p, mp=-1):
    global vnum, ans
    dfn[p] = vnum
    low[p] = vnum
    child = 0
    vnum += 1
    for q in V[p]:
        if q == mp:
            continue
        if not dfn[q]:
            child += 1
            S.append((p, q))
            dfs(q, p)
            low[p] = min(low[p], low[q])
            if dfn[p] <= low[q]:
                tmp = set()
                if mp != -1:
                    ac[p] = True
                elif child >= 2:
                    ac[p] = True
                while S[-1] != (p, q):
                    tmp.update(S.pop())
                tmp.update(S.pop())
                BCC.append(tmp)
        elif dfn[p] > dfn[q]:
            low[p] = min(low[p], dfn[q])
            S.append((p, q))


case = 0
while True:
    case += 1
    N = int(sys.stdin.readline())
    if not N:
        break
    V = [[] for _ in range(N + 2)]
    for _ in range(N):
        s, t = map(int, sys.stdin.readline().split())
        V[s].append(t)
        V[t].append(s)
    dfn = [0] * (N + 2)
    low = [0] * (N + 2)
    S = []
    BCC = []
    vnum = 1
    ans = 1
    ac = [False] * (N + 2)
    dfs(1)
    if len(BCC) == 1:
        print("Case", str(case) + ':', 2, len(BCC[0]) * (len(BCC[0]) - 1) // 2)
        continue
    num = 0
    for i in BCC:
        cnt = 0
        for j in i:
            if ac[j]:
                cnt += 1
        if cnt == 1:
            ans *= (len(i)) - 1
            num += 1
    print("Case", str(case) + ':', num, ans)
