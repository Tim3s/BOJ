import sys

M, N = list(map(int, sys.stdin.readline().split()))
farm = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
res = 0
zero = 0
cur = []
for i in range(N):
    for j in range(M):
        if farm[i][j] == 0:
            zero += 1
        elif farm[i][j] == 1:
            cur.append([i, j])
while True:
    if not zero:
        break
    if len(cur) == 0:
        res = -1
        break
    newcur = []
    for item in cur:
        row, col = item
        if row > 0 and not farm[row - 1][col]:
            farm[row - 1][col] = 1
            newcur.append([row - 1, col])
            zero -= 1
        if col > 0 and not farm[row][col - 1]:
            farm[row][col - 1] = 1
            newcur.append([row, col - 1])
            zero -= 1
        if row < N - 1 and not farm[row + 1][col]:
            farm[row + 1][col] = 1
            newcur.append([row + 1, col])
            zero -= 1
        if col < M - 1 and not farm[row][col + 1]:
            farm[row][col + 1] = 1
            newcur.append([row, col + 1])
            zero -= 1
    cur = newcur
    res += 1
print(res)
