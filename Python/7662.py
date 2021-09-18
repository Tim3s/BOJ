import sys
import heapq

T = int(sys.stdin.readline())
for i in range(T):
    maxheap = []
    minheap = []
    k = int(sys.stdin.readline())
    visit = [False] * k
    for j in range(k):
        tmp = sys.stdin.readline().split()
        if tmp[0] == "I":
            heapq.heappush(maxheap, (-int(tmp[1]), j))
            heapq.heappush(minheap, (int(tmp[1]), j))
        elif tmp[1] == "1":
            while maxheap and visit[maxheap[0][1]]:
                heapq.heappop(maxheap)
            if maxheap:
                visit[heapq.heappop(maxheap)[1]] = True
        else:
            while minheap and visit[minheap[0][1]]:
                heapq.heappop(minheap)
            if minheap:
                visit[heapq.heappop(minheap)[1]] = True
    while minheap and visit[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and visit[maxheap[0][1]]:
        heapq.heappop(maxheap)
    if minheap:
        print(-maxheap[0][0], minheap[0][0])
    else:
        print("EMPTY")
