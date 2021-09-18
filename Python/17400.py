import sys


def init(left, right, idx):
    if left == right:
        segment[idx] = c[left]
    else:
        mid = (left + right) // 2
        segment[idx] = init(left, mid, idx * 2) + init(mid + 1, right, idx * 2 + 1)
    return segment[idx]


def change(left, right, idx):
    if L < left or L > right:
        pass
    elif left == right:
        segment[idx] += -R if L % 2 else R
        return segment[idx]
    else:
        mid = (left + right) // 2
        segment[idx] = change(left, mid, 2 * idx) + change(mid + 1, right, 2 * idx + 1)
    return segment[idx]


def getsum(left, right, idx):
    if R < left or L > right:
        return 0
    if L <= left and right <= R:
        return segment[idx]
    mid = (left + right) // 2
    return getsum(left, mid, 2 * idx) + getsum(mid + 1, right, 2 * idx + 1)


N, Q = map(int, sys.stdin.readline().split())
c = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(1, N + 1, 2):
    c[i] *= -1
segment = [0] * (N * 4)
init(1, N, 1)
for _ in range(Q):
    op, L, R = map(int, sys.stdin.readline().split())
    if op == 1:
        print(abs(getsum(1, N, 1)))
    else:
        change(1, N, 1)
