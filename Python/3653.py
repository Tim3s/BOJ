import sys


def update(x, val):
    while x <= M:
        tree[x] += val
        x += x & -x


def getsum(x):
    res = 0
    while x:
        res += tree[x]
        x -= x & -x
    return res


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    M += N
    tree = [0] * (M + 1)
    loc = [0] + [i for i in range(N, 0, -1)]
    for i in range(1, N + 1):
        update(i, 1)
    watch = map(int, sys.stdin.readline().split())
    newidx = N + 1
    for i in watch:
        print(N - getsum(loc[i]), end=' ')
        update(loc[i], -1)
        loc[i] = newidx
        update(newidx, 1)
        newidx += 1
    print()
