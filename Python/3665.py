import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    t = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    higher = [[] for _ in range(n)]
    lower = [[] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            higher[t[j]].append(t[i])
            lower[t[i]].append(t[j])
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, sys.stdin.readline().split())
        if b in higher[a]:
            higher[b].append(a)
            lower[a].append(b)
            higher[a].remove(b)
            lower[b].remove(a)
        else:
            higher[a].append(b)
            lower[b].append(a)
            higher[b].remove(a)
            lower[a].remove(b)
    q = deque()
    for i in range(n):
        if not higher[i]:
            q.append(i)
    valid = True
    ans = []
    while q:
        if len(q) > 1:
            valid = False
            break
        cur = q.popleft()
        ans.append(cur + 1)
        for v in lower[cur]:
            higher[v].remove(cur)
            if not higher[v]:
                q.append(v)
    if not valid:
        print('?')
    elif len(ans) == n:
        print(*ans)
    else:
        print('IMPOSSIBLE')
