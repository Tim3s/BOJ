import sys
import copy

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
newbus = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if not newbus[a - 1][b - 1]:
        newbus[a - 1][b - 1] = c
    else:
        newbus[a - 1][b - 1] = min(newbus[a - 1][b - 1], c)
bus = 0

while bus != newbus:
    bus = copy.deepcopy(newbus)
    for i in range(n):
        for j in range(n):
            if newbus[i][j]:
                for k in range(n):
                    if newbus[k][i]:
                        if not newbus[k][j]:
                            newbus[k][j] = newbus[k][i] + newbus[i][j]
                        else:
                            newbus[k][j] = min(newbus[k][j], newbus[k][i] + newbus[i][j])
                    if newbus[j][k]:
                        if not newbus[i][k]:
                            newbus[i][k] = newbus[i][j] + newbus[j][k]
                        else:
                            newbus[i][k] = min(newbus[i][k], newbus[i][j] + newbus[j][k])
for i in range(n):
    bus[i][i] = 0
    print(' '.join(list(map(str, bus[i]))))
