import sys
import math


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    print(math.lcm(*num) % 1000000007)
