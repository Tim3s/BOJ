import sys


def update(left, right, idx):
    if index < left or index > right:
        return segment[idx]
    if left == right:
        segment[idx] = val
        return segment[idx]
    mid = (left + right) >> 1
    segment[idx] = min(update(left, mid, 2 * idx), update(mid + 1, right, 2 * idx + 1))
    return segment[idx]


def getmin(left, right, idx):
    if index >= right:
        return segment[idx]
    if index < left:
        return sys.maxsize
    mid = (left + right) >> 1
    return min(getmin(left, mid, idx * 2), getmin(mid + 1, right, idx * 2 + 1))


N, index, val = map(int, sys.stdin.readline().split())
segment = [0] * (N * 4)
