import sys
import math


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

    def count(self):
        cnt = 0
        for _i in self.__data:
            if _i == -1:
                cnt += 1
        return cnt


def near(pos1, pos2):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 <= (pos1[2] + pos2[2]) ** 2


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    territory = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    uf = UnionFind(N)
    for i in range(N):
        for j in range(i + 1, N):
            if uf.find(i) != uf.find(j) and near(territory[i], territory[j]):
                uf.union(i, j)
    print(uf.count())
