import sys
import heapq


N, M = map(int, sys.stdin.readline().split())
heap = []
harder = [[] for _ in range(N)]
easier = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    harder[A].append(B)
    easier[B].append(A)
for i in range(N):
    if not easier[i]:
        heapq.heappush(heap, i)
while heap:
    cur = heapq.heappop(heap)
    print(cur + 1, end=' ')
    for i in harder[cur]:
        easier[i].remove(cur)
        if not easier[i]:
            heapq.heappush(heap, i)
