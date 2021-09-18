n = int(input())
n %= 1500000
if n == 0 or n == 1:
    print(n)
else:
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append((fib[-1] + fib[-2]) % 1000000)
    print(fib[n])
