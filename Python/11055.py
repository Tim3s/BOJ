import sys
import copy

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = copy.deepcopy(A)
ans = 0
for i in range(N):
    for j in range(i):
        if A[j] < A[i] and B[j] + A[i] > B[i]:
            B[i] = B[j] + A[i]
    if B[i] > ans:
        ans = B[i]
print(ans)
