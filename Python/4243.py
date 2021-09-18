import sys


def dp(left, right, pos):
    if memo[left][right][pos] != -1:
        return memo[left][right][pos]
    if left == 1 and right == N:
        return 0
    memo[left][right][pos] = sys.maxsize
    loc = right if pos else left
    if left > 1:
        memo[left][right][pos] = min(memo[left][right][pos], dp(left - 1, right, 0) + (N - right + left - 1) * (t[loc] - t[left - 1]))
    if right < N:
        memo[left][right][pos] = min(memo[left][right][pos], dp(left, right + 1, 1) + (N - right + left - 1) * (t[right + 1] - t[loc]))
    return memo[left][right][pos]


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    a = int(sys.stdin.readline())
    t = [0, 0] + [int(sys.stdin.readline()) for _ in range(N - 1)]
    for i in range(N):
        t[i + 1] += t[i]
    cost = 0
    length = 0
    ans = -1
    memo = [[[-1] * 2 for _ in range(N + 1)] for _ in range(N + 1)]
    print(dp(a, a, 0))
