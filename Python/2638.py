import sys
import copy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
newcheese = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cheese = 0
airmap = [[0] * M for _ in range(N)]
res = -1
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
idx = 1
for i in range(N):
    for j in range(M):
        if not airmap[i][j] and not newcheese[i][j]:
            q = deque([(i, j)])
            airmap[i][j] = idx
            while q:
                x, y = q.popleft()
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < M and not airmap[nx][ny] and not newcheese[nx][ny]:
                        q.append((nx, ny))
                        airmap[nx][ny] = idx
            idx += 1
while cheese != newcheese:
    res += 1
    nextoutset = set()
    cheese = copy.deepcopy(newcheese)
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if cheese[i][j] == 1:
                cnt = 0
                tmpoutset = []
                for dx, dy in d:
                    tmp = airmap[i + dx][j + dy]
                    if tmp:
                        tmpoutset.append(tmp)
                        if tmp == 1:
                            cnt += 1
                if cnt >= 2:
                    newcheese[i][j] = 0
                    nextoutset = nextoutset.union(set(tmpoutset))
    nextoutset.discard(1)
    for i in range(N):
        for j in range(M):
            if airmap[i][j] in nextoutset or (not airmap[i][j] and not newcheese[i][j]):
                airmap[i][j] = 1
print(res)
