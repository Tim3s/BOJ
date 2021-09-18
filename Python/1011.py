import math

ln = int(input())
for nothing in range(ln):
    tmp = input().split()
    distance = int(tmp[1]) - int(tmp[0])
    even = 2 * (math.ceil((-1 + math.sqrt(1 + 4 * distance)) / 2))
    odd = 2 * (math.ceil(math.sqrt(distance)) - 1) + 1
    print(min(even, odd))
