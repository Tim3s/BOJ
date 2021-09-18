import sys


def clockwise(a, b, c):
    tmp = (c[1] - b[1]) * (b[0] - a[0]) - (c[0] - b[0]) * (b[1] - a[1])
    return 0 if tmp == 0 else (1 if tmp > 0 else -1)


L1 = list(map(int, sys.stdin.readline().split()))
L2 = list(map(int, sys.stdin.readline().split()))
x1 = L1[:2]
x2 = L1[2:]
x3 = L2[:2]
x4 = L2[2:]
c1 = clockwise(x1, x2, x3)
c2 = clockwise(x1, x2, x4)
c3 = clockwise(x3, x4, x1)
c4 = clockwise(x3, x4, x2)
if c1 * c2 == c3 * c4 == 0:
    if min(x1[0], x2[0]) <= max(x3[0], x4[0]) and min(x3[0], x4[0]) <= max(x1[0], x2[0]) and\
            min(x1[1], x2[1]) <= max(x3[1], x4[1]) and min(x3[1], x4[1]) <= max(x1[1], x2[1]):
        print(1)
    else:
        print(0)
    sys.exit(0)
c1 *= c2
c3 *= c4
print(int(c1 <= 0 and c3 <= 0))
