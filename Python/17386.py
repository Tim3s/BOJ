import sys


def clockwise(a, b, c):
    tmp = (c[1] - b[1]) * (b[0] - a[0]) - (c[0] - b[0]) * (b[1] - a[1])
    return int(tmp / abs(tmp))


L1 = list(map(int, sys.stdin.readline().split()))
L2 = list(map(int, sys.stdin.readline().split()))
x1 = L1[:2]
x2 = L1[2:]
x3 = L2[:2]
x4 = L2[2:]
print(int(clockwise(x1, x2, x3) * clockwise(x1, x2, x4) == clockwise(x1, x3, x4) * clockwise(x2, x3, x4) == -1))
