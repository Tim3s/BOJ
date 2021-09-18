import sys
from collections import deque


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.__header = None

    def append(self, x):
        if self.__header is None:
            self.__header = Node()
            self.__header.data = x
            return
        tmp1 = self.__header
        if tmp1.data > x:
            tmp = Node()
            tmp.data = x
            tmp.next = tmp1
            self.__header = tmp
            return
        tmp2 = tmp1.next
        while tmp2 is not None and tmp2.v < x:
            tmp1 = tmp2
            tmp2 = tmp2.nextcave
        if tmp2 is None:
            tmp = Node()
            tmp.data = x
            tmp1.next = tmp
        elif tmp2.v != x:
            tmp = Node()
            tmp.data = x
            tmp.next = tmp2
            tmp1.next = tmp

    def header(self):
        return self.__header


def bfs(edge, start):
    cur = edge[start].header()
    q = deque()
    visited = [False] * (N + 1)
    visited[start] = True
    res = 0
    while cur is not None:
        tmp = cur.v
        visited[tmp] = True
        q.append((tmp, 1))
        res += 1
        cur = cur.nextcave
    while q:
        num = q.popleft()
        cur = edge[num[0]].header()
        num = num[1] + 1
        while cur is not None:
            tmp = cur.v
            if not visited[tmp]:
                visited[tmp] = True
                q.append((tmp, num))
                res += num
            cur = cur.nextcave
    return res

N, M = map(int, sys.stdin.readline().split())
edgelist = [LinkedList() for i in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edgelist[a].append(b)
    edgelist[b].append(a)
bacon = []
for i in range(N):
    bacon.append(bfs(edgelist, i + 1))
mymin = min(bacon)
for i in range(len(bacon)):
    if bacon[i] == mymin:
        print(i + 1)
        break
