def update(x, val):
    while x <= n:
        tree[x] += val
        x += x & -x


def getsum(x):
    res = 0
    while x:
        res += tree[x]
        x -= x & -x
    return res


n = int(input())
tree = [0] * n
