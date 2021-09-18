import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
for i in range(1, N):
    num[i] += num[i - 1]
num.append(0)
for i in range(M):
    left, right = map(int, sys.stdin.readline().split())
    print(num[right - 1] - num[left - 2])
