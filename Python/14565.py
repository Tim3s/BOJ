import sys


def gcd(a, b):
    if b == 0:
        return a, (1, 0)
    res = gcd(b, a % b)
    g = res[0]
    x, y = res[1]
    return g, (y, x - (a // b) * y)


N, A = map(int, sys.stdin.readline().split())
print(0 if A % N == 0 else N - (A % N), end=' ')
ans = gcd(A, N)
if ans[0] > 1:
    print(-1)
else:
    print((ans[1][0] + N) % N)
