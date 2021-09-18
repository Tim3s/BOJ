from itertools import combinations

N, M = map(int, input().split())
for item in sorted(list(set(combinations(sorted(map(int, input().split())), M)))):
    print(' '.join(map(str, item)))
