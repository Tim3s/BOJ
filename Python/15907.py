import sys

ans = 2
N = int(sys.stdin.readline())
if N <= 2:
    print(N)
    sys.exit(0)
time = list(map(int, sys.stdin.readline().split()))
prime = [True] * time[-1]
cur = [0] * 2
for i in range(N):
    cur[time[i] % 2] += 1
ans = max(ans, max(cur))
length = time[-1] - time[0]
for i in range(3, time[-1], 2):
    if prime[i]:
        if 1 + length // i <= ans:
            break
        cur = [0] * i
        for j in time:
            cur[j % i] += 1
        ans = max(ans, max(cur))
        for j in range(i * i, len(prime), 2 * i):
            prime[j] = False
print(ans)
