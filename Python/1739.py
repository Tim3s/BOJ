import sys
sys.setrecursionlimit(10 ** 9)


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    visited[n] = idx
    for v in backward[n]:
        if visited[v] == -1:
            dfs2(v)


T = int(sys.stdin.readline())
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    length = N + M
    forward = [[] for _ in range(2 * length + 1)]
    backward = [[] for _ in range(2 * length + 1)]
    for _ in range(K):
        a, b, c, d = map(int, sys.stdin.readline().split())
        b += N
        d += N
        if a == c and b == d:
            continue
        if a == c:
            if b < d:
                forward[-a].append(a)
                backward[a].append(-a)
                continue
            forward[a].append(-a)
            backward[-a].append(a)
            continue
        if b == d:
            if a < c:
                forward[-b].append(b)
                backward[b].append(-b)
                continue
            forward[b].append(-b)
            backward[-b].append(b)
            continue
        if b < d:
            forward[-a].append(c)
            forward[-c].append(a)
            backward[c].append(-a)
            backward[a].append(-c)
            if a < c:
                forward[-b].append(d)
                forward[-d].append(b)
                backward[d].append(-b)
                backward[b].append(-d)
                forward[-a].append(b)
                forward[-b].append(a)
                forward[-c].append(d)
                forward[-d].append(c)
                backward[b].append(-a)
                backward[a].append(-b)
                backward[d].append(-c)
                backward[c].append(-d)
                continue
            forward[b].append(-d)
            forward[d].append(-b)
            backward[-d].append(b)
            backward[-b].append(d)
            forward[-a].append(-b)
            forward[b].append(a)
            forward[-c].append(-d)
            forward[d].append(c)
            backward[-b].append(-a)
            backward[a].append(b)
            backward[-d].append(-c)
            backward[c].append(d)
            continue
        forward[a].append(-c)
        forward[c].append(-a)
        backward[-c].append(a)
        backward[-a].append(c)
        if a < c:
            forward[-b].append(d)
            forward[-d].append(b)
            backward[d].append(-b)
            backward[b].append(-d)
            forward[a].append(b)
            forward[-b].append(-a)
            forward[c].append(d)
            forward[-d].append(-c)
            backward[b].append(a)
            backward[-a].append(-b)
            backward[d].append(c)
            backward[-c].append(-d)
            continue
        forward[b].append(-d)
        forward[d].append(-b)
        backward[-d].append(b)
        backward[-b].append(d)
        forward[a].append(-b)
        forward[b].append(-a)
        forward[c].append(-d)
        forward[d].append(-c)
        backward[-b].append(a)
        backward[-a].append(b)
        backward[-d].append(c)
        backward[-c].append(d)
        continue
    stack = []
    visited = [False] * (2 * length + 1)
    for i in range(-length, 0):
        if not visited[i]:
            dfs1(i)
    for i in range(1, length + 1):
        if not visited[i]:
            dfs1(i)
    idx = 0
    visited = [-1] * (2 * length + 1)
    while stack:
        cur = stack.pop()
        if visited[cur] == -1:
            dfs2(cur)
            idx += 1
    valid = True
    for i in range(1, length + 1):
        if visited[i] == visited[-i]:
            print('No')
            valid = False
            break
    if valid:
        print('Yes')
