import sys
from collections import deque

N, K = list(map(int, input().split()))
if N == K:
    print(0)
    print(1)
    sys.exit(0)
q = deque()
q.append(N)
cnt = 0
visited = [100001] * 100001
visited[N] = 0
while q:
    x = q.popleft()
    if x == K:
        cnt += 1
        continue
    for nx in [x + 1, x - 1, 2 * x]:
        if 0 <= nx <= 100000 and visited[nx] > visited[x]:
            visited[nx] = visited[x] + 1
            q.append(nx)
print(visited[K])
print(cnt)
