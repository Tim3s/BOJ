N = int(input())
f = [i for i in range(N+1)]
for i in range(N, 0, -1):
    for j in range(2 * i, N+1, i):
        f[j] += i
print(sum(f))
