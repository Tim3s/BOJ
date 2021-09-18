import sys


def cclockwise(a, b, c):
    return a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1])


x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
A = [x1, y1]
B = [x2, y2]
C = [x3, y3]
D = [x4, y4]
c1 = cclockwise(A, B, C)  # D
c2 = cclockwise(A, B, D)  # C
c3 = cclockwise(C, D, A)  # B
c4 = cclockwise(C, D, B)  # A
if c1 * c2 == 0 and c3 * c4 == 0:
    if min(A[0], B[0]) <= max(C[0], D[0]) and min(C[0], D[0]) <= max(A[0], B[0]) and \
            min(A[1], B[1]) <= max(C[1], D[1]) and min(C[1], D[1]) <= max(A[1], B[1]):
        print(1)
        if max(A[0], B[0]) == min(C[0], D[0]) and max(A[1], B[1]) == min(C[1], D[1]):
            print(min(C[0], D[0]), min(C[1], D[1]))
        elif max(C[0], D[0]) == min(A[0], D[0]) and max(C[1], D[1]) == min(A[1], B[1]):
            print(min(A[0], B[0]), min(A[1], B[1]))
        elif c2 * c3 != 0 or c1 * c3 != 0:
            print(*B)
        elif c2 * c4 != 0 or c1 * c4 != 0:
            print(*A)
    else:
        print(0)
elif c1 * c2 <= 0 and c3 * c4 <= 0:
    print(1)
    if x1 != x2 and x3 != x4:
        m1, m2 = (y2 - y1) / (x2 - x1), (y4 - y3) / (x4 - x3)
        n1, n2 = -m1 * x1 + y1, -m2 * x3 + y3
        print((n1 - n2) / (m2 - m1), (m2 * n1 - m1 * n2) / (m2 - m1))
    elif x1 == x2 and x3 != x4:
        m = (y4 - y3) / (x4 - x3)
        print(x1, m * (x1 - x3) + y3)
    elif x3 == x4 and x1 != x2:
        m = (y2 - y1) / (x2 - x1)
        print(x3, m * (x3 - x1) + y1)
else:
    print(0)
