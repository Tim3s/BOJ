import sys
import bisect


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


N = int(sys.stdin.readline())
tree = [0] * (N + 1)
player = [0] + list(int(sys.stdin.readline()) for _ in range(N))
compress = sorted(player)
for i in range(1, N + 1):
    cur = bisect.bisect_left(compress, player[i])
    print(i - getsum(cur))
    update(cur)
