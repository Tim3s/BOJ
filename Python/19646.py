import sys


def makesegment(left, right, idx):
    if left == right:
        segment[idx] = w[left]
        return w[left]
    mid = (left + right) // 2
    segment[idx] = makesegment(left, mid, 2 * idx) + makesegment(mid + 1, right, 2 * idx + 1)
    return segment[idx]


def get(left, right, idx, P):
    if left == right:
        segment[idx] = 0
        return left + 1, 0
    mid = (left + right) // 2
    if segment[idx * 2] < P:
        tmp = get(mid + 1, right, idx * 2 + 1, P - segment[idx * 2])
        segment[idx] = segment[idx * 2] + tmp[1]
    else:
        tmp = get(left, mid, idx * 2, P)
        segment[idx] = tmp[1] + segment[idx * 2 + 1]
    return tmp[0], segment[idx]


N = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))
segment = [0] * (N * 4)
makesegment(0, N - 1, 1)
for cur in p:
    print(get(0, N - 1, 1, cur)[0], end=' ')
