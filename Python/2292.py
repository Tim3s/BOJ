import math
n = int(input())
if n == 1:
    print(1)
else:
    print(int((3 + math.sqrt(-15 + 12 * n)) / 6 + 1))
