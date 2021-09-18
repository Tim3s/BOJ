import sys


def dp(cur, seq, bits):
    if seq == N:
        return 1
    if memo[seq][bits] != -1:
        return memo[seq][bits]
    memo[seq][bits] = 0
    for i in range(N):
        if not bits & 1 << i:
            memo[seq][bits] = max(memo[seq][bits], dp(i, seq + 1, bits | 1 << i) * bond[i][seq] / 100)
    return memo[seq][bits]


N = int(sys.stdin.readline())
bond = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [[-1] * (1 << N) for _ in range(N)]
print(format(dp(0, 0, 0) * 100, '.10f'))
