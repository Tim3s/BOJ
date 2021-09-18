import sys
from collections import deque


class Node:
    def __init__(self):
        self.vertex = None
        self.weight = None
        self.next = None


class LinkedList:
    def __init__(self, a=None):
        self.__header = None
        if a:
            self.__header = Node()
            self.__header.vertex = a[0]
            self.__header.weight = a[1]
            _cur = self.__header
            for i in range(2, len(a), 2):
                _cur.next = Node()
                _cur = _cur.next
                _cur.vertex = a[i]
                _cur.weight = a[i + 1]

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
tree = [0] * (V + 1)
for i in range(V):
    tmp = list(map(int, sys.stdin.readline().split()))
    tree[tmp[0]] = LinkedList(tmp[1:-1])
print(bfs(bfs(1)[1])[0])
# for i in range(1, V + 1):
#     tmp = tree[i].header()
#     while tmp:
#         print(tmp.vertex, tmp.weight, end=' ')
#         tmp = tmp.next
#     print()
