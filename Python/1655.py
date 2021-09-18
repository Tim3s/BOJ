import heapq
import sys

low = []
high = []
N = int(sys.stdin.readline())
for i in range(N):
    cur = int(sys.stdin.readline())
    if i % 2:
        heapq.heappush(high, cur)
    else:
        heapq.heappush(low, (-cur, cur))
    if i != 0:
        while high[0] < low[0][1]:
            tmp = heapq.heappop(high)
            heapq.heappush(high, heapq.heappop(low)[1])
            heapq.heappush(low, (-tmp, tmp))
    print(low[0][1])
