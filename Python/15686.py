import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chickencnt = 0
homecnt = 0
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
            homecnt += 1
        elif city[i][j] == 2:
            chicken.append((i, j))
            chickencnt += 1
length = []
for x, y in chicken:
    tmp = []
    for i in range(homecnt):
        tmp.append(abs(x - home[i][0]) + abs(y - home[i][1]))
    length.append(tmp)
res = 50000
for selected in list(combinations(list(range(chickencnt)), M)):
    res = min(res, sum([min([length[selected[j]][i] for j in range(M)]) for i in range(homecnt)]))
print(res)
