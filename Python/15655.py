import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
for item in list(combinations(sorted(map(int, sys.stdin.readline().split())), M)):
    print(' '.join(map(str, item)))
