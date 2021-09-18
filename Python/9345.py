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
    if A <= left and B >= right:
        return minimum[idx], maximum[idx]
    if A > right or B < left:
        return sys.maxsize, 0
    mid = (left + right) // 2
    tmp1 = getm(left, mid, 2 * idx)
    tmp2 = getm(mid + 1, right, 2 * idx + 1)
    return min(tmp1[0], tmp2[0]), max(tmp1[1], tmp2[1])


def change(left, right, idx):
    if left <= A <= right or left <= B <= right:
        if left == right:
            if left == A or left == B:
                minimum[idx] = num[left]
                maximum[idx] = num[left]
        else:
            mid = (left + right) // 2
            tmp1 = change(left, mid, 2 * idx)
            tmp2 = change(mid + 1, right, 2 * idx + 1)
            minimum[idx] = min(tmp1[0], tmp2[0])
            maximum[idx] = max(tmp1[1], tmp2[1])
    return minimum[idx], maximum[idx]


T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    num = [i for i in range(N)]
    minimum = [0] * (N * 4)
    maximum = [0] * (N * 4)
    makesegment(0, N - 1, 1)
    for _ in range(K):
        Q, A, B = map(int, sys.stdin.readline().split())
        if Q:
            tmp = getm(0, N - 1, 1)
            if A <= tmp[0] <= tmp[1] <= B:
                print('YES')
            else:
                print('NO')
        else:
            tmp = num[A]
            num[A] = num[B]
            num[B] = tmp
            change(0, N - 1, 1)
