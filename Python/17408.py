import sys


def init(left, right, idx):
    if left == right:
        segment[idx] = A[left]
        index[idx] = left
        return segment[idx], index[idx]
    mid = (left + right) >> 1
    segment[idx], index[idx] = max(init(left, mid, idx * 2), init(mid + 1, right, idx * 2 + 1))
    return segment[idx], index[idx]


def change(left, right, idx):
    if l < left or l > right:
        return segment[idx], index[idx]
    if left == right:
        segment[idx] = r
        return segment[idx], index[idx]
    mid = (left + right) >> 1
    segment[idx], index[idx] = max(change(left, mid, 2 * idx), change(mid + 1, right, 2 * idx + 1))
    return segment[idx], index[idx]


def getmax(left, right, idx):
    if r < left or l > right:
        return 0, 0
    if l <= left and right <= r:
        return segment[idx], index[idx]
    mid = (left + right) // 2
    return max(getmax(left, mid, 2 * idx), getmax(mid + 1, right, 2 * idx + 1))


N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))
segment = [0] * (N * 4)
index = [0] * (N * 4)
init(1, N, 1)
M = int(sys.stdin.readline())
for _ in range(M):
    op, l, r = map(int, sys.stdin.readline().split())
    if op == 1:
        change(1, N, 1)
        continue
    max1, tmp = getmax(1, N, 1)
    if tmp == l:
        l += 1
        print(max1 + getmax(1, N, 1)[0])
    elif tmp == r:
        r -= 1
        print(max1 + getmax(1, N, 1)[0])
    else:
        tmp2 = r
        r = tmp - 1
        max2 = getmax(1, N, 1)[0]
        r = tmp2
        l = tmp + 1
        print(max1 + max(max2, getmax(1, N, 1)[0]))
