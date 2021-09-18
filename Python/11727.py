import sys

res = [1, 1]
n = int(sys.stdin.readline())
for i in range(1, n):
    res.append((2 * res[-2] + res[-1]) % 10007)
print(res[n])
