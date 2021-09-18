import sys
import math


def exp(a, b):
    res = 1
    while b > 0:
        if b % 2:
            res = (res * a) % 1000000007
        b = b // 2
        a = a * a % 1000000007
    return res


def C(n, r):
    return fact[n] * exp((fact[r] * fact[n - r]), 1000000005) % 1000000007


num = [int(i) for i in sys.stdin.readline().split()]
fact = [1] * 4000001
for i in range(2, 4000001):
    fact[i] = fact[i - 1] * i % 1000000007
print(C(num[0], num[1]))
