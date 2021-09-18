import sys


m, Seed, X1, X2 = map(int, sys.stdin.readline().split())
a = (pow((X1 - Seed), m - 2, m) * (X2 - X1)) % m
c = (X1 - a * Seed) % m
print(a, c)
