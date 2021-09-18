import sys

N = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
newhouse = [[[0] * 3 for _ in range(N)] for _ in range(N)]
newhouse[0][1][-1] = 1
for i in range(N):
    for j in range(1, N):
        down = i < N - 1 and not house[i + 1][j]
        right = j < N - 1 and not house[i][j + 1]
        if down:
            newhouse[i + 1][j][1] = newhouse[i][j][0] + newhouse[i][j][1]
        if right:
            newhouse[i][j + 1][-1] = newhouse[i][j][0] + newhouse[i][j][-1]
        if down and right and not house[i + 1][j + 1]:
            newhouse[i + 1][j + 1][0] = sum(newhouse[i][j])
print(sum(newhouse[N - 1][N - 1]))
