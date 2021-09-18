import sys


def update(x):
    while x <= 200001:
        tree[x] += 1
        tree2[x] += X
        tree2[x] %= 1000000007
        x += x & -x


def getsum(x):
    res1 = 0
    res2 = 0
    while x:
        res1 += tree[x]
        res2 += tree2[x]
        x -= x & -x
    return [res1, res2]


N = int(sys.stdin.readline())
tree = [0] * 200002
tree2 = [0] * 200002
X = int(sys.stdin.readline()) + 1
update(X)
ans = 1
for _ in range(N - 1):
    X = int(sys.stdin.readline()) + 1
    left = getsum(X - 1)
    right = getsum(200001)
    tmp = getsum(X)
    right[0] -= tmp[0]
    right[1] -= tmp[1]
    ans *= ((left[0] - right[0]) * X - left[1] + right[1]) % 1000000007
    ans %= 1000000007
    update(X)
print(ans)
