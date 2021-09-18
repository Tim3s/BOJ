import sys
sys.setrecursionlimit(10 ** 9)


def dfs(idx, left, right):
    if idx == L:
        return 0
    if memo[idx][left][right]:
        return memo[idx][left][right]
    memo[idx][left][right] = sys.maxsize
    if left != seq[idx]:
        cur = 2 if right == 0 else 1 if right == seq[idx] else 4 if abs(right - seq[idx]) == 2 else 3
        tmp = sorted([left, seq[idx]])
        memo[idx][left][right] = min(memo[idx][left][right], cur + dfs(idx + 1, tmp[1], tmp[0]))
    if right != seq[idx]:
        cur = 2 if left == 0 else 1 if left == seq[idx] else 4 if abs(left - seq[idx]) == 2 else 3
        tmp = sorted([seq[idx], right])
        memo[idx][left][right] = min(memo[idx][left][right], cur + dfs(idx + 1, tmp[1], tmp[0]))
    return memo[idx][left][right]


seq = list(map(int, sys.stdin.readline().split()[:-1]))
L = len(seq)
memo = [[[0] * i for i in range(1, 6)] for _ in range(L)]
print(dfs(0, 0, 0))
