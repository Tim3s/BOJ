import sys

V, E = map(int, sys.stdin.readline().split())
dist = [[2147483647] * V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    dist[a - 1][b - 1] = c
for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = min([dist[i][i] for i in range(V)])
print(ans if ans != 2147483647 else -1)
