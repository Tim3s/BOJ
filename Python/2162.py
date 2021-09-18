import sys


class UnionFind:
    def __init__(self, x):
        self.__data = [-1 for _ in range(x)]
        self.__size = [1 for _ in range(x)]
        self.__group = x
        self.__maxsize = 1

    def find(self, index):
        while self.__data[index] != -1:
            index = self.__data[index]
        return index

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.__group -= 1
        if self.__size[x] < self.__size[y]:
            self.__size[y] += self.__size[x]
            self.__data[x] = y
            self.__maxsize = max(self.__maxsize, self.__size[y])
        else:
            self.__size[x] += self.__size[y]
            self.__data[y] = x
            self.__maxsize = max(self.__maxsize, self.__size[x])

    def size(self, x):
        return self.__size[self.find(x)]

    def group(self):
        return self.__group

    def maxsize(self):
        return self.__maxsize


def ccw(a, b, c):
    return a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1])


def crossing(A, B, C, D):
    c1 = ccw(A, B, C)
    c2 = ccw(A, B, D)
    c3 = ccw(C, D, A)
    c4 = ccw(C, D, B)
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D
    if c1 * c2 == c3 * c4 == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and \
                min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return 1
        else:
            return 0
    c1 *= c2
    c3 *= c4
    return int(c1 <= 0 and c3 <= 0)


N = int(sys.stdin.readline())
num = []
for i in range(N):
    num.append(list(map(int, sys.stdin.readline().split())))
uf = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        if i != j and uf.find(i) != uf.find(j) and crossing(num[i][:2], num[i][2:], num[j][:2], num[j][2:]):
            uf.union(i, j)
print(uf.group())
print(uf.maxsize())
