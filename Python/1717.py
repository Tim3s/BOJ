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


n, m = map(int, sys.stdin.readline().split())
uf = UnionFind(n + 1)
for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        uf.union(a, b)
        continue
    print('YES' if uf.find(a) == uf.find(b) else 'NO')
