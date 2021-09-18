import sys

N = int(sys.stdin.readline())
sinker = list(map(int, sys.stdin.readline().split()))
weight = set()
for i in range(N):
    cur = sinker[i]
    adder = set()
    for j in weight:
        adder.add(j + cur)
        adder.add(j - cur)
    weight = weight.union(adder)
    weight.add(cur)
    weight.add(-cur)
M = int(sys.stdin.readline())
marble = list(map(int, sys.stdin.readline().split()))
for i in marble:
    print('Y' if i in weight else 'N', end=' ')
