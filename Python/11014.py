import sys


def dfs(p):
    vis[p] = True
    for q in V[p]:
        if b[q] == -1 or (not vis[b[q]] and dfs(b[q])):
            b[p] = q
            b[q] = p
            return True
    return False


for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    classroom = [list(sys.stdin.readline()) for _ in range(N)]
    V = [[] for _ in range(N * M)]
    empty = 0
    for i in range(N):
        for j in range(M):
            if classroom[i][j] == '.':
                empty += 1
                for ni, nj in ((i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)):
                    if 0 <= ni < N and 0 <= nj < M and classroom[ni][nj] == '.':
                        # print(i, j, ni, nj)
                        V[i * M + j].append(ni * M + nj)
    # print(V)
    ans = 0
    b = [-1] * (N * M)
    for i in range(N):
        for j in range(0, M, 2):
            if classroom[i][j] == '.':
                vis = [False] * (N * M)
                if dfs(i * M + j):
                    ans += 1
    # print(b, ans)
    print(empty - ans)
