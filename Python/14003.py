import bisect
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
length = []
idx = []
B = [-1] * N
for i in range(N):
    loc = bisect.bisect_left(length, A[i])
    if loc != 0:
        B[i] = idx[loc - 1]
    if len(length) == loc:
        length.append(A[i])
        idx.append(i)
    else:
        length[loc] = A[i]
        idx[loc] = i
print(len(length))
result = []
cur = idx[-1]
while cur != -1:
    result.append(A[cur])
    cur = B[cur]
print(' '.join(list(map(str, reversed(result)))))
