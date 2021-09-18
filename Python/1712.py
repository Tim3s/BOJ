num = input().split()
num[0] = int(num[0])
num[1] = int(num[1])
num[2] = int(num[2])
n = 0
if num[1] >= num[2]:
    n = -1
else:
    n = int(num[0] / (num[2] - num[1]) + 1)
print(n)
