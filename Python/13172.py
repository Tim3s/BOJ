import sys

res = 0
M = int(sys.stdin.readline())
for _ in range(M):
    b, a = map(int, sys.stdin.readline().split())
    res += a * pow(b, 1000000005, 1000000007)
    res %= 1000000007
print(res)
