import sys
import copy

R, C, T = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
cleaner = []
for i in range(2, R - 2):
    if room[i][0] == -1:
        cleaner.append(i)
for _ in range(T):
    newroom = [[0] * C for _ in range(R)]
    newroom[cleaner[0]][0] = -1
    newroom[cleaner[1]][0] = -1
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                newroom[i][j] += room[i][j]
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < R and 0 <= y < C and not (y == 0 and x in cleaner):
                        newroom[x][y] += room[i][j] // 5
                        newroom[i][j] -= room[i][j] // 5
    for i in range(cleaner[0] - 2, -1, -1):
        newroom[i + 1][0] = newroom[i][0]
    for i in range(cleaner[1] + 2, R):
        newroom[i - 1][0] = newroom[i][0]
    for i in range(1, C):
        newroom[0][i - 1] = newroom[0][i]
        newroom[R - 1][i - 1] = newroom[R - 1][i]
    for i in range(1, cleaner[0] + 1):
        newroom[i - 1][C - 1] = newroom[i][C - 1]
    for i in range(R - 1, cleaner[1], -1):
        newroom[i][C - 1] = newroom[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        newroom[cleaner[0]][i] = newroom[cleaner[0]][i - 1]
        newroom[cleaner[1]][i] = newroom[cleaner[1]][i - 1]
    newroom[cleaner[0]][1] = newroom[cleaner[1]][1] = 0
    room = copy.deepcopy(newroom)
print(sum([sum(room[i]) for i in range(R)]) + 2)
