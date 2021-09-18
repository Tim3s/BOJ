import sys

N, C = map(int, sys.stdin.readline().split())
home = sorted([int(sys.stdin.readline()) for _ in range(N)])
left = 1
right = home[-1] - home[0] + 1
res = 0
while left < right:
    mid = (left + right) // 2
    cur = home[0]
    cnt = 1
    for i in range(1, N):
        if home[i] - cur >= mid:
            cnt += 1
            cur = home[i]
    if cnt >= C:
        res = mid
        left = mid + 1
    else:
        right = mid
print(res)
