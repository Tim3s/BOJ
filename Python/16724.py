import sys


def bfs(x, y):
    global idx
    idx += 1
    while not visited[x][y]:
        visited[x][y] = True
        move = world[x][y]
        world[x][y] = idx
        if move == 'D':
            x += 1
        elif move == 'U':
            x -= 1
        elif move == 'L':
            y -= 1
        else:
            y += 1
    if world[x][y] == idx:
        return 1
    return 0


N, M = map(int, sys.stdin.readline().split())
world = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
cnt = 0
idx = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += bfs(i, j)
print(cnt)
