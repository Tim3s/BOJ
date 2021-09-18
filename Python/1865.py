import sys
import copy


class Node:
    def __init__(self):
        self.vertex = None
        self.weight = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.__header = None

    def append(self, x, length):
        tmpNode = Node()
        tmpNode.weight = length
        tmpNode.vertex = x
        tmpNode.next = self.__header
        self.__header = tmpNode

    def header(self):
        return self.__header


TC = int(sys.stdin.readline())
for i in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    Vlist = [LinkedList() for i in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        Vlist[S].append(E, T)
        Vlist[E].append(S, T)
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        Vlist[S].append(E, -T)
    distance = [1000000000] * (N + 1)
    distance[1] = 0
    for _ in range(M + W):
        newdis = copy.deepcopy(distance)
        for v in range(1, N + 1):
            cur = Vlist[v].header()
            while cur is not None:
                distance[cur.v] = min(distance[cur.v], distance[v] + cur.w)
                cur = cur.nextcave
    print('YES' if newdis != distance else 'NO')
