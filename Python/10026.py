import sys
from collections import deque


def bfs(x, y, col):
    visited[x][y] = True
    q = deque([(x, y)])
    if col == 'R':
        color[x][y] = 'G'
    while q:
        x, y = q.popleft()
        if x > 0 and color[x - 1][y] == col and not visited[x - 1][y]:
            if col == 'R':
                color[x - 1][y] = 'G'
            visited[x - 1][y] = True
            q.append((x - 1, y))
        if y > 0 and color[x][y - 1] == col and not visited[x][y - 1]:
            if col == 'R':
                color[x][y - 1] = 'G'
            visited[x][y - 1] = True
            q.append((x, y - 1))
        if x < N - 1 and color[x + 1][y] == col and not visited[x + 1][y]:
            if col == 'R':
                color[x + 1][y] = 'G'
            visited[x + 1][y] = True
            q.append((x + 1, y))
        if y < N - 1 and color[x][y + 1] == col and not visited[x][y + 1]:
            if col == 'R':
                color[x][y + 1] = 'G'
            visited[x][y + 1] = True
            q.append((x, y + 1))


N = int(sys.stdin.readline())
color = [list(sys.stdin.readline().rstrip()) for i in range(N)]
visited = [[False] * N for i in range(N)]
res = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, color[i][j])
            res += 1
print(res)
visited = [[False] * N for i in range(N)]
res = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, color[i][j])
            res += 1
print(res)
