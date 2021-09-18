import sys


def dp(left, right):
    if left == 2 or right == 2:
        return True
    if memo[left][right] != -1:
        return memo[left][right]
    tmp1 = False
    if left > 2:
        for i in range(1, left // 2 + 1):
            if not dp(i, left - i):
                tmp1 = True
                break
    tmp2 = False
    if right > 2:
        for i in range(1, right // 2 + 1):
            if not dp(i, right - i):
                tmp2 = True
                break
    memo[left][right] = tmp1 or tmp2
    return memo[left][right]


N, M = map(int, sys.stdin.readline().split())
memo = [[-1] * 101 for _ in range(101)]
print('A' if dp(N, M) else 'B')
