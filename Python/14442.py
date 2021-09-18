import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, finalx, finaly):
    if N == M == 1:
        return 1
    q = deque([(x, y, 1)])
    visited = [[2000] * M for _ in range(N)]
    visited[0][0] = 0
    while q:
        x, y, time = q.popleft()
        time += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if nx == finalx and ny == finaly:
                    return time
                newbroke = maze[nx][ny] + visited[x][y]
                if newbroke < visited[nx][ny] and newbroke <= K:
                    visited[nx][ny] = newbroke
                    q.append((nx, ny, time))
    return -1


N, M, K = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
print(bfs(0, 0, N - 1, M - 1))
