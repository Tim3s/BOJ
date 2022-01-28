import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
conquer = [0] * (N + 1)
last = [0] * (N + 1)
for i in range(1, N + 1):
    V, E = map(int, sys.stdin.readline().split())
    conquer[i] = V - E
    last[i] = last[i-1] + V
    for _ in range(E):
        sys.stdin.readline()
Q = int(sys.stdin.readline())
for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        print(conquer[query[1]])
        continue
    tmp = bisect_left(last, query[1])
    if query[0] == 2:
        conquer[tmp] += 1
    else:
        conquer[tmp] -= 1
