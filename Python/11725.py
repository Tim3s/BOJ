import sys
from collections import deque


class Node:
    def __init__(self):
        self.vertex = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.__header = None

    def append(self, x):
        tmpNode = Node()
        tmpNode.vertex = x
        tmpNode.next = self.__header
        self.__header = tmpNode

    def header(self):
        return self.__header


N = int(sys.stdin.readline())
edge = [LinkedList() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)
parent = [0] * (N + 1)
q = deque([1])
while q:
    v = q.popleft()
    cur = edge[v].header()
    while cur:
        if not parent[cur.v]:
            parent[cur.v] = v
            q.append(cur.v)
        cur = cur.nextcave
for i in range(2, N + 1):
    print(parent[i])
