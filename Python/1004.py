import sys


def dist(_x1, _y1, _x2, _y2):
    return (_x1 - _x2) ** 2 + (_y1 - _y2) ** 2


T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        if (dist(x1, y1, cx, cy) < r ** 2) ^ (dist(x2, y2, cx, cy) < r ** 2):
            cnt += 1
    print(cnt)
