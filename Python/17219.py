import sys

N, M = map(int, sys.stdin.readline().split())
table = dict()
for i in range(N):
    site, password = sys.stdin.readline().split()
    table[site] = password
for j in range(M):
    print(table[sys.stdin.readline().rstrip()])
