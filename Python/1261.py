import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, finalx, finaly):
    q = deque([(x, y)])
    visited = [[200] * M for _ in range(N)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                newbroke = maze[nx][ny] + visited[x][y]
                if newbroke < visited[nx][ny]:
                    visited[nx][ny] = newbroke
                    q.append((nx, ny))
    return visited[finalx][finaly]


M, N = map(int, sys.stdin.readline().split())
if N == M == 1:
    print(0)
    sys.exit(0)
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
print(bfs(0, 0, N - 1, M - 1))
