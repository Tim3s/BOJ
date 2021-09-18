def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


num = [int(i) for i in input().split()]
prime = list(range(2, num[1] + 1))
index = 0
for i in range(max(2, num[0]), num[1] + 1):
    if isPrime(i):
        print(i)
