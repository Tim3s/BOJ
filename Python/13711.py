import sys
import bisect

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
memo = [0] * (N + 1)
for i in range(N):
    memo[B[i]] = i
for i in range(N):
    A[i] = memo[A[i]]
length = []
for i in range(N):
    tmp = bisect.bisect_left(length, A[i])
    if tmp == len(length):
        length.append(A[i])
    else:
        length[tmp] = A[i]
print(len(length))
