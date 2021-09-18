import sys


def update(x):
    while x <= 200000:
        tree[x] += 1
        x += x & -x


def getsum(x):
    res = 0
    while x:
        res += tree[x]
        x -= x & -x
    return res


def init(left, right, idx):
    if left == right:
        segment[idx] = data[left]
        return segment[idx]
    mid = (left + right) >> 1
    segment[idx] = max(init(left, mid, idx * 2), init(mid + 1, right, idx * 2 + 1))
    return segment[idx]


def getmax(left, right, idx):
    if left >= i:
        return 0
    if right < i:
        return segment[idx]
    mid = (left + right) >> 1
    return max(getmax(left, mid, idx * 2), getmax(mid + 1, right, idx * 2 + 1))


K = int(sys.stdin.readline())
ans = [0, 0]
tree = [0] * 200001
segment = [0] * 524288
data = list(map(int, sys.stdin.readline().split()))
init(0, K - 2, 1)
for i in range(K - 1, 0, -1):
    if data[i] * 2 + i < K:
        cur = getmax(0, K - 2, 1)
        if getsum(cur) >= data[i] * 2:
            ans = max(ans, [cur, data[i]])
    update(data[i])
if ans == [0, 0]:
    print(-1)
else:
    print(*ans)
