import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
bigger = [set() for _ in range(N)]
smaller = [set() for _ in range(N)]
visited = [False] * N
for _ in range(M):
    tmp = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    for i in range(1, len(tmp) - 1):
        smaller[tmp[i]].add(tmp[i + 1])
        bigger[tmp[i + 1]].add(tmp[i])
q = deque()
for i in range(N):
    if len(bigger[i]) == 0:
        q.append(i)
        visited[i] = True
ans = []
while q:
    cur = q.popleft()
    ans.append(cur + 1)
    for v in smaller[cur]:
        bigger[v].remove(cur)
        if not visited[v]:
            if not len(bigger[v]):
                visited[v] = True
                q.append(v)
if len(ans) == N:
    print('\n'.join(list(map(str, ans))))
else:
    print(0)
