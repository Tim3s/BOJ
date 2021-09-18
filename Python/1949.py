import sys
sys.setrecursionlimit(10 ** 9)


def dfs(x):
    memo[x][1] = resident[x]
    memo[x][0] = 0
    for i in village[x]:
        if memo[i][0] == -1:
            dfs(i)
            memo[x][0] += max(memo[i][0], memo[i][1])
            memo[x][1] += memo[i][0]


N = int(sys.stdin.readline())
village = [[] for _ in range(N)]
resident = list(map(int, sys.stdin.readline().split()))
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    village[a-1].append(b-1)
    village[b-1].append(a-1)
memo = [[-1, -1] for _ in range(N + 1)]
dfs(0)
print(max(memo[0]))
