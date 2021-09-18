import sys


def C(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    if memo[n][r]:
        return memo[n][r]
    memo[n][r] = C(n-1, r) + C(n-1, r-1)
    return memo[n][r]


N, M, K = map(int, sys.stdin.readline().split())
memo = [[0] * i for i in range(1, N + M + 2)]
for i in range(N + M):
    memo[i][0] = 1
    memo[i][i] = 1
if K > C(N + M, M):
    print(-1)
    sys.exit(0)
for i in range(N + M - 1, -1, -1):
    tmp = C(i, M)
    if tmp < K:
        M -= 1
        print('z', end='')
        K -= tmp
    else:
        print('a', end='')
