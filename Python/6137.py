import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque([sys.stdin.readline().rstrip() for i in range(N)])
res = ""
for i in range(N):
    left = 0
    right = len(d) - 1
    same = True
    while left < right:
        if d[left] != d[right]:
            res += d.popleft() if d[left] < d[right] else d.pop()
            same = False
            break
        left += 1
        right -= 1
    if same:
        res += d.pop()
for i in range(N):
    if i != 0 and i % 80 == 0:
        print('\n', end='')
    print(res[i], end='')
