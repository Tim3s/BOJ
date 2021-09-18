import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
tmp = a[0]
for i in range(n - 1):
    a[i] = (a[i + 1] - a[i]) % 360000
a[n - 1] = (tmp - a[n - 1]) % 360000
b = list(map(int, sys.stdin.readline().split()))
b.sort()
tmp = b[0]
for i in range(n - 1):
    b[i] = (b[i + 1] - b[i]) % 360000
b[n - 1] = (tmp - b[n - 1]) % 360000
newidx = [0] * n
idx = 0
for i in range(1, len(a)):
    while idx > 0 and a[i] != a[idx]:
        idx = newidx[idx - 1]
    if a[idx] == a[i]:
        idx += 1
        newidx[i] = idx
idx = 0
for i in range(-n, n):
    while idx > 0 and a[idx] != b[i]:
        idx = newidx[idx - 1]
    if a[idx] == b[i]:
        idx += 1
        if idx == n:
            print('possible')
            sys.exit(0)
print('impossible')
