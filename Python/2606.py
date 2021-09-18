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


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
net = UnionFind(N + 1)
for i in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    net.union(a, b)
print(net.size(1) - 1)
