import math

num = input().split()
num[0] = int(num[0])
num[1] = int(num[1])
num[2] = int(num[2])
print(math.ceil((num[2] - num[0]) / (num[0] - num[1]) + 1))
