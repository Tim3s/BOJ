import sys


def dfs(x):
    global cnt
    cnt += 1
    into[x] = cnt
    for v in lower[x]:
        dfs(v)
    out[x] = cnt


def update(x):
    while x <= n:
        tree[x] += tmp[2]
        x += x & -x


def getsum(x):
    res = 0
    while x:
        res += tree[x]
        x -= x & -x
    return res


n, m = map(int, sys.stdin.readline().split())
higher = [0] + list(map(int, sys.stdin.readline().split()))
lower = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    lower[higher[i]].append(i)
into = [0] * (n + 1)
out = [0] * (n + 1)
cnt = 0
dfs(1)
tree = [0] * (n + 1)
for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp[0] == 1:
        update(into[tmp[1]])
    else:
        print(getsum(out[tmp[1]]) - getsum(into[tmp[1]] - 1))
