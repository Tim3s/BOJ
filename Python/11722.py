import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = [1] * N
ans = 1
for i in range(N):
    for j in range(i):
        if A[i] < A[j] and B[j] + 1 > B[i]:
            B[i] = B[j] + 1
    if B[i] > ans:
        ans = B[i]
print(ans)
