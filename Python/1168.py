import sys


def init(left, right, idx):
    if left == right:
        segment[idx] = 1
        return segment[idx]
    mid = (left + right) >> 1
    segment[idx] = init(left, mid, idx * 2) + init(mid + 1, right, idx * 2 + 1)
    return segment[idx]


def get(cur):
    left = 1
    right = N
    idx = 1
    while True:
        segment[idx] -= 1
        if left == right:
            print(left, end='')
            return
        idx <<= 1
        if cur > segment[idx]:
            cur -= segment[idx]
            left = ((left + right) >> 1) + 1
            idx += 1
            continue
        right = (left + right) >> 1


N, K = map(int, sys.stdin.readline().split())
segment = [0] * (N * 4)
init(1, N, 1)
idx = 1
K -= 1
print('<', end='')
for i in range(N - 1):
    idx = (idx + K - 1) % (N - i) + 1
    get(idx)
    print(', ', end='')
get(1)
print('>')
