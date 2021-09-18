import sys
import heapq


n, m, r = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))
edge = [[10000] * n for i in range(n)]
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    a, b = a - 1, b - 1
    edge[a][b] = edge[b][a] = l
for check in range(n):
    for i in range(n):
        for j in range(n):
            if i != check and j != check and i != j:
                edge[i][j] = min(edge[i][j], edge[i][check] + edge[check][j])
res = 0
for i in range(n):
    edge[i][i] = 0
    tmp = 0
    for j in range(n):
        tmp += t[j] if edge[i][j] <= m else 0
    res = max(tmp, res)
print(res)
