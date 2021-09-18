import math
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
a = 1
for i in A:
    a *= i
b = 1
for i in B:
    b *= i
res = str(math.gcd(a, b))[-9:]
print(res)
