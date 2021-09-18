N = int(input())
fib = [0, 1]
for _ in range(N - 1):
    fib.append(fib[-1] + fib[-2])
print(fib[N])
