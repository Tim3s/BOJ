import sys

m = int(sys.stdin.readline())
sparse = [[0] + list(map(int, sys.stdin.readline().split()))]
for i in range(18):
    tmp = [0]
    for j in range(1, m + 1):
        tmp.append(sparse[-1][sparse[-1][j]])
    sparse.append(tmp)
Q = int(sys.stdin.readline())
for _ in range(Q):
    n, x = map(int, sys.stdin.readline().split())
    for i in range(19):
        if n & 1 << i:
            x = sparse[i][x]
    print(x)
