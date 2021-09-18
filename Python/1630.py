import math

ans = 1
N = int(input())
squared = math.sqrt(N)
prime = [True] * (N + 1)
ans *= 2 ** int(math.log2(N))
ans %= 987654321
for i in range(3, N + 1, 2):
    if prime[i]:
        ans *= i ** int(math.log(N, i))
        ans %= 987654321
        for j in range(i * i, N + 1, 2 * i):
            prime[j] = False
print(ans)
