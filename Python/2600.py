import sys


def dp(left, right):
    if left < 0 or right < 0:
        return True
    if left < b1 and right < b1:
        return False
    if memo[left][right] != -1:
        return memo[left][right]
    tmp1 = False
    if right >= b1:
        tmp1 = False if dp(left, right - b1) and dp(left, right - b2) and dp(left, right - b3) else True
    tmp2 = False
    if left >= b1:
        tmp2 = False if dp(left - b1, right) and dp(left - b2, right) and dp(left - b3, right) else True
    memo[left][right] = tmp1 or tmp2
    return memo[left][right]


b1, b2, b3 = map(int, sys.stdin.readline().split())
for _ in range(5):
    k1, k2 = map(int, sys.stdin.readline().split())
    memo = [[-1] * 501 for _ in range(501)]
    print('A' if dp(k1, k2) else 'B')
    # print(memo)
