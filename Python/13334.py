import sys
import heapq

n = int(sys.stdin.readline())
loc = [list(sorted(list(map(int, sys.stdin.readline().split())))) for _ in range(n)]
d = int(sys.stdin.readline())
loc.sort(key=lambda x: x[1])
heap = []
ans = 0
cur = 0
for i in range(n):
    cur = loc[i][1]
    heapq.heappush(heap, loc[i])
    while heap and heap[0][0] < cur - d:
        heapq.heappop(heap)
    ans = max(ans, len(heap))
print(ans)
