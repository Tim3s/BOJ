import sys
import heapq


class Node:
    def __init__(self):
        self.vertex = None
        self.length = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.__header = None

    def append(self, x, length):
        tmpNode = Node()
        tmpNode.length = length
        tmpNode.vertex = x
        tmpNode.next = self.__header
        self.__header = tmpNode

    def header(self):
        return self.__header


T = int(sys.stdin.readline())
for i in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    g, h = sorted([g, h])
    edgelist = [LinkedList() for j in range(n + 1)]
    for j in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        if a == g and b == h:
            edgelist[a].append(b, 2 * d - 1)
            edgelist[b].append(a, 2 * d - 1)
        else:
            edgelist[a].append(b, 2 * d)
            edgelist[b].append(a, 2 * d)
    destination = []
    for j in range(t):
        destination.append(int(sys.stdin.readline()))
    visited = [False] * (n + 1)
    distance = [10000000] * (n + 1)
    heap = [(0, s)]
    while True:
        while heap and visited[heap[0][1]]:
            heapq.heappop(heap)
        if not heap:
            break
        dis, s = heapq.heappop(heap)
        visited[s] = True
        distance[s] = dis
        cur = edgelist[s].header()
        while cur is not None:
            heapq.heappush(heap, (dis + cur.w, cur.v))
            cur = cur.nextcave
    final = []
    val = []
    for j in range(t):
        val.append(distance[destination[j]])
    for j in range(t):
        if val[j] % 2 == 1:
            final.append(destination[j])
    print(' '.join([str(i) for i in sorted(final)]))
