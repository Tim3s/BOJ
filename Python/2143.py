import sys
import bisect

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
asum = []
for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += A[j]
        asum.append(tmp)
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
bsum = []
for i in range(m):
    tmp = 0
    for j in range(i, m):
        tmp += B[j]
        bsum.append(tmp)
bsum.sort()
ans = 0
for i in asum:
    ans += bisect.bisect_right(bsum, T - i) - bisect.bisect_left(bsum, T - i)
print(ans)
