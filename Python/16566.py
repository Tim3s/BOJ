import sys
from bisect import bisect_left

N, M, K = map(int, sys.stdin.readline().split())
card = sorted(list(map(int, sys.stdin.readline().split())))
C = map(int, sys.stdin.readline().split())
used = [False] * M
for i in C:
    tmp = bisect_left(card, i)
    if card[tmp] == i:
        tmp += 1
    while used[tmp]:
        tmp += 1
    print(card[tmp])
    used[tmp] = True
