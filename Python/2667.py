import sys
from collections import deque


def bfs(x, y):
    d = deque()
    d.append((x, y))
    visited[x][y] = True
    res = 1
    while d:
        x, y = d.popleft()
        if x > 0 and apt[x - 1][y] and not visited[x - 1][y]:
            visited[x - 1][y] = True
            res += 1
            d.append((x - 1, y))
        if y > 0 and apt[x][y - 1] and not visited[x][y - 1]:
            visited[x][y - 1] = True
            res += 1
            d.append((x, y - 1))
        if x < N - 1 and apt[x + 1][y] and not visited[x + 1][y]:
            visited[x + 1][y] = True
            res += 1
            d.append((x + 1, y))
        if y < N - 1 and apt[x][y + 1] and not visited[x][y + 1]:
            visited[x][y + 1] = True
            res += 1
            d.append((x, y + 1))
    return res


N = int(sys.stdin.readline())
apt = [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(N)]
visited = [[False] * N for i in range(N)]
num = []
for i in range(N):
    for j in range(N):
        if apt[i][j] and not visited[i][j]:
            num.append(bfs(i, j))
print(len(num))
print('\n'.join([str(i) for i in sorted(num)]))
