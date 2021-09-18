import sys

n = int(sys.stdin.readline())
M = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
memo = [[0] * n for _ in range(n)]
for i in range(n - 1):
    memo[i][i + 1] = M[i][i + 1]
for diff in range(2, n):
    for i in range(n - diff):
        memo[i][i + diff] = memo[i + 1][i + diff - 1]
        if M[i][i + diff] == 1:
            memo[i][i + diff] += 1
        tmp = max([0] + [memo[i][j] + memo[j + 1][i + diff] for j in range(i, i + diff)])
        memo[i][i + diff] = max(memo[i][i + diff], tmp)
print(memo[0][n - 1])
