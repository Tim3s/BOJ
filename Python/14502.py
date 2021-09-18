import sys
import copy
from itertools import combinations
from collections import deque

d = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs(newlab, visited, x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and newlab[nx][ny] % 2 == 0:
                visited[nx][ny] = True
                newlab[nx][ny] = 2
                q.append((nx, ny))


def findsafe(newlab, newwall):
    for x, y in newwall:
        newlab[x][y] = 1
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and newlab[i][j] == 2:
                bfs(newlab, visited, i, j)
    res = 0
    for i in range(N):
        res += newlab[i].count(0)
    return res


N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
empty = []
for i in range(N):
    for j in range(M):
        if not lab[i][j]:
            empty.append([i, j])
wall = list(combinations(empty, 3))
res = 0
for item in wall:
    res = max(res, findsafe(copy.deepcopy(lab), item))
print(res)
