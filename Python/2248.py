import sys


def C(n, r):
    if memo[n][r]:
        return memo[n][r]
    memo[n][r] = C(n-1, r) + C(n-1, r-1)
    return memo[n][r]


N, L, I = map(int, sys.stdin.readline().split())
memo = [[0] * i for i in range(1, N + 2)]
for i in range(N + 1):
    memo[i][0] = 1
    memo[i][i] = 1
for i in range(N - 1, -1, -1):
    tmp = [C(i, j) for j in range(min(L + 1, i + 1))]
    tmp = sum(tmp)
    if tmp < I:
        print('1', end='')
        L -= 1
        I -= tmp
    else:
        print('0', end='')
