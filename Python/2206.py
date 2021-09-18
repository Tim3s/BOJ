import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque([(0, 0, 1, False)])
    visited = [[False] * M for _ in range(N)]
    locbroke = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    while q:
        x, y, time, broke = q.popleft()
        time += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if nx == N - 1 and ny == M - 1:
                    return time
                if maze[nx][ny] == 0 and not locbroke[nx][ny][int(broke)]:
                    locbroke[nx][ny][int(broke)] = True
                    if locbroke[nx][ny][0]:
                        visited[nx][ny] = True
                    q.append((nx, ny, time, broke))
                elif maze[nx][ny] == 1 and not broke:
                    q.append((nx, ny, time, True))
                    visited[nx][ny] = True
    return -1


N, M = map(int, sys.stdin.readline().split())
if N == M == 1:
    print(1)
    sys.exit(0)
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
print(bfs())
