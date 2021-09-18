import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
time = [0 for _ in range(n + 1)]
former = [[] for _ in range(n + 1)]
latter = [[] for _ in range(n + 1)]
back = [[] for _ in range(n + 1)]
for _ in range(m):
    A, B, C = map(int, sys.stdin.readline().split())
    latter[A].append([B, C])
    former[B].append(A)
    back[B].append([A, C])
start, end = map(int, sys.stdin.readline().split())
if start == end:
    print('0\n0')
    sys.exit(0)
q = deque()
q.append(start)
while q:
    A = q.popleft()
    for B, C in latter[A]:
        former[B].remove(A)
        if time[B] < time[A] + C:
            time[B] = time[A] + C
        if not former[B]:
            q.append(B)
print(time[end])
ans = set()
visited = [False] * (n + 1)
q.append(end)
while q:
    cur = q.popleft()
    visited[cur] = True
    for v, c in back[cur]:
        if (cur, v) not in ans and time[cur] == time[v] + c:
            ans.add((cur, v))
            if not visited[v]:
                visited[v] = True
                q.append(v)
print(len(ans))
