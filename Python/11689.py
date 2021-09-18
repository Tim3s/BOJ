import sys


def phi(n):
    _i = 2
    res = n
    while _i ** 2 <= n:
        if not n % _i:
            res = res // _i * (_i - 1)
            while not n % _i:
                n //= _i
        _i += 1
    if n != 1:
        res = res // n * (n - 1)
    return res


print(phi(int(sys.stdin.readline())))
