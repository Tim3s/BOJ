import sys
from collections import deque

N = int(sys.stdin.readline())
back = [0] * (N + 1)
back[N] = -1
q = deque()
q.append((N, 0))
time = 0
cur = 1
while True:
    cur, time = q.popleft()
    if cur == 1:
        break
    time += 1
    if cur > 1 and not back[cur - 1]:
        q.append((cur - 1, time))
        back[cur - 1] = cur
    if not cur % 3 and not back[cur // 3]:
        q.append((cur // 3, time))
        back[cur // 3] = cur
    if not cur % 2 and not back[cur // 2]:
        q.append((cur // 2, time))
        back[cur // 2] = cur
print(time)
ans = []
while cur != -1:
    ans.append(cur)
    cur = back[cur]
print(' '.join(map(str, reversed(ans))))
