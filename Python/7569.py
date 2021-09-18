import sys

M, N, H = map(int, sys.stdin.readline().split())
farm = [[list(map(int, sys.stdin.readline().split())) for i in range(N)] for j in range(H)]
res = 0
zero = 0
cur = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if farm[i][j][k] == 0:
                zero += 1
            elif farm[i][j][k] == 1:
                cur.append((i, j, k))
while True:
    if not zero:
        break
    if len(cur) == 0:
        res = -1
        break
    newcur = []
    for item in cur:
        height, row, col = item
        if height > 0 and not farm[height - 1][row][col]:
            farm[height - 1][row][col] = 1
            newcur.append((height - 1, row, col))
            zero -= 1
        if row > 0 and not farm[height][row - 1][col]:
            farm[height][row - 1][col] = 1
            newcur.append((height, row - 1, col))
            zero -= 1
        if col > 0 and not farm[height][row][col - 1]:
            farm[height][row][col - 1] = 1
            newcur.append((height, row, col - 1))
            zero -= 1
        if height < H - 1 and not farm[height + 1][row][col]:
            farm[height + 1][row][col] = 1
            newcur.append((height + 1, row, col))
            zero -= 1
        if row < N - 1 and not farm[height][row + 1][col]:
            farm[height][row + 1][col] = 1
            newcur.append((height, row + 1, col))
            zero -= 1
        if col < M - 1 and not farm[height][row][col + 1]:
            farm[height][row][col + 1] = 1
            newcur.append((height, row, col + 1))
            zero -= 1
    cur = newcur
    res += 1
print(res)
