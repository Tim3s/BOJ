import sys

N, K = map(int, sys.stdin.readline().split())
print(sorted(list(map(int, sys.stdin.readline().split())))[K - 1])
