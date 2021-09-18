import sys


def makesegment(left, right, idx):
    if left == right:
        minimum[idx] = num[left]
        maximum[idx] = num[left]
    else:
        mid = (left + right) // 2
        tmp1 = makesegment(left, mid, 2 * idx)
        tmp2 = makesegment(mid + 1, right, 2 * idx + 1)
        minimum[idx] = min(tmp1[0], tmp2[0])
        maximum[idx] = max(tmp1[1], tmp2[1])
    return minimum[idx], maximum[idx]


def getm(left, right, idx):
    if a <= left and b >= right:
        return minimum[idx], maximum[idx]
    if a > right or b < left:
        return sys.maxsize, 0
    mid = (left + right) // 2
    tmp1 = getm(left, mid, 2 * idx)
    tmp2 = getm(mid + 1, right, 2 * idx + 1)
    return min(tmp1[0], tmp2[0]), max(tmp1[1], tmp2[1])


N, M = map(int, sys.stdin.readline().split())
num = [int(sys.stdin.readline()) for _ in range(N)]
minimum = [0] * (N * 4)
maximum = [0] * (N * 4)
makesegment(0, N - 1, 1)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    print(*getm(0, N - 1, 1))
