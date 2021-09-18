import sys
from collections import deque

N = int(sys.stdin.readline())
parts = [0] * (N + 1)
parts[N] = 1
M = int(sys.stdin.readline())
low = [[] for _ in range(N + 1)]
high = [[] for _ in range(N + 1)]
for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    low[X].append([Y, K])
    high[Y].append(X)
q = deque()
q.append(N)
base = []
for i in range(1, N + 1):
    if not low[i]:
        base.append(i)
while q:
    X = q.popleft()
    for Y, K in low[X]:
        high[Y].remove(X)
        parts[Y] += parts[X] * K
        if not high[Y]:
            q.append(Y)
for i in base:
    print(i, parts[i])
