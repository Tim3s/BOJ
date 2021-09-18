import sys


def init(left, right, idx):
    if left == right:
        segment[idx] = ads[left]
    else:
        mid = (left + right) // 2
        segment[idx] = max(init(left, mid, 2 * idx), init(mid + 1, right, 2 * idx + 1))
    return segment[idx]


def getmax(left, right, idx):
    if l > right or r < left:
        return 0
    if l <= left and right <= r:
        return segment[idx]
    mid = (left + right) // 2
    return max(getmax(left, mid, 2 * idx), getmax(mid + 1, right, 2 * idx + 1))


N, M = map(int, sys.stdin.readline().split())
ads = list(map(int, sys.stdin.readline().split()))
segment = [0] * (N * 4)
init(0, N - 1, 1)
for l in range(N - 2 * M + 2):
    r = l + 2 * M - 2
    print(getmax(0, N - 1, 1), end=' ')
