import sys

N = int(sys.stdin.readline())
if N == 1:
    print(0)
    sys.exit(0)
scoville = sorted(list(map(int, sys.stdin.readline().split())))
ans = -pow(2, N - 1, 1000000007) * scoville[0] - scoville[-1] + scoville[0]
ans %= 1000000007
for i in range(1, N - 1):
    ans += scoville[i] * (pow(2, i, 1000000007) - pow(2, N - i - 1, 1000000007))
    ans %= 1000000007
ans += scoville[-1] * pow(2, N - 1, 1000000007)
ans %= 1000000007
print(ans)
