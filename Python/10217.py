import sys


class Node:
    def __init__(self, v=None, c = None, d=None):
        self.v = v
        self.d = d
        self.c = c
        self.next = None


class LinkedList:
    def __init__(self):
        self.__header = None

    def append(self, x, c, l):
        tmpNode = Node(x, c, l)
        tmpNode.next = self.__header
        self.__header = tmpNode

    def header(self):
        return self.__header


T = int(sys.stdin.readline())
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    ans = [[2147483647] * (M + 1) for _ in range(N + 1)]
    plane = [LinkedList() for _ in range(N + 1)]
    ans[1][0] = 0
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        plane[u].append(v, c, d)
    for j in range(M + 1):
        for i in range(1, N + 1):
            if ans[i][j] != 2147483647:
                cur = plane[i].header()
                while cur:
                    if cur.c + j <= M:
                        ans[cur.v][cur.c + j] = min(ans[cur.v][cur.c + j], ans[i][j] + cur.d)
                    cur = cur.next
    ans = min(ans[N])
    print(ans if ans != 2147483647 else "Poor KCM")
