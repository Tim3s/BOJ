num = [int(i) for i in input().split()]
print(min(num[0], num[1], num[2] - num[0], num[3] - num[1]))
