import sys


def init(l, r, idx):
    if l == r:
        maximum[idx] = middle[idx] = left[idx] = right[idx] = A[l]
        return
    mid = (l + r) >> 1
    tmp1 = 2 * idx
    tmp2 = tmp1 + 1
    init(l, mid, tmp1)
    init(mid + 1, r, tmp2)
    middle[idx] = middle[tmp1] + middle[tmp2]
    left[idx] = max(left[tmp1], middle[tmp1] + left[tmp2])
    right[idx] = max(right[tmp2], right[tmp1] + middle[tmp2])
    maximum[idx] = max(right[tmp1] + left[tmp2], maximum[tmp1], maximum[tmp2])


def getsum(l, r, idx):
    if i <= l and r <= j:
        return left[idx], middle[idx], right[idx], maximum[idx]
    mid = (l + r) >> 1
    idx <<= 1
    if i > mid:
        return getsum(mid + 1, r, idx + 1)
    if j <= mid:
        return getsum(l, mid, idx)
    tmp1 = getsum(l, mid, idx)
    tmp2 = getsum(mid + 1, r, idx + 1)
    return max(tmp1[0], tmp1[1] + tmp2[0]), tmp1[1] + tmp2[1], max(tmp2[2], tmp1[2] + tmp2[1]), \
           max(tmp1[3], tmp2[3], tmp1[2] + tmp2[0])


N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))
middle = [0] * (N * 4)
left = [0] * (N * 4)
right = [0] * (N * 4)
maximum = [0] * (N * 4)
init(1, N, 1)
M = int(sys.stdin.readline())
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(getsum(1, N, 1)[3])
