ln = int(input())
prime = [True] * 10000
for i in range(2, 10000):
    if prime[i]:
        for j in range(2 * i, 10000, i):
            prime[j] = False
for nothing in range(ln):
    n = int(input())
    for i in range(int(n / 2), n):
        if prime[i] and prime[n - i]:
            print(n - i, i)
            break
