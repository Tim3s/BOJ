import sys
import math

T = int(sys.stdin.readline())
for index in range(1, T + 1):
    A, B, N = map(int, sys.stdin.readline().split())
    digits = []
    i = 2
    for i in range(2, int(math.sqrt(N)) + 1):
        if not N % i:
            digits.append(i)
            while not N % i:
                N //= i
        i += 1
    if N != 1:
        digits.append(N)
    ans = 0
    for i in range(1, 1 << len(digits)):
        mul = 1
        cnt = 0
        for j in range(len(digits)):
            if i & (1 << j):
                cnt += 1
                mul *= digits[j]
        if cnt % 2:
            ans -= B // mul - (A - 1) // mul
        else:
            ans += B // mul - (A - 1) // mul
    print("Case #" + str(index) + ":", B - A + 1 + ans)
