import sys
from collections import deque
import heapq


class UnionFind:
    def __init__(self, x):
        self.__data = [-1 for _ in range(x)]
        self.__size = [1 for _ in range(x)]

    def find(self, index):
        while self.__data[index] != -1:
            index = self.__data[index]
        return index

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.__size[x] < self.__size[y]:
            self.__size[y] += self.__size[x]
            self.__data[x] = y
        else:
            self.__size[x] += self.__size[y]
            self.__data[y] = x

    def size(self, x):
        return self.__size[self.find(x)]


def bfs(x, y):
    global idx
    idx += 1
    isle[x][y] = idx
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < N and 0 <= ny < M and island[nx][ny] and not isle[nx][ny]:
                q.append((nx, ny))
                isle[nx][ny] = idx


N, M = map(int, sys.stdin.readline().split())
island = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
idx = 0
isle = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if island[i][j] and not isle[i][j]:
            bfs(i, j)
del island
heap = []
for i in range(N):
    for j in range(M):
        if isle[i][j]:
            for k in range(i + 1, N):
                if isle[k][j]:
                    if k - i <= 2 or isle[k][j] == isle[i][j]:
                        break
                    heapq.heappush(heap, (k - i - 1, isle[i][j] - 1, isle[k][j] - 1))
                    break
            for k in range(j + 1, M):
                if isle[i][k]:
                    if k - j <= 2 or isle[i][j] == isle[i][k]:
                        break
                    heapq.heappush(heap, (k - j - 1, isle[i][j] - 1, isle[i][k] - 1))
                    break
uf = UnionFind(idx)
cnt = 1
ans = 0
while True:
    while heap and uf.find(heap[0][1]) == uf.find(heap[0][2]):
        heapq.heappop(heap)
    if not heap:
        break
    cnt += 1
    length, a, b = heapq.heappop(heap)
    ans += length
    uf.union(a, b)
print(ans if cnt == idx else -1)
