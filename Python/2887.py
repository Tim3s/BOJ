import sys
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


N = int(sys.stdin.readline())
god = []
heap = []
uf = UnionFind(N)
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    god.append([x, y, z, i])
for i in range(3):
    god.sort(key=lambda x: x[i])
    for j in range(N - 1):
        heapq.heappush(heap, (abs(god[j][i] - god[j + 1][i]), god[j][3], god[j + 1][3]))
ans = 0
while True:
    while heap and uf.find(heap[0][1]) == uf.find(heap[0][2]):
        heapq.heappop(heap)
    if not heap:
        break
    dist, i, j = heapq.heappop(heap)
    ans += dist
    uf.union(i, j)
print(ans)
