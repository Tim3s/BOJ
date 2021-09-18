import sys
from collections import deque


def bfs(x, y, size):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[False] * N for i in range(N)]
    visited[x][y] = True
    q = deque([(x, y, 0)])
    done = False
    toReturn = []
    mintime = 0
    while q:
        x, y, time = q.popleft()
        if done and time == mintime:
            return sorted(toReturn)[0]
        time += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and water[nx][ny] <= size:
                if 0 < water[nx][ny] < size:
                    if not done:
                        done = True
                        mintime = time
                    toReturn.append((nx, ny, time))
                visited[nx][ny] = True
                q.append((nx, ny, time))
    if done and time > mintime:
        return sorted(toReturn)[0]
    return


N = int(sys.stdin.readline())
water = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
done = False
for i in range(N):
    for j in range(N):
        if water[i][j] == 9:
            done = True
            shark = [i, j]
            break
    if done:
        break
res = 0
sharksize = 2
eaten = 0
while True:
    water[shark[0]][shark[1]] = 0
    shark = bfs(shark[0], shark[1], sharksize)
    if shark is None:
        break
    eaten += 1
    if eaten == sharksize:
        sharksize += 1
        eaten = 0
    res += shark[2]
print(res)
