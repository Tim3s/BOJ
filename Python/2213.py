import sys
from collections import deque


def dfs(x):
    memo[x][1] = w[x]
    memo[x][0] = 0
    for i in e[x]:
        if memo[i][0] == -1:
            dfs(i)
            memo[x][0] += memo[i][eachmax[i]]
            memo[x][1] += memo[i][0]
    eachmax[x] = 0 if memo[x][0] > memo[x][1] else 1


n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
e = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    e[a-1].append(b-1)
    e[b-1].append(a-1)
memo = [[-1, -1] for _ in range(n)]
eachmax = [[2] for _ in range(n)]
dfs(0)
print(memo[0][eachmax[0]])
ans = set()
visited = [False] * n
q = deque()
q.append((0, eachmax[0]))
visited[0] = True
while q:
    v, indep = q.popleft()
    if indep:
        ans.add(v)
        for i in e[v]:
            if not visited[i]:
                q.append((i, 0))
                visited[i] = True
    else:
        for i in e[v]:
            if not visited[i]:
                q.append((i, eachmax[i]))
print(' '.join(list(map(lambda x: str(x + 1), sorted(list(ans))))))
