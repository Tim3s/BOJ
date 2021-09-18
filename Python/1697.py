import sys
from collections import deque

N, K = list(map(int, input().split()))
if N == K:
    print(0)
    sys.exit(0)
visited = [False] * 100001
d = deque()
d.append([N, 0])
visited[N] = True
while True:
    loc, time = d.popleft()
    if loc > 0 and not visited[loc - 1]:
        if loc - 1 == K:
            res = time + 1
            break
        visited[loc - 1] = True
        d.append([loc - 1, time + 1])
    if loc + 1 <= 100000 and not visited[loc + 1]:
        if loc + 1 == K:
            res = time + 1
            break
        visited[loc + 1] = True
        d.append([loc + 1, time + 1])
    if loc * 2 <= 100000 and not visited[loc * 2]:
        if loc * 2 == K:
            res = time + 1
            break
        visited[loc * 2] = True
        d.append([loc * 2, time + 1])
print(res)
