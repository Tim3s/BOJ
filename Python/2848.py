import sys
from collections import deque

N = int(sys.stdin.readline())
if N == 0:
    print()
    sys.exit(0)
cur1 = sys.stdin.readline().rstrip()
former = {i: [] for i in cur1}
latter = {i: [] for i in cur1}
for _ in range(N - 1):
    cur2 = sys.stdin.readline().rstrip()
    for i in cur2:
        if i not in former:
            former[i] = []
            latter[i] = []
    for i in range(min(len(cur1), len(cur2))):
        if cur1[i] != cur2[i]:
            latter[cur1[i]].append(cur2[i])
            former[cur2[i]].append(cur1[i])
            break
        if i == min(len(cur1), len(cur2)) - 1:
            if len(cur1) > len(cur2):
                print('!')
                sys.exit(0)
    cur1 = cur2
q = deque()
for key in former:
    if not former[key]:
        q.append(key)
ans = ''
valid = True
while q:
    if len(q) > 1:
        valid = False
    cur = q.popleft()
    ans += cur
    for v in latter[cur]:
        former[v].remove(cur)
        if not former[v]:
            q.append(v)
if len(ans) != len(former):
    print('!')
elif not valid:
    print('?')
else:
    print(ans)
