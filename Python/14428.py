import sys


def init(left, right, idx):
    if left == right:
        segment[idx] = [num[left], left]
        return segment[idx]
    mid = (left + right) // 2
    segment[idx] = min(init(left, mid, 2 * idx), init(mid + 1, right, 2 * idx + 1))
    return segment[idx]


def change(left, right, idx):
    if left == right:
        if left == p:
            segment[idx][0] += q
    elif left <= p <= right:
        mid = (left + right) // 2
        segment[idx] = min(change(left, mid, 2 * idx), change(mid + 1, right, 2 * idx + 1))
    return segment[idx]


def getmin(left, right, idx):
    if p <= left and q >= right:
        return segment[idx]
    if q < left or p > right:
        return [sys.maxsize, 0]
    mid = (left + right) // 2
    return min(getmin(left, mid, 2 * idx), getmin(mid + 1, right, 2 * idx + 1))


N = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
segment = [0, 0] * (N * 4 + 4)
init(1, N, 1)
M = int(sys.stdin.readline())
for _ in range(M):
    op, p, q = map(int, sys.stdin.readline().split())
    if op == 1:
        tmp = q
        q -= num[p]
        num[p] = tmp
        change(1, N, 1)
    else:
        print(getmin(1, N, 1)[1])
