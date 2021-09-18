import sys


def change(left, right, idx):
    if left == right:
        if left == p:
            segment[idx] += q
    elif left <= p <= right:
        mid = (left + right) // 2
        segment[idx] = change(left, mid, 2 * idx) + change(mid + 1, right, 2 * idx + 1)
    return segment[idx]


def getsum(left, right, idx):
    if p <= left and q >= right:
        return segment[idx]
    if q < left or p > right:
        return 0
    mid = (left + right) // 2
    return getsum(left, mid, 2 * idx) + getsum(mid + 1, right, 2 * idx + 1)


N, Q = map(int, sys.stdin.readline().split())
segment = [0] * ((N + 1) * 4)
for _ in range(Q):
    op, p, q = map(int, sys.stdin.readline().split())
    if op == 1:
        change(1, N, 1)
    else:
        print(getsum(1, N, 1))
