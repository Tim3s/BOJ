N = int(input())
num = []
i = 2
while i ** 2 <= N:
    while not N % i:
        num.append(i)
        N //= i
    i += 1
if N != 1:
    num.append(N)
if len(num) <= 1:
    print(-1)
else:
    for i in range(1, len(num), 2):
        if i == len(num) - 2:
            print(num[i - 1] * num[i] * num[i + 1])
        else:
            print(num[i - 1] * num[i], end=' ')
