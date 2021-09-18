import sys
import heapq


class Node:
    def __init__(self):
        self.v = None
        self.w = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.__header = None

    def append(self, x, length):
        tmpNode = Node()
        tmpNode.w = length
        tmpNode.v = x
        tmpNode.next = self.__header
        self.__header = tmpNode

    def header(self):
        return self.__header


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus = [LinkedList() for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a].append(b, c)
S, E = map(int, sys.stdin.readline().split())
visited = [False] * (N + 1)
heap = [(1, S)]
while True:
    while visited[heap[0][1]]:
        heapq.heappop(heap)
    w, v = heapq.heappop(heap)
    if v == E:
        print(w - 1)
        sys.exit(0)
    visited[v] = True
    cur = bus[v].header()
    while cur:
        if not visited[cur.v]:
            heapq.heappush(heap, (w + cur.w, cur.v))
        cur = cur.nextcave
