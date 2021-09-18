def fibonacci(n):
    if fib[n] != -1:
        return fib[n]
    fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib[n]


fib = [0] + [1] + [-1] * 45
print(fibonacci(int(input())))
