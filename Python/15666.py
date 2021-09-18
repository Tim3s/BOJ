from itertools import combinations_with_replacement

N, M = map(int, input().split())
for item in sorted(list(set(combinations_with_replacement(sorted(map(int, input().split())), M)))):
    print(' '.join(map(str, item)))
