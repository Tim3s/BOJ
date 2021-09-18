import sys
import math


T = int(sys.stdin.readline())
for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    MNgcd = math.gcd(M, N)
    if x % MNgcd != y % MNgcd:
        print(-1)
        continue
    res = (x - 1) % M + 1
    while (res - 1) % N + 1 != y:
        res += M
    print(res)
