import sys

n, k = map(int, sys.stdin.readline().split())
ans = [0] * (k + 1)
ans[0] = 1
for _ in range(n):
    coin = int(sys.stdin.readline())
    for i in range(k):
        if coin + i <= k:
            ans[coin + i] += ans[i]
            continue
        break
print(ans[k])
