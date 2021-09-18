import sys
sys.setrecursionlimit(10 ** 9)


def dfs(x, d):
    global cnt
    cnt += 1
    into[x] = cnt
    depth[x] = d
    d += 1
    for v in E[x]:
        if not into[v]:
            dfs(v, d)
    out[x] = cnt


def update(x):
    while x <= N:
        tree[x] += 1
        x += x & -x


def getsum(x):
    res = 0
    while x:
        res += tree[x]
        x -= x & -x
    return res


N, C = map(int, sys.stdin.readline().split())
E = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    E[x].append(y)
    E[y].append(x)
into = [0] * (N + 1)
out = [0] * (N + 1)
depth = [0] * (N + 1)
cnt = 0
dfs(C, 1)
tree = [0] * (N + 1)
Q = int(sys.stdin.readline())
for _ in range(Q):
    op, A = map(int, sys.stdin.readline().split())
    if op == 1:
        update(into[A])
        continue
    print((getsum(out[A]) - getsum(into[A] - 1)) * depth[A])
