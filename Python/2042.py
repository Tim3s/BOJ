import sys


def makesegment(left, right, idx):
    if left == right:
        segment[idx] = num[left]
        return num[left]
    mid = (left + right) // 2
    segment[idx] = makesegment(left, mid, 2 * idx) + makesegment(mid + 1, right, 2 * idx + 1)
    return segment[idx]


def change(left, right, idx):
    if left <= b <= right:
        segment[idx] += tmp
        if left == right:
            return
        mid = (left + right) // 2
        change(left, mid, 2 * idx)
        change(mid + 1, right, 2 * idx + 1)


def getsum(left, right, idx):
    if b <= left and c >= right:
        return segment[idx]
    if b > right or c < left:
        return 0
    mid = (left + right) // 2
    return getsum(left, mid, idx * 2) + getsum(mid + 1, right, idx * 2 + 1)


N, M, K = map(int, sys.stdin.readline().split())
num = [int(sys.stdin.readline()) for _ in range(N)]
segment = [0] * (N * 4)
makesegment(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    b -= 1
    if a == 1:
        tmp = c - num[b]
        num[b] = c
        change(0, N - 1, 1)
    else:
        c -= 1
        print(getsum(0, N - 1, 1))
