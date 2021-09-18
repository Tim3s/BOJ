import sys


def makesegment(left, right, idx):
    if left == right:
        segment[idx] = num[left]
        return num[left]
    mid = (left + right) // 2
    segment[idx] = (makesegment(left, mid, 2 * idx) * makesegment(mid + 1, right, 2 * idx + 1)) % 1000000007
    return segment[idx]


def change(left, right, idx):
    if left <= b <= right:
        segment[idx] = segment[idx] * c * pow(tmp, 1000000005, 1000000007) % 1000000007
        if left == right:
            return
        mid = (left + right) // 2
        change(left, mid, 2 * idx)
        change(mid + 1, right, 2 * idx + 1)


def revise(left, right, idx):
    if left <= b <= right:
        if left == right == b:
            segment[idx] = c
        else:
            mid = (left + right) // 2
            segment[idx] = (revise(left, mid, 2 * idx) * revise(mid + 1, right, 2 * idx + 1)) % 1000000007
    return segment[idx]


def getsum(left, right, idx):
    if b <= left and c >= right:
        return segment[idx]
    if b > right or c < left:
        return 1
    mid = (left + right) // 2
    return (getsum(left, mid, idx * 2) * getsum(mid + 1, right, idx * 2 + 1)) % 1000000007


N, M, K = map(int, sys.stdin.readline().split())
num = [int(sys.stdin.readline()) for _ in range(N)]
segment = [0] * (N * 4)
makesegment(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    b -= 1
    if a == 1:
        tmp = num[b]
        num[b] = c
        if tmp != 0:
            change(0, N - 1, 1)
            continue
        revise(0, N - 1, 1)
        continue
    c -= 1
    print(getsum(0, N - 1, 1))
