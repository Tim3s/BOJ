import math
tmp = list(map(int, input().split()))
print(int(math.factorial(tmp[0]) // math.factorial(tmp[1]) // math.factorial(tmp[0] - tmp[1])))
