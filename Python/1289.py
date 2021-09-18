import sys
sys.setrecursionlimit(10 ** 9)


def dfs(start, weight):
    visited[start] = True
    global ans
    ans += weight
    res = 0
    for v, w in E[start]:
        if not visited[v]:
            tmp = dfs(v, (weight + 1) * w) * w
            ans += tmp * res
            ans %= 1000000007
            res += tmp
    return res + 1


N = int(sys.stdin.readline())
E = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B, W = map(int, sys.stdin.readline().split())
    E[A].append([B, W])
    E[B].append([A, W])
ans = 0
visited = [False] * (N + 1)
dfs(1, 0)
print(ans)
