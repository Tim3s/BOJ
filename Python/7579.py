import sys

N, M = map(int, sys.stdin.readline().split())
active = list(map(int, sys.stdin.readline().split()))
shutdown = list(map(int, sys.stdin.readline().split()))
cost = [2147483647] * (M + 1)
cost[0] = 0
for i in range(N):
    for j in range(M, -1, -1):
        cur = min(M, active[i] + j)
        cost[cur] = min(cost[cur], cost[j] + shutdown[i])
        continue
print(cost[M])
