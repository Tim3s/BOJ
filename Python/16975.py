import sys


def makesegment(left, right, idx):
    if left == right:
        segment[idx] = num[left]
        return num[left]
    mid = (left + right) // 2
    segment[idx] = makesegment(left, mid, 2 * idx) + makesegment(mid + 1, right, 2 * idx + 1)
    return segment[idx]


def change(left, right, idx):
    if left <= i <= right or left <= j <= right:
        if left == right:
            if left == i:
                segment[idx] += k
            elif left == j:
                segment[idx] -= k
        else:
            mid = (left + right) // 2
            segment[idx] = change(left, mid, 2 * idx) + change(mid + 1, right, 2 * idx + 1)
    return segment[idx]


def getsum(left, right, idx):
    if 0 <= left and x >= right:
        return segment[idx]
    if 0 > right or x < left:
        return 0
    mid = (left + right) // 2
    return getsum(left, mid, idx * 2) + getsum(mid + 1, right, idx * 2 + 1)


N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
for i in range(N - 1, 0, -1):
    num[i] -= num[i - 1]
segment = [0] * (N * 4)
makesegment(0, N - 1, 1)
M = int(sys.stdin.readline())
for _ in range(M):
    Q = list(map(int, sys.stdin.readline().split()))
    if Q[0] == 1:
        Q, i, j, k = Q
        i -= 1
        change(0, N - 1, 1)
    else:
        Q, x = Q
        x -= 1
        print(getsum(0, N - 1, 1))
