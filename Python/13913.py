import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
time = 0
back = [-2] * 100001
back[N] = -1
q = deque()
q.append((N, time))
while True:
    cur, time = q.popleft()
    if cur == K:
        break
    time += 1
    if cur > 0 and back[cur - 1] == -2:
        back[cur - 1] = cur
        q.append((cur - 1, time))
    if cur < 100000 and back[cur + 1] == -2:
        back[cur + 1] = cur
        q.append((cur + 1, time))
    if cur <= 50000 and back[cur * 2] == -2:
        back[cur * 2] = cur
        q.append((cur * 2, time))
print(time)
cur = K
ans = []
while cur != -1:
    ans.append(cur)
    cur = back[cur]
print(' '.join(map(str, reversed(ans))))
