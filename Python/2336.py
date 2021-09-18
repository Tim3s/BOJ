import sys


def update(left, right, idx):
    if B < left or B > right:
        return segment[idx]
    if left == right:
        segment[idx] = C
        return segment[idx]
    mid = (left + right) >> 1
    segment[idx] = min(update(left, mid, 2 * idx), update(mid + 1, right, 2 * idx + 1))
    return segment[idx]


def getmin(left, right, idx):
    if B >= right:
        return segment[idx]
    if B < left:
        return sys.maxsize
    mid = (left + right) >> 1
    return min(getmin(left, mid, idx * 2), getmin(mid + 1, right, idx * 2 + 1))


N = int(sys.stdin.readline())
exam = [[] for _ in range(N)]
for _ in range(3):
    tmp = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    for i in range(N):
        exam[tmp[i]].append(i)
exam.sort()
segment = [sys.maxsize] * (N * 4)
ans = 0
for A, B, C in exam:
    if getmin(0, N - 1, 1) > C:
        ans += 1
    update(0, N - 1, 1)
print(ans)
