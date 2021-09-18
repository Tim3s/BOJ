import sys
import math


def mul(a, b, c):
    if b == 1:
        return a % c
    mullist = [a % c] * int(math.log(b, 2) + 1)
    for i in range(1, len(mullist)):
        mullist[i] = (mullist[i - 1] ** 2) % c
    res = 1
    for i in range(len(mullist)):
        if b % 2 == 1:
            res = (res * mullist[i]) % c
        b = b // 2
    return res


num = [int(i) for i in sys.stdin.readline().split()]
print(mul(num[0], num[1], num[2]))