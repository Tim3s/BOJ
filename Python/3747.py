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


# data = []
# try:
#     while True:
#         tmp = list(map(int, sys.stdin.readline().split()))
#         data += tmp
#         if len(tmp) <= 2:
#             break
# except:
#     pass
cur = 0
# print(data)
lines = sys.stdin.readlines()
data = []
for line in lines:
    data += list(map(int, line.split()))
try:
    while True:
        # print(cur)
        tmp = data[cur:data[cur + 1] * 2 + cur + 2]
        # print(tmp)
        cur += 2 + 2 * data[cur + 1]
        # print(cur)
        # print(tmp)
        N, M = tmp[0], tmp[1]
        forward = [set() for _ in range(2 * N + 1)]
        backward = [set() for _ in range(2 * N + 1)]
        for i in range(2, 2 * M + 2, 2):
            a, b = tmp[i], tmp[i + 1]
            # print(a, b)
            forward[-a].add(b)
            forward[-b].add(a)
            backward[b].add(-a)
            backward[a].add(-b)
        stack = []
        visited = [False] * (2 * N + 1)
        for i in range(-N, 0):
            if not visited[i]:
                dfs1(i)
        for i in range(1, N + 1):
            if not visited[i]:
                dfs1(i)
        idx = 0
        # print(stack)
        visited = [-1] * (2 * N + 1)
        while stack:
            current = stack.pop()
            if visited[current] == -1:
                dfs2(current)
                idx += 1
        valid = True
        # print(visited)
        for i in range(1, N + 1):
            if visited[i] == visited[-i]:
                print(0)
                valid = False
                break
        if valid:
            print(1)
except:
    sys.exit(0)
