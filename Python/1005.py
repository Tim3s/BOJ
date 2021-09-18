import sys


def dfs(cur):
    if memo[cur] != -1:
        return memo[cur]
    memo[cur] = 0
    for v in require[cur]:
        memo[cur] = max(memo[cur], dfs(v))
    memo[cur] += D[cur]
    return memo[cur]


T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    memo = [-1] * N
    require = [[] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        require[Y - 1].append(X - 1)
    print(dfs(int(sys.stdin.readline()) - 1))
