import math
num = int(input())
big = int((1 + math.sqrt(8 * num)) / 2)
small = int(num - big * (big - 1) / 2)
if big % 2 == 0:
    print(small, '/', big + 1 - small, sep='')
else:
    print(big + 1 - small, '/', small, sep='')
