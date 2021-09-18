import sys
import math

A, B = map(int, sys.stdin.readline().split())
A, B = max(A, B), min(A, B)
tmp = A - B
if tmp == 0:
    print(1)
    sys.exit(0)
digits = set()
for i in range(1, int(math.sqrt(tmp)) + 1):
    if not tmp % i:
        digits.add(i)
        digits.add(tmp // i)
ans = sys.maxsize
cur = 10 ** 19
for i in digits:
    tmp = i - B % i
    if math.lcm(A + tmp, B + tmp) < cur:
        cur = math.lcm(A + tmp, B + tmp)
        ans = tmp
    elif math.lcm(A + tmp, B + tmp) == cur:
        ans = min(ans, tmp)
print(ans)
