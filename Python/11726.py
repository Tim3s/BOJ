num = [1, 1]
n = int(input())
for i in range(2, n + 1):
    num.append((num[-1] + num[-2]) % 10007)
print(num[n])
