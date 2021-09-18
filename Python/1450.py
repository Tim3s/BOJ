import sys
from bisect import bisect_right


def calcA(last, w):
    if last == mid:
        asum.append(w)
        return
    calcA(last + 1, w)
    calcA(last + 1, w + a[last])


def calcB(last, w):
    if last == len(b):
        bsum.append(w)
        return
    calcB(last + 1, w)
    calcB(last + 1, w + b[last])


N, C = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))
mid = N // 2
a = weight[:mid]
b = weight[mid:]
asum = []
bsum = []
calcA(0, 0)
calcB(0, 0)
bsum.sort()
cnt = 0
for i in asum:
    cnt += bisect_right(bsum, C - i)
print(cnt)
