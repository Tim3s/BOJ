import sys


def bfs(curx, cury):
    global loc, N, M, stack
    if curx > 0 and loc[curx - 1][cury]:
        stack.append([curx - 1, cury])
        loc[curx - 1][cury] = False
    if cury > 0 and loc[curx][cury - 1]:
        stack.append([curx, cury - 1])
        loc[curx][cury - 1] = False
    if curx < M - 1 and loc[curx + 1][cury]:
        stack.append([curx + 1, cury])
        loc[curx + 1][cury] = False
    if cury < N - 1 and loc[curx][cury + 1]:
        stack.append([curx, cury + 1])
        loc[curx][cury + 1] = False


T = int(sys.stdin.readline())
for j in range(T):
    res = 0
    M, N, K = list(map(int, sys.stdin.readline().split()))
    loc = [[False] * N for i in range(M)]
    stack = []
    for i in range(K):
        x, y = list(map(int, sys.stdin.readline().split()))
        loc[x][y] = True
    for i in range(M):
        for k in range(N):
            if loc[i][k]:
                loc[i][k] = False
                bfs(i, k)
                while len(stack) != 0:
                    tmp = stack.pop(0)
                    bfs(tmp[0], tmp[1])
                res += 1
    print(res)
