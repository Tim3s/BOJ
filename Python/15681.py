import sys
sys.setrecursionlimit(10 ** 9)


def dfs(root):
    ans[root] = 1
    for v in E[root]:
        if not ans[v]:
            ans[root] += dfs(v)
    return ans[root]


N, R, Q = map(int, sys.stdin.readline().split())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    E[U - 1].append(V - 1)
    E[V - 1].append(U - 1)
ans = [0] * N
dfs(R - 1)
for _ in range(Q):
    print(ans[int(sys.stdin.readline()) - 1])
