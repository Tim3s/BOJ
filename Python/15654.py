import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
num = list(permutations(sorted(list(map(int, sys.stdin.readline().split()))), M))
for item in num:
    for item2 in item:
        print(item2, end=' ')
    print()
