import math
import sys

D1, D2 = map(int, sys.stdin.readline().split())
denom = [False] * 2001
cnt = 0
for i in range(D1, D2 + 1):
    tmp = []
    for j in range(i):
        cur = i // math.gcd(i, j)
        if not denom[cur]:
            tmp.append(cur)
            cnt += 1
    for j in tmp:
        denom[j] = True
print(cnt)
