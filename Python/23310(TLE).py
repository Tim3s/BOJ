import math
import sys

N, M = map(int, sys.stdin.readline().split())
X = [0] + list(map(int, sys.stdin.readline().split()))
weeks = [0] * (N + 1)
weeks[0] = 2147483647
lcm = math.lcm(N, M)
cant = [[] for _ in range(N + 1)]
cancount = [lcm // N] * (N + 1)
# print(N, M, lcm)
for i in range(M, lcm + 1, M):
    # print('doing')
    cant[(i-1) % N + 1].append((i-1) // N + 1)
    cancount[(i-1) % N + 1] -= 1
for i in range(1, N + 1):
    if cancount[i] == 0:
        weeks[i] = 2147483647
        continue
    weeks[i] += (X[i] // cancount[i]) * lcm // N
    if X[i] % cancount[i] == 0:
        cur = lcm // N
        while cur in cant[i]:
            cur -= 1
            weeks[i] -= 1
    else:
        cur = 0
        tmp = X[i] % cancount[i]
        while tmp:
            cur += 1
            weeks[i] += 1
            if cur not in cant[i]:
                tmp -= 1
print(cant)
print(weeks)
print(weeks.index(min(weeks)))
