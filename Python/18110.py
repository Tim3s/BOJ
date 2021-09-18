import sys
import math

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit(0)
if n <= 3:
    print(math.floor(sum([int(sys.stdin.readline()) for _ in range(n)]) / n + 0.5))
    sys.exit(0)
deleted = math.floor(n * 0.15 + 0.5)
num = sorted([int(sys.stdin.readline()) for _ in range(n)])[deleted:-deleted]
print(math.floor(sum(num) / (n - 2 * deleted) + 0.5))
