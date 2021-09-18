import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
bigger = [[] for _ in range(N)]
smaller = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    smaller[A].append(B)
    bigger[B].append(A)
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
print(*ans)
