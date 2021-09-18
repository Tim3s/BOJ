import sys


def dp(i):
    if i == K:
        print('GOOD')
        sys.exit(0)
    for j in range(len(time)):
        if time[j] >= T[i]:
            time[j] -= T[i]
            dp(i + 1)
            time[j] += T[i]


N, K = map(int, sys.stdin.readline().split())
cur = 0
time = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    if cur != s:
        time.append(s - cur)
    cur = e
if cur != 1440:
    time.append(1440 - cur)
T = list(map(int, sys.stdin.readline().split()))
T.sort(reverse=True)
dp(0)
print('BAD')
