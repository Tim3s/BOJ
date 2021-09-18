import sys


def dfsb(n, tmpsub):
    for i in range(tmpsub + 2, N, 2):
        for x, y in bloc[i]:
            if x + y not in ur:
                ur.add(x + y)
                dfsb(n + 1, i)
                ur.remove(x + y)
    global ansb
    ansb = max(ansb, n)


def dfsw(n, tmpsub):
    for i in range(tmpsub + 2, N, 2):
        for x, y in bloc[i]:
            if x + y not in ur:
                ur.add(x + y)
                dfsw(n + 1, i)
                ur.remove(x + y)
    global answ
    answ = max(answ, n)


N = int(sys.stdin.readline())
chess = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ur = set()
bloc = [[] for _ in range(2 * N - 1)]
for i in range(N):
    for j in range(N):
        if chess[i][j] == 1:
            bloc[i - j].append((i, j))
ansb = 0
answ = 0
dfsb(0, -(N + 1))
dfsw(0, -N)
print(ansb + answ)
