def dp(n, r):
    if n / r < 2:
        return 0
    if n / r == 2:
        return 2
    if r == 1:
        return n
    if memo[n][r]:
        return memo[n][r]
    memo[n][r] = dp(n-1, r) + dp(n-2, r-1)
    return memo[n][r]


N = int(input())
K = int(input())
memo = [[0] * (K + 1) for _ in range(N + 1)]
print(dp(N, K) % 1000000003)
