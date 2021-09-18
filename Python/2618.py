import sys


def getdist(a, b):
    return abs(case[b][0] - case[a][0]) + abs(case[b][1] - case[a][1])


N = int(sys.stdin.readline())
W = int(sys.stdin.readline())
case = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(W)]
dp = [[2000000] * (W + 1) for _ in range(W + 1)]
back = [[[-1, -1] for _ in range(W + 1)] for _ in range(W + 1)]
dp[1][0] = case[1][0] + case[1][1] - 2
dp[0][1] = 2 * N - case[1][0] - case[1][1]
for i in range(2, W + 1):
    dp[i][0] = dp[i - 1][0] + getdist(i, i - 1)
    back[i][0] = [i - 1, 0]
    dp[0][i] = dp[0][i - 1] + getdist(i, i - 1)
    back[0][i] = [0, i - 1]
for i in range(1, W):
    dp[i][i + 1] = dp[i][0] + 2 * N - case[i + 1][0] - case[i + 1][1]
    back[i][i + 1] = [i, 0]
    dp[i + 1][i] = dp[0][i] + case[i + 1][0] + case[i + 1][1] - 2
    back[i + 1][i] = [0, i]
for i in range(1, W):
    for j in range(i + 1, W):
        jtoj = getdist(j, j + 1)
        itoj = getdist(i, j + 1)
        if dp[i][j + 1] > dp[i][j] + jtoj:
            dp[i][j + 1] = dp[i][j] + jtoj
            back[i][j + 1] = [i, j]
        if dp[j + 1][j] > dp[i][j] + itoj:
            dp[j + 1][j] = dp[i][j] + itoj
            back[j + 1][j] = [i, j]
        if dp[j + 1][i] > dp[j][i] + jtoj:
            dp[j + 1][i] = dp[j][i] + jtoj
            back[j + 1][i] = [j, i]
        if dp[j][j + 1] > dp[j][i] + itoj:
            dp[j][j + 1] = dp[j][i] + itoj
            back[j][j + 1] = [j, i]
res = [dp[W][i] for i in range(W)] + [dp[i][W] for i in range(W)]
ans = min(res)
print(ans)
idx = res.index(ans)
if idx >= W:
    x, y = idx - W, W
else:
    x, y = W, idx
police = []
while x != -1:
    if x > y:
        police.append('1')
    else:
        police.append('2')
    x, y = back[x][y]
print('\n'.join(reversed(police)))
