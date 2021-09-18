import sys
from collections import deque


class Node:
    def __init__(self):
        self.v = None
        self.w = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.__header = None

    def append(self, x, l):
        tmpNode = Node()
        tmpNode.w = l
        tmpNode.v = x
        tmpNode.next = self.__header
        self.__header = tmpNode

    def header(self):
        return self.__header


def bfs(start):
    visit = [-1] * (N + 1)
    visit[start] = 0
    q = deque()
    q.append(start)
    mymax = [0, start]
    while q:
        t = q.popleft()
        cur = tree[t].header()
        while cur:
            if visit[cur.v] == -1:
                visit[cur.v] = visit[t] + cur.w
                q.append(cur.v)
                if mymax[0] < visit[cur.v]:
                    mymax = [visit[cur.v], cur.v]
            cur = cur.next
    return mymax


N, S = map(int, sys.stdin.readline().split())
tree = [LinkedList() for _ in range(N + 1)]
edgesum = 0
for i in range(N - 1):
    A, B, C = list(map(int, sys.stdin.readline().split()))
    tree[A].append(B, C)
    tree[B].append(A, C)
    edgesum += C
print(edgesum * 2 - bfs(bfs(1)[1])[0])
