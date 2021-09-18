def fibonacci(n):
    if fib[n] != -1:
        return fib[n]
    fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib[n]


fib = [0, 1]
for i in range(2, 10001):
    fib.append(fib[-1] + fib[-2])
print(fibonacci(int(input())))
