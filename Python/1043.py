import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
q = deque(list(map(int, sys.stdin.readline().split()[1:])))
know = [False] * (N + 1)
for item in q:
    know[item] = True
party = [set(map(int, sys.stdin.readline().split()[1:])) for _ in range(M)]
visited = [False] * M
while q:
    cur = q.popleft()
    for i in range(M):
        if not visited[i] and cur in party[i]:
            visited[i] = True
            for person in party[i]:
                if not know[person]:
                    know[person] = True
                    q.append(person)
res = 0
for i in range(M):
    if not visited[i]:
        res += 1
print(res)
