import sys


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    visited[n] = idx
    for v in backward[n]:
        if visited[v] == -1:
            dfs2(v)


def make(a, b):
    forward[a].append(b)
    backward[b].append(a)


prev = [0]
pref = [0]
n = int(sys.stdin.readline())
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    prev.append(tmp[0])
    pref.append(tmp)
left = 0
right = n - 1
ans = n - 1
while left <= right:
    mid = (left + right) >> 1
    forward = [[] for _ in range(2 * n + 1)]
    backward = [[] for _ in range(2 * n + 1)]
    for i in range(1, n + 1):
        for j in range(mid + 1, n):
            # print(i, j)
            if prev[i] == prev[pref[i][j]]:
                make(-i, pref[i][j])
                make(-pref[i][j], i)
                make(pref[i][j], -i)
                make(i, -pref[i][j])
            elif (prev[i] + 1) % 3 == prev[pref[i][j]]:
                make(-i, -pref[i][j])
                make(pref[i][j], i)
            else:
                make(i, pref[i][j])
                make(-pref[i][j], -i)
    # print(mid)
    # print(forward)
    # print(backward)
    stack = []
    visited = [False] * (2 * n + 1)
    for i in range(-n, 0):
        if not visited[i]:
            dfs1(i)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
    idx = 0
    visited = [-1] * (2 * n + 1)
    while stack:
        cur = stack.pop()
        if visited[cur] == -1:
            dfs2(cur)
            idx += 1
    valid = True
    for i in range(1, n + 1):
        if visited[i] == visited[-i]:
            valid = False
            break
    if valid:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)

