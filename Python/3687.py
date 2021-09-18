import sys
import copy

T = int(sys.stdin.readline())
smalllist = [0, 0, 1, 7, 4, 2, 0, 8]
small = [0, 0, 1, 7, 4, 2, 6, 8, 10]
for _ in range(9, 101):
    small.append(min([small[-i] * 10 + smalllist[i] for i in range(2, 8)]))
for _ in range(T):
    n = int(sys.stdin.readline())
    if n % 2:
        big = '7' + '1' * (n // 2 - 1)
    else:
        big = '1' * (n // 2)
    print(small[n], big)
