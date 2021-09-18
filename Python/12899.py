import sys


def update(left, right, idx):
    while True:
        segment[idx] += 1
        if left == right:
            return
        mid = (left + right) >> 1
        idx <<= 1
        if X > mid:
            left = mid + 1
            idx += 1
            continue
        right = mid
    # if X < left or X > right:
    #     return segment[idx]
    # if left == right:
    #     segment[idx] += 1
    #     return segment[idx]
    # mid = (left + right) >> 1
    # segment[idx] = update(left, mid, idx * 2) + update(mid + 1, right, idx * 2 + 1)
    # return segment[idx]


def get(left, right, idx):
    global X
    while True:
        segment[idx] -= 1
        if left == right:
            print(left)
            return
        idx <<= 1
        if X > segment[idx]:
            X -= segment[idx]
            left = ((left + right) >> 1) + 1
            idx += 1
            continue
        right = (left + right) >> 1


N = int(sys.stdin.readline())
segment = [0] * 4194304
for _ in range(N):
    T, X = map(int, sys.stdin.readline().split())
    if T & 1:
        update(1, 2000000, 1)
        continue
    get(1, 2000000, 1)
