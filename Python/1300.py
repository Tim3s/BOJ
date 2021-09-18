import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())
left = 1
right = N * N + 1
ans = 1
while left < right:
    mid = (left + right) // 2
    tmp = 0
    for i in range(1, N + 1):
        tmp += min(N, mid // i)
    if tmp >= k:
        ans = mid
        right = mid
    else:
        left = mid + 1
print(ans)
