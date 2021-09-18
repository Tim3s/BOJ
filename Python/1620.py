import sys

N, M = list(map(int, sys.stdin.readline().split()))
its = {}
sti = {}
for i in range(1, N + 1):
    tmp = sys.stdin.readline().rstrip()
    its[i] = tmp
    sti[tmp] = i
for i in range(M):
    tmp = sys.stdin.readline().rstrip()
    if tmp.isdigit():
        print(its[int(tmp)])
    else:
        print(sti[tmp])
