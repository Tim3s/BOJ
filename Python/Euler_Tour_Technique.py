def dfs(x):
    global cnt
    cnt += 1
    into[x] = cnt
    for v in V[x]:
        dfs(v)
    out[x] = cnt


n = int(input())
into = [0] * n
out = [0] * n
V = [[] for _ in range(n)]
