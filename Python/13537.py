import sys
import bisect


def init(left, right, idx):
    if left == right:
        segment[idx].append(A[left])
    else:
        mid = (left + right) // 2
        segment[idx] = sorted(init(left, mid, idx * 2) + init(mid + 1, right, idx * 2 + 1))
    return segment[idx]


def getsum(left, right, idx):
    if j < left or i > right:
        return 0
    if i <= left and right <= j:
        return len(segment[idx]) - bisect.bisect_right(segment[idx], k)
    mid = (left + right) // 2
    return getsum(left, mid, 2 * idx) + getsum(mid + 1, right, 2 * idx + 1)


N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
segment = [[] for _ in range(N * 4)]
init(1, N, 1)
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    print(getsum(1, N, 1))
