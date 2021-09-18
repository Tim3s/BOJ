import math
import sys


def dfs(L, remainder, visited):
    if visited == (1 << N) - 1:
        if remainder == 0:
            return 1
        return 0
    if dp[remainder][visited] != -1:
        return dp[remainder][visited]
    dp[remainder][visited] = 0
    for i in range(N):
        tmp = 1 << i
        if not tmp & visited or not visited:
            dp[remainder][visited] += dfs(L + num[i], (remainder + rm[i][L]) % K, visited | tmp)
    return dp[remainder][visited]


N = int(sys.stdin.readline())
num = [sys.stdin.readline().rstrip() for _ in range(N)]
nums = list(map(int, num))
num = list(map(len, num))
K = int(sys.stdin.readline())
dp = [[-1] * (1 << N) for _ in range(K)]
rm = [[0] * sum(num) for _ in range(N)]
for i in range(N):
    for j in range(sum(num)):
        rm[i][j] = (nums[i] * 10 ** j) % K
numer = dfs(0, 0, 0)
denom = math.factorial(N)
gcd = math.gcd(numer, denom)
print(numer // gcd, denom // gcd, sep='/')
