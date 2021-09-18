import sys


def dp(cur, price, bits):
    if memo[cur][price][bits] != -1:
        return memo[cur][price][bits]
    memo[cur][price][bits] = 0
    for i in range(N):
        if not bits & (1 << i) and artist[cur][i] >= price:
            memo[cur][price][bits] = max(memo[cur][price][bits], 1 + dp(i, artist[cur][i], bits | (1 << i)))
    return memo[cur][price][bits]


N = int(sys.stdin.readline())
artist = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
memo = [[[-1] * (1 << 15) for _ in range(10)] for _ in range(N)]
print(dp(0, 0, 1) + 1)
