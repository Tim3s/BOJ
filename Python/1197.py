import heapq
import sys


class UnionFind:
    def __init__(self, x):
        self.__data = [-1 for i in range(x)]
        self.__size = [1 for i in range(x)]

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


V, E = map(int, sys.stdin.readline().split())
heap = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (C, A, B))
cnt = 0
uf = UnionFind(V + 1)
while True:
    while heap and uf.find(heap[0][1]) == uf.find(heap[0][2]):
        heapq.heappop(heap)
    if not heap:
        break
    C, A, B = heapq.heappop(heap)
    cnt += C
    uf.union(A, B)
print(cnt)
