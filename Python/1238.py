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


N, M, X = map(int, sys.stdin.readline().split())
toparty = [LinkedList() for _ in range(N + 1)]
tohome = [LinkedList() for _ in range(N + 1)]
for _ in range(M):
    S, E, T = map(int, sys.stdin.readline().split())
    toparty[E].append(S, T)
    tohome[S].append(E, T)
time = [0] * (N + 1)
heap = [(0, X)]
visited = [False] * (N + 1)
while True:
    while heap and visited[heap[0][1]]:
        heapq.heappop(heap)
    if not heap:
        break
    w, v = heapq.heappop(heap)
    visited[v] = True
    time[v] = w
    cur = toparty[v].header()
    while cur:
        if not visited[cur.v]:
            heapq.heappush(heap, (w + cur.w, cur.v))
        cur = cur.nextcave
heap = [(0, X)]
visited = [False] * (N + 1)
while True:
    while heap and visited[heap[0][1]]:
        heapq.heappop(heap)
    if not heap:
        break
    w, v = heapq.heappop(heap)
    visited[v] = True
    time[v] += w
    cur = tohome[v].header()
    while cur:
        if not visited[cur.v]:
            heapq.heappush(heap, (w + cur.w, cur.v))
        cur = cur.nextcave
print(max(time))
