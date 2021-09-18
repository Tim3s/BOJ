import sys
import math


T = int(sys.stdin.readline())
memo = [False] * 1000001
for i in range(1, 1000001):
    for j in range(1, math.floor(math.sqrt(i)) + 1):
        if not memo[i - j ** 2]:
            memo[i] = True
            break
for _ in range(T):
    print('koosaga' if memo[int(sys.stdin.readline())] else 'cubelover')
