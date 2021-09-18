import math
import sys
import heapq

N, R, BX, BY, BVX, BVY = map(int, sys.stdin.readline().split())
time = []
possible = 0
for _ in range(N):
    X, Y, VX, VY = map(int, sys.stdin.readline().split())
    X -= BX
    Y -= BY
    VX -= BVX
    VY -= BVY
    if VX == VY == 0:
        if X ** 2 + Y ** 2 <= R ** 2:
            possible += 1
        continue
    a = VX ** 2 + VY ** 2
    b = X * VX + Y * VY
    c = X ** 2 + Y ** 2 - R ** 2
    d = b ** 2 - a * c
    if d < 0:
        continue
    if d == 0:
        if a * b <= 0:
            time.append([-b / a, -b / a])
        continue
    if math.sqrt(d) >= b:
        time.append([max(0, (-b - math.sqrt(d)) / a), (-b + math.sqrt(d)) / a])
time.sort()
end = []
ans = 0
for s, e in time:
    while end and end[0] < s:
        heapq.heappop(end)
    heapq.heappush(end, e)
    ans = max(ans, len(end))
print(possible + ans)
