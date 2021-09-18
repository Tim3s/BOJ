import math

n = int(input())
cnt = n
for i in range(1, int(math.sqrt(n))):
    cnt += (n - 1) // i
i = (n - 1) // int(math.sqrt(n))
while i:
    cnt += i * ((n - 1) // i - (n - 1) // (i + 1))
    i -= 1
print(cnt)
