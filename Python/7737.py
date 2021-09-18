import sys


def phi(_n):
    _i = 2
    res = _n
    while _i ** 2 <= _n:
        if not _n % _i:
            prime.append(_i)
            res = res // _i * (_i - 1)
            while not _n % _i:
                _n //= _i
        _i += 1
    if _n != 1:
        prime.append(_n)
        res = res // _n * (_n - 1)
    return res


n, m = map(int, sys.stdin.readline().split())
prime = []
newm = phi(m) - 1
coprime = [0] * 200001
digit = [[0] * len(prime) for _ in range(200001)]
coprime[0] = 1
for i in range(1, 200001):
    k = i
    for j in range(len(prime)):
        digit[i][j] = digit[i - 1][j]
        while not k % prime[j]:
            k //= prime[j]
            digit[i][j] += 1
    coprime[i] = coprime[i - 1] * k % m
ans = 0
for i in range(1, n - 1):
    cur = coprime[i * 2] * pow(coprime[i], newm, m) * pow(coprime[i + 1], newm, m) % m
    for j in range(len(prime)):
        cur = cur * pow(prime[j], digit[i * 2][j] - digit[i][j] - digit[i + 1][j], m) % m
    ans = (ans + cur) % m
print(ans)
