import math

ln = int(input())
for nothing in range(ln):
    k = int(input())
    n = int(input())
    print(int(math.factorial(n + k) / (math.factorial(n - 1) * math.factorial(k + 1))))
