import math
import sys
import decimal

T = int(sys.stdin.readline())
for _ in range(T):
    a, b, k = map(int, sys.stdin.readline().split())
    a *= 10 ** 6
    b *= 10 ** 6
    r0 = (a + b - math.sqrt(a ** 2 + b ** 2)) / 2
    # if k == 1:
    #     print(math.pi * r0 ** 2)
    #     continue
    a -= r0
    b -= r0
    a = math.sqrt(r0 ** 2 + a ** 2)
    b = math.sqrt(r0 ** 2 + b ** 2)
    # print(a, b)
    r1 = r0 * (a - r0) / (a + r0)
    a -= r0 + r1
    r2 = r0 * (b - r0) / (b + r0)
    b -= r0 + r2
    c = r0 * math.sqrt(2)
    # r0 *= (math.sqrt(2) - 1)
    for _ in range(1, k):
        if r0 > r1 and r0 > r2:
            tmp = r0 * (c - r0) / (c + r0)
            c -= r0 + tmp
            r0 = tmp
            continue
        if r1 > r2:
            tmp = r1 * (a - r1) / (a + r1)
            a -= r1 + tmp
            r1 = tmp
            continue
        tmp = r2 * (b - r2) / (b + r2)
        b -= r2 + tmp
        r2 = tmp
    # print(r0, r1, r2)
    print(decimal.Decimal(max(r0, r1, r2)) ** decimal.Decimal(2) * decimal.Decimal(math.pi) / decimal.Decimal(10 ** 12))
