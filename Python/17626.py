n = int(input())
num = [0, 1]
for i in range(2, n + 1):
    a = 2
    num.append(1 + num[-1])
    while a ** 2 <= i:
        num[i] = min(num[i], 1 + num[i - a ** 2])
        a += 1
print(num[n])
