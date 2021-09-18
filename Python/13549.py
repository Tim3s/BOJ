import sys
from collections import deque

N, K = list(map(int, input().split()))
if N == K:
    print(0)
    sys.exit(0)
visited = [100000] * 100001
d = deque()
d.append([N, 0])
visited[N] = 0
res = 100000
while d:
    loc, time = d.popleft()
    if loc > 0 and visited[loc - 1] > time + 1:
        if loc - 1 == K:
            res = min(res, time + 1)
        visited[loc - 1] = time + 1
        d.append([loc - 1, time + 1])
    if loc + 1 <= 100000 and visited[loc + 1] > time + 1:
        if loc + 1 == K:
            res = min(res, time + 1)
        visited[loc + 1] = time + 1
        d.append([loc + 1, time + 1])
    if loc * 2 <= 100000 and visited[loc * 2] > time:
        if loc * 2 == K:
            res = min(res, time)
        visited[loc * 2] = time
        d.append([loc * 2, time])
print(res)
