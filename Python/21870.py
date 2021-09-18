import sys


def gcd(a, b):
    a, b = sorted([a, b])
    while a != 0:
        tmp = b % a
        b = a
        a = tmp
    return b


def get(start, end):
    res = room[start]
    for i in range(start + 1, end + 1):
        res = gcd(res, room[i])
    return res


def calc(start, end):
    if start == end:
        return room[start]
    mid = (start + end - 1) // 2
    return max(calc(start, mid) + get(mid + 1, end), calc(mid + 1, end) + get(start, mid))


N = int(sys.stdin.readline())
room = list(map(int, sys.stdin.readline().split()))
print(calc(0, N - 1))
