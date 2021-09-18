import sys


def newshark():
    shark = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if sharks[i][j]:
                s, d, z = sharks[i][j]
                x = i + dx[d] * s
                y = j + dy[d] * s
                while not (0 <= x < R):
                    if x < 0:
                        x = -x
                        d = 3 - d
                    if x >= R:
                        x = 2 * (R - 1) - x
                        d = 3 - d
                while not (0 <= y < C):
                    if y < 0:
                        y = -y
                        d = 7 - d
                    if y >= C:
                        y = 2 * (C - 1) - y
                        d = 7 - d
                if not shark[x][y] or shark[x][y][2] < z:
                    shark[x][y] = (s, d, z)
    return shark


R, C, M = map(int, sys.stdin.readline().split())
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
sharks = [[0] * C for _ in range(R)]
ans = 0
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    if d // 3:
        s %= 2 * (C - 1)
        if s >= C:
            s = 2 * (C - 1) - s
            d = 7 - d
    else:
        s %= 2 * (R - 1)
        if s >= R:
            s = 2 * (R - 1) - s
            d = 3 - d
    sharks[r - 1][c - 1] = (s, d, z)
for man in range(C):
    for i in range(R):
        if sharks[i][man]:
            ans += sharks[i][man][2]
            sharks[i][man] = 0
            break
    if man == C - 1:
        break
    sharks = newshark()
print(ans)
