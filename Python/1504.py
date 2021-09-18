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


N, E = map(int, sys.stdin.readline().split())
V = [LinkedList() for _ in range(N + 1)]
length = [0] * (N + 1)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    V[a].append(b, c)
    V[b].append(a, c)
v1, v2 = map(int, sys.stdin.readline().split())
heap = [(1, 1)]
while True:
    while heap and length[heap[0][1]]:
        heapq.heappop(heap)
    if not heap:
        break
    w, v = heapq.heappop(heap)
    length[v] = w
    if length[v1] and length[v2]:
        break
    cur = V[v].header()
    while cur:
        if not length[cur.v]:
            heapq.heappush(heap, (w + cur.w, cur.v))
        cur = cur.nextcave
if not ((v1 == 1 or length[v1]) and length[v2]):
    print(-1)
    sys.exit(0)
heap = [(1, N)]
endlength = [0] * (N + 1)
while True:
    while heap and endlength[heap[0][1]]:
        heapq.heappop(heap)
    if not heap:
        break
    w, v = heapq.heappop(heap)
    endlength[v] = w
    if endlength[v1] and endlength[v2]:
        break
    cur = V[v].header()
    while cur:
        if not endlength[cur.v]:
            heapq.heappush(heap, (w + cur.w, cur.v))
        cur = cur.nextcave
midlength = [0] * (N + 1)
heap = [(1, v1)]
while True:
    while heap and midlength[heap[0][1]]:
        heapq.heappop(heap)
    if not heap:
        break
    w, v = heapq.heappop(heap)
    midlength[v] = w
    if midlength[v2]:
        break
    cur = V[v].header()
    while cur:
        if not midlength[cur.v]:
            heapq.heappush(heap, (w + cur.w, cur.v))
        cur = cur.nextcave
print(min(length[v1] + endlength[v2], length[v2] + endlength[v1]) + midlength[v2] - 3)
