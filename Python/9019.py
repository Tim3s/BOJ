import sys
from collections import deque

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    q = deque([(A, '')])
    visited = [False] * 10000
    visited[A] = True
    while True:
        A, op = q.popleft()
        D = 2 * A % 10000
        S = (A - 1) % 10000
        L = A * 10 % 10000 + A // 1000
        R = A // 10 + A % 10 * 1000
        if not visited[D]:
            if D == B:
                print(op + 'D')
                break
            visited[D] = True
            q.append((D, op + 'D'))
        if not visited[S]:
            if S == B:
                print(op + 'S')
                break
            visited[S] = True
            q.append((S, op + 'S'))
        if not visited[L]:
            if L == B:
                print(op + 'L')
                break
            visited[L] = True
            q.append((L, op + 'L'))
        if not visited[R]:
            if R == B:
                print(op + 'R')
                break
            visited[R] = True
            q.append((R, op + 'R'))
