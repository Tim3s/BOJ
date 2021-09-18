import sys


def check(row, col, s):
    for i in range(row, row + s):
        for j in range(col, col + s):
            if tile[i][j]:
                return False
    return True


def dfs(row, col, s):
    global idx
    s //= 2
    if check(row, col, s):
        tile[row + s - 1][col + s - 1] = idx
    if check(row, col + s, s):
        tile[row + s - 1][col + s] = idx
    if check(row + s, col, s):
        tile[row + s][col + s - 1] = idx
    if check(row + s, col + s, s):
        tile[row + s][col + s] = idx
    idx += 1
    if s == 1:
        return
    dfs(row, col, s)
    dfs(row + s, col, s)
    dfs(row, col + s, s)
    dfs(row + s, col + s, s)


idx = 1
K = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())
x, y = 2 ** K - y, x - 1
tile = [[0] * (2 ** K) for _ in range(2 ** K)]
tile[x][y] = -1
dfs(0, 0, 2 ** K)
for i in range(2 ** K):
    print(' '.join(map(str, tile[i])))
