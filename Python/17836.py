import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, finalx, finaly):
    q = deque([(x, y, 0, False)])
    visited = [[False] * M for _ in range(N)]
    nogramvisit = [[False] * M for _ in range(N)]
    visited[x][y] = True
    nogramvisit[x][y] = True
    while q:
        x, y, time, gram = q.popleft()
        time += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if nx == finalx and ny == finaly:
                    return time
                if gram or maze[nx][ny] == 2:
                    q.append((nx, ny, time, True))
                    visited[nx][ny] = True
                elif maze[nx][ny] == 0 and not nogramvisit[nx][ny]:
                    nogramvisit[nx][ny] = True
                    q.append((nx, ny, time, gram))
        if time > T:
            return 'Fail'
    return 'Fail'


N, M, T = map(int, sys.stdin.readline().split())
if N == M == 1:
    print(0)
    sys.exit(0)
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(bfs(0, 0, N - 1, M - 1))
