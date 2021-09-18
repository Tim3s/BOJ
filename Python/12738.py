import bisect
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
length = []
for i in range(N):
    loc = bisect.bisect_left(length, A[i])
    if len(length) == loc:
        length.append(A[i])
    else:
        length[loc] = A[i]
print(len(length))
