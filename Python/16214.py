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


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    philist = [M]
    while philist[-1] != 1:
        philist.append(phi(philist[-1]))
    cur = N
    for i in range(len(philist) - 1, -1, -1):
        cur = pow(N, cur, philist[i]) + philist[i]
    print(cur % M)
