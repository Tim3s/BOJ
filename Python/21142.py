import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
forward = [[i for i in range(k) if i != j] for j in range(k)]
backward = [[i for i in range(k) if i != j] for j in range(k)]
for _ in range(n):
    cur = sys.stdin.readline()
    for i in range(k):
        for j in range(i + 1, k):
            A = ord(cur[i]) - 65
            B = ord(cur[j]) - 65
            if A in forward[B]:
                forward[B].remove(A)
                backward[A].remove(B)
ans = 0
q = deque()
for i in range(k):
    if not backward[i]:
        q.append((i, 1))
while q:
    cur, length = q.popleft()
    ans = length
    length += 1
    for v in forward[cur]:
        backward[v].remove(cur)
        if not backward[v]:
            q.append((v, length))
print(ans)
