import sys


def updateodd(x, val):
    while x < length:
        odd[x] ^= val
        x += x & -x


def getodd(x):
    res = 0
    while x:
        res ^= odd[x]
        x -= x & -x
    return res


def updateeven(x, val):
    while x < length:
        even[x] ^= val
        x += x & -x


def geteven(x):
    res = 0
    while x:
        res ^= even[x]
        x -= x & -x
    return res


n, q = map(int, sys.stdin.readline().split())
A = [0] + list(map(int, sys.stdin.readline().split()))
length = n // 2 + 2
odd = [0] * length
even = [0] * length
for i in range(1, n + 1, 2):
    updateodd(i // 2 + 1, A[i])
for i in range(2, n + 1, 2):
    updateeven(i // 2, A[i])
for _ in range(q):
    # print(odd, even)
    op, l, u = map(int, sys.stdin.readline().split())
    if op == 1:
        if l % 2:
            updateodd(l // 2 + 1, A[l] ^ u)
            A[l] = u
        else:
            updateeven(l // 2, A[l] ^ u)
            A[l] = u
    else:
        if (u - l) % 2:
            print(0)
        else:
            if l % 2:
                # print(getodd(u // 2 + 1), getodd(l // 2))
                print(getodd(u // 2 + 1) ^ getodd(l // 2))
            else:
                # print(geteven(u // 2), geteven(l // 2 - 1))
                print(geteven(u // 2) ^ geteven(l // 2 - 1))
