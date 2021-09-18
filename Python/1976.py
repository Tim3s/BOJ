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
uf = UnionFind(N + 1)
for i in range(1, N + 1):
    num = [0] + list(map(int, sys.stdin.readline().split()))
    for j in range(1, N + 1):
        if num[j] == 1:
            uf.union(i, j)
num = list(map(int, sys.stdin.readline().split()))
possible = True
for i in range(M - 1):
    if uf.find(num[i]) != uf.find(num[i - 1]):
        possible = False
        break
print('YES' if possible else 'NO')
