import sys

for _ in range(int(sys.stdin.readline())):
    sys.stdin.readline()
    x, y = map(int, sys.stdin.readline().split())
    fx, fy = map(int, sys.stdin.readline().split())
    nx, ny = map(int, sys.stdin.readline().split())
    if x == fx == nx and (ny - y) * (fy - ny) > 0:
        print(abs(fy - y) + 2)
    elif y == fy == ny and (nx - x) * (fx - nx) > 0:
        print(abs(fx - x) + 2)
    else:
        print(abs(fy - y) + abs(fx - x))
