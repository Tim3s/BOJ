import sys


def dfs(p):
    vis[p] = True
    for q in V[p]:
        if b[q] == 0 or (not vis[b[q]] and dfs(b[q])):
            a[p] = q
            b[q] = p
            return True
    return False


def find(p):
    XL.add(p)
    for x in V[p]:
        if x != a[p] and x not in XR:
            XR.add(x)
            if b[x] != 0:
                find(b[x])


N, M = map(int, sys.stdin.readline().split())
ans = 0
V = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    V[i] = list(map(int, sys.stdin.readline().split()))[1:]
a = [0] * (N + 1)
b = [0] * (M + 1)
for i in range(1, N + 1):
    vis = [False] * (N + 1)
    if dfs(i):
        ans += 1
print(ans)
XL = set()
XR = set()
for i in range(1, N + 1):
    if a[i] == 0:
        find(i)
ansl = [i for i in range(1, N + 1) if i not in XL]
print(len(ansl), *ansl)
ansr = sorted(list(XR))
print(len(ansr), *ansr)
