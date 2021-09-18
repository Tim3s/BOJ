import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, finalx, finaly):
    if N == M == 1:
        return 1
    q = deque([(x, y, 1, True, 0)])
    broke = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
    broke[x][y][0] = True
    while q:
        x, y, time, night, curbroke = q.popleft()
        night = not night
        if x == finalx and y == finaly:
            return time
        time += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not broke[nx][ny][0]:
                if not maze[nx][ny]:
                    if not broke[nx][ny][curbroke]:
                        broke[nx][ny][curbroke] = True
                        q.append((nx, ny, time, night, curbroke))
                elif curbroke < K and not broke[nx][ny][curbroke]:
                    if night:
                        q.append((x, y, time, night, curbroke))
                    else:
                        broke[nx][ny][curbroke] = True
                        q.append((nx, ny, time, night, curbroke + 1))
    return -1


N, M, K = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
print(bfs(0, 0, N - 1, M - 1))
