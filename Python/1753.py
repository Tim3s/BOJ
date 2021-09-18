import sys
import heapq


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


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
Vlist = [LinkedList() for i in range(V + 1)]
for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    Vlist[a].append(b, w)
distance = [1000000] * (V + 1)
visited = [False] * (V + 1)
heap = [(0, K)]
while True:
    while heap and visited[heap[0][1]]:
        heapq.heappop(heap)
    if not heap:
        break
    dis, v = heapq.heappop(heap)
    visited[v] = True
    distance[v] = dis
    cur = Vlist[v].header()
    while cur:
        heapq.heappush(heap, (dis + cur.w, cur.v))
        cur = cur.nextcave
for i in range(1, V + 1):
    if distance[i] == 1000000:
        print('INF')
    else:
        print(distance[i])
