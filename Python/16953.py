import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())
if A > B:
    print(-1)
    sys.exit(0)
if A == B:
    print(1)
    sys.exit(0)
q = deque()
q.append((A, 1))
while q:
    A, time = q.popleft()
    time += 1
    for i in [10 * A + 1, 2 * A]:
        if i == B:
            print(time)
            sys.exit(0)
        if i < B:
            q.append((i, time))
print(-1)
