import sys


def init(left, right, idx):
    if left == right:
        segment[idx] = A[left]
    else:
        mid = (left + right) // 2
        segment[idx] = init(left, mid, 2 * idx) + init(mid + 1, right, 2 * idx + 1)
    return segment[idx]


def change(left, right, idx):
    if left <= l <= right:
        segment[idx] += 1 if r else -1
        if left != right:
            mid = (left + right) // 2
            change(left, mid, 2 * idx)
            change(mid + 1, right, 2 * idx + 1)


def getsum(left, right, idx):
    if l > right or r < left:
        return 0
    if l <= left and right <= r:
        return segment[idx]
    mid = (left + right) // 2
    return getsum(left, mid, 2 * idx) + getsum(mid + 1, right, 2 * idx + 1)


N = int(sys.stdin.readline())
A = [0] + list(map(lambda x: int(x) % 2, sys.stdin.readline().split()))
segment = [0] * (N * 4)
init(1, N, 1)
M = int(sys.stdin.readline())
for _ in range(M):
    op, l, r = map(int, sys.stdin.readline().split())
    if op == 1:
        r %= 2
        if r != A[l]:
            A[l] = r
            change(1, N, 1)
    elif op == 2:
        print(r - l + 1 - getsum(1, N, 1))
    else:
        print(getsum(1, N, 1))
