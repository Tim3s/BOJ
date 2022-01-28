import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    s = deque(list(map(lambda x: ord(x) - 97, list(sys.stdin.readline().rstrip()))))
    alpha = True
    start = len(s) - 1
    while len(s) > 1:
        if s[0] == start:
            s.popleft()
        elif s[-1] == start:
            s.pop()
        else:
            alpha = False
            break
        start -= 1
    if alpha and not s[0]:
        print('YES')
    else:
        print('NO')
