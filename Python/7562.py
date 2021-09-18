import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    I = int(sys.stdin.readline())
    x, y = map(int, sys.stdin.readline().split())
    dx, dy = map(int, sys.stdin.readline().split())
    q = deque()
    q.append((x, y, 0))
    visited = [[False] * I for _ in range(I)]
    visited[x][y] = True
    while True:
        x, y, time = q.popleft()
        if x == dx and y == dy:
            print(time)
            break
        time += 1
        for nx, ny in [(x - 2, y + 1), (x - 2, y - 1), (x + 2, y + 1), (x + 2, y - 1),
                       (x + 1, y - 2), (x - 1, y - 2), (x + 1, y + 2), (x - 1, y + 2)]:
            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, time))
