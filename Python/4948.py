def isPrime(n, m):
    prime = [True] * m
    for i in range(2, int(m ** 0.5 + 1)):
        if prime[i]:
            for j in range(2 * i, m, i):
                prime[j] = False
    result = 0
    for i in range(n, m):
        if prime[i]:
            result += 1
    print(result)


num = int(input())
while num != 0:
    n = 0
    isPrime(num + 1, 2 * num + 1)
    num = int(input())
