import sys

ln = int(sys.stdin.readline())
n = [0] * 10001
for nothing in range(ln):
    n[int(sys.stdin.readline())] += 1
for i in range(1, 10001):
    if n[i] != 0:
        for j in range(n[i]):
            print(i)
