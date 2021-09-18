import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    ans = 0
    i = 5
    while i <= N:
        ans += N // i
        i *= 5
    print(ans)
