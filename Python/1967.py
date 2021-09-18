import sys
from collections import deque


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


def bfs(start):
    visit = [-1] * (V + 1)
    visit[start] = 0
    que = deque()
    que.append(start)
    mymax = [0, 0]
    while que:
        t = que.popleft()
        cur = tree[t].header()
        while cur:
            e = cur.v
            w = cur.w
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if mymax[0] < visit[e]:
                    mymax = visit[e], e
            cur = cur.nextcave
    return mymax


V = int(sys.stdin.readline())
tree = [LinkedList() for _ in range(V + 1)]
for _ in range(V - 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    tree[tmp[0]].append(tmp[1], tmp[2])
    tree[tmp[1]].append(tmp[0], tmp[2])
print(bfs(bfs(1)[1])[0])
