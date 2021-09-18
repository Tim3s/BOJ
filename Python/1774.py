import math
import sys
import heapq


class UnionFind:
    def __init__(self):
        self.__data = dict()
        self.__size = dict()

    def find(self, x, y):
        while self.__data[(x, y)] != -1:
            x, y = self.__data[(x, y)]
        return x, y

    def append(self, x, y):
        self.__data[(x, y)] = -1
        self.__size[(x, y)] = 1

    def union(self, x, y, nx, ny):
        a = self.find(x, y)
        b = self.find(nx, ny)
        if a == b:
            return
        if self.__size[a] < self.__size[b]:
            self.__size[b] += self.__size[a]
            self.__data[a] = b
        else:
            self.__size[a] += self.__size[b]
            self.__data[b] = a


N, M = map(int, sys.stdin.readline().split())
god = []
heap = []
uf = UnionFind()
for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    for nx, ny in god:
        heapq.heappush(heap, [math.sqrt((nx - x) ** 2 + (ny - y) ** 2), x, y, nx, ny])
    god.append([x, y])
    uf.append(x, y)
ans = 0.0
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    x, y = god[a - 1]
    nx, ny = god[b - 1]
    uf.union(x, y, nx, ny)
while True:
    while heap and uf.find(heap[0][1], heap[0][2]) == uf.find(heap[0][3], heap[0][4]):
        heapq.heappop(heap)
    if not heap:
        break
    dist, x, y, nx, ny = heapq.heappop(heap)
    ans += dist
    uf.union(x, y, nx, ny)
print(format(ans, '.2f'))
