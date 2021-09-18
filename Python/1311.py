import sys
from collections import deque


N = int(sys.stdin.readline())
D = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[sys.maxsize] * (1 << N) for _ in range(N)]
q = deque()
last = [[sys.maxsize] * (1 << N) for _ in range(N)]
for i in range(N):
    dp[0][2 ** i] = D[0][i]
    q.append((0, 2 ** i))
while q:
    i, j = q.popleft()
    if last[i][j] == dp[i][j]:
        continue
    last[i][j] = dp[i][j]
    if i != N - 1:
        for k in range(N):
            if not (j & (1 << k)):
                dp[i + 1][j + (1 << k)] = min(dp[i + 1][j + (1 << k)], dp[i][j] + D[i + 1][k])
                q.append((i + 1, j + (1 << k)))
print(dp[-1][-1])
