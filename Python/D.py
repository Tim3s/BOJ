import sys


def update(x, val):
    while x <= N + 1:
        tree[x] += val
        x += x & -x


def getsum(x):
    res = 0
    while x > 0:
        res += tree[x]
        x -= x & -x
    return res


def init(left, right, idx):
    if left == right:
        segment[idx] = A[left]
        return segment[idx]
    mid = (left + right) >> 1
    idx <<= 1
    segment[idx] = min(init(left, mid, idx), init(mid + 1, right, idx + 1))
    return segment[idx]


def updateseg(left, right, idx):
    if i < left or i > right:
        return segment[idx]
    if left == right:
        segment[idx] = j
        return segment[idx]
    mid = (left + right) >> 1
    idx <<= 1
    segment[idx] = min(updateseg(left, mid, idx), updateseg(mid + 1, right, idx + 1))
    return segment[idx]


def getl(left, right, idx):
    if segment[idx] >= j:
        return 0
    if left == right:
        return left if left <= i else 0
    mid = (left + right) >> 1
    idx <<= 1
    if mid >= i:
        return getl(left, mid, idx)
    return max(getl(left, mid, idx), getl(mid + 1, right, idx + 1))


def getr(left, right, idx):
    if segment[idx] >= j:
        return N + 1
    if left == right:
        return left if left >= i else N + 1
    mid = (left + right) >> 1
    idx <<= 1
    if mid <= i:
        return getr(mid + 1, right, idx + 1)
    return min(getr(left, mid, idx), getr(mid + 1, right, idx + 1))


N = int(sys.stdin.readline())
tree = [0] * (N + 1)
segment = [0] * (N * 4)
A = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(1, N + 1):
    update(i, A[i])
init(1, N, 1)
for _ in range(int(sys.stdin.readline())):
    q, i, j = map(int, sys.stdin.readline().split())
    if q == 1:
        update(i, j - A[i])
        A[i] = j
        updateseg(1, N, 1)
    else:
        l = getl(1, N, 1)
        r = getr(1, N, 1) - 1
        # print(l, r)
        # print(getsum(r))
        # print(getsum(l))
        print(getsum(r) - getsum(l))
