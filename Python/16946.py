import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, num):
    newmaze[x][y] = num
    q = deque([(x, y)])
    res = 1
    while q:
        curx, cury = q.popleft()
        for _i in range(4):
            nx = curx + dx[_i]
            ny = cury + dy[_i]
            if 0 <= nx < N and 0 <= ny < M and not maze[nx][ny] and not newmaze[nx][ny]:
                res = (res + 1) % 10
                q.append((nx, ny))
                newmaze[nx][ny] = num
    mapdict[num] = res


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
newmaze = [[0] * M for _ in range(N)]
mapdict = dict()
mapdict[0] = 0
idx = 1
for i in range(N):
    for j in range(M):
        if not maze[i][j] and not newmaze[i][j]:
            bfs(i, j, idx)
            idx += 1
for i in range(N):
    for j in range(M):
        if maze[i][j]:
            tmpset = set()
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < M:
                    tmpset.add(newmaze[ni][nj])
            for group in tmpset:
                maze[i][j] += mapdict[group]
            maze[i][j] %= 10
for i in range(N):
    print(''.join([str(i) for i in maze[i]]))
