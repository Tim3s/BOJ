from itertools import permutations

N, M = map(int, input().split())
for item in sorted(list(set(permutations(map(int, input().split()), M)))):
    print(' '.join(map(str, item)))
