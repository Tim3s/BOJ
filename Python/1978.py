dump = int(input())
num = [int(i) for i in input().split()]
n = 0
for i in num:
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag and i != 1:
        n += 1
print(n)
