import math
import sys

X, Y, D, T = map(int, sys.stdin.readline().split())
dist = math.sqrt(X ** 2 + Y ** 2)
if dist < D:
    print(min(T + D - dist, dist, 2 * T))
else:
    print(min(dist // D * (T - D) + dist, dist, (dist // D + 1) * T))
