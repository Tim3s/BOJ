import sys

T = int(sys.stdin.readline())
f = [i for i in range(1000001)]
for i in range(1, 1000001):
    for j in range(2 * i, 1000001, i):
        f[j] += i
    f[i] += f[i - 1]
for _ in range(T):
    print(f[int(sys.stdin.readline())])
