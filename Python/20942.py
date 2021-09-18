import sys
sys.setrecursionlimit(10 ** 9)


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


N = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
# print(tmp)
# seat = [0]
# for i in tmp:
#     seat += i
# print(seat)
M = int(sys.stdin.readline())
forward = [set() for _ in range(10 * N + 1)]
backward = [set() for _ in range(10 * N + 1)]
for i in range(len(tmp)):
    if tmp[i]:
        cur = i * 5
        # print(tmp[i])
        for j in range(5):
            # print(j)
            cur += 1
            if tmp[i] & 1 << j:
                forward[-cur].add(cur)
                backward[cur].add(-cur)
                continue
            forward[cur].add(-cur)
            backward[-cur].add(cur)
# print(forward)
for i in range(0, 5 * N, 5):
    tmp3 = i + 3
    tmp4 = i + 4
    tmp5 = i + 5
    forward[-tmp5].add(tmp4)
    forward[tmp5].add(-tmp4)
    forward[tmp5].add(-tmp3)
    forward[-tmp4].add(tmp5)
    forward[tmp4].add(-tmp5)
    forward[tmp3].add(-tmp5)
    backward[tmp4].add(-tmp5)
    backward[-tmp4].add(tmp5)
    backward[-tmp3].add(tmp5)
    backward[tmp5].add(-tmp4)
    backward[-tmp5].add(tmp4)
    backward[-tmp5].add(tmp3)
for _ in range(M):
    # print(forward)
    t, x, y, z = sys.stdin.readline().split()
    x = int(x) * 5 - 5
    y = int(y) * 5 - 5
    # print(x, y)
    z = int(z)
    # print(z)
    if t == '&':
        # print('&')
        for j in range(5):
            x += 1
            y += 1
            if z & 1 << j:
                forward[-x].add(x)
                forward[-y].add(y)
                backward[x].add(-x)
                backward[y].add(-y)
                continue
            forward[x].add(-y)
            forward[y].add(-x)
            backward[-y].add(x)
            backward[-x].add(y)
        continue
    for j in range(5):
        x += 1
        y += 1
        if z & 1 << j:
            forward[-x].add(y)
            forward[-y].add(x)
            backward[y].add(-x)
            backward[x].add(-y)
            continue
        forward[x].add(-x)
        forward[y].add(-y)
        backward[-x].add(x)
        backward[-y].add(y)
stack = []
visited = [False] * (10 * N + 1)
for i in range(-5 * N, 0):
    if not visited[i]:
        dfs1(i)
for i in range(1, 5 * N + 1):
    if not visited[i]:
        dfs1(i)
idx = 0
visited = [-1] * (10 * N + 1)
while stack:
    cur = stack.pop()
    if visited[cur] == -1:
        dfs2(cur)
        idx += 1
ans = [0] * (5 * N + 1)
for i in range(1, 5 * N + 1):
    if visited[i] == visited[-i]:
        print(0)
        sys.exit(0)
    if visited[i] > visited[-i]:
        ans[i] = 1
print(1)
# print(seat)
# print(visited)
for i in range(1, 5 * N, 5):
    res = 0
    for j in range(5):
        res += (1 << j) * ans[i + j]
    print(res, end=' ')
