import sys
from bisect import bisect_left, bisect_right


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


N, S = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
mid = N // 2
ans = 0
a = num[:mid]
b = num[mid:]
asum = []
bsum = []
calcA(0, 0)
calcB(0, 0)
bsum.sort()
for i in asum:
    ans += bisect_right(bsum, S - i) - bisect_left(bsum, S - i)
if S == 0:
    ans -= 1
print(ans)
