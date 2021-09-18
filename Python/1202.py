import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewel = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
bag = sorted([int(sys.stdin.readline()) for _ in range(K)])
heap = []
idx = 0
ans = 0
for i in bag:
    while idx < N and jewel[idx][0] <= i:
        heapq.heappush(heap, -jewel[idx][1])
        idx += 1
    if heap:
        ans -= heapq.heappop(heap)
print(ans)
