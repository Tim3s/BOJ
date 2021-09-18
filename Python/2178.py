import sys
from collections import deque


def bfs():
    d = deque()
    d.append((0, 0, 1))
    visited = [[False] * M for i in range(N)]
    visited[0][0] = True
    row = N - 1
    col = M - 1
    while True:
        x, y, distance = d.popleft()
        distance += 1
        if (x + 1 == row and y == col) or (x == row and y + 1 == col):
            return distance
        if x > 0 and maze[x - 1][y] and not visited[x - 1][y]:
            visited[x - 1][y] = True
            d.append((x - 1, y, distance))
        if y > 0 and maze[x][y - 1] and not visited[x][y - 1]:
            visited[x][y - 1] = True
            d.append((x, y - 1, distance))
        if x < row and maze[x + 1][y] and not visited[x + 1][y]:
            visited[x + 1][y] = True
            d.append((x + 1, y, distance))
        if y < col and maze[x][y + 1] and not visited[x][y + 1]:
            visited[x][y + 1] = True
            d.append((x, y + 1, distance))


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(N)]
print(bfs())
