prime = set()
isPrime = [True for _ in range(1000001)]
for i in range(3, 1000000, 2):
    if isPrime[i]:
        prime.add(i)
        for j in range(2*i, 1000001, i):
            isPrime[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n//2+1, 2):
        if i in prime and n-i in prime:
            break
    print(f"{n} = {i} + {n-i}")
