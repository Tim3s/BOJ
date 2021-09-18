import sys
import math

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if d > r1 + r2:
    print(format(0, '.3f'))
elif d + r1 <= r2:
    print(format(math.pi * r1 ** 2, '.3f'))
elif d + r2 <= r1:
    print(format(math.pi * r2 ** 2, '.3f'))
else:
    k1 = (d ** 2 + r1 ** 2 - r2 ** 2) / (2 * r1 * d)
    k1 = 2 * math.acos(k1)
    k2 = 2 * math.acos((d ** 2 - r1 ** 2 + r2 ** 2) / (2 * r2 * d))
    print(format(1 / 2 * (r1 ** 2 * (k1 - math.sin(k1)) + r2 ** 2 * (k2 - math.sin(k2))), '.3f'))
