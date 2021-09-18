import sys


def out(left, right, idx):
    global B
    if left == right:
        segment[idx] -= 1
        print(left)
        return segment[idx]
    mid = (left + right) // 2
    if segment[idx * 2] < B:
        B -= segment[idx * 2]
        segment[idx] = segment[idx * 2] + out(mid + 1, right, idx * 2 + 1)
    else:
        segment[idx] = out(left, mid, idx * 2) + segment[idx * 2 + 1]
    return segment[idx]


def into(left, right, idx):
    if left > B or B > right:
        return
    segment[idx] += C
    if left != right:
        mid = (left + right) // 2
        into(left, mid, idx * 2)
        into(mid + 1, right, idx * 2 + 1)


n = int(sys.stdin.readline())
segment = [0] * 4000000
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp[0] == 1:
        A, B = tmp
        out(1, 1000000, 1)
    else:
        A, B, C = tmp
        into(1, 1000000, 1)

