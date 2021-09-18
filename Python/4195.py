import sys


class UnionFind:
    def __init__(self):
        self.__data = dict()
        self.__size = dict()

    def find(self, index):
        if index not in self.__data:
            self.append(index)
            return index
        while self.__data[index] != -1:
            index = self.__data[index]
        return index

    def append(self, x):
        self.__data[x] = -1
        self.__size[x] = 1

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


T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    uf = UnionFind()
    for _ in range(F):
        a, b = sys.stdin.readline().split()
        uf.union(a, b)
        print(uf.size(a))
