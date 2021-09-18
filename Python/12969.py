import sys


def make(n, a, b, k):
    if n == N:
        if k == K:
            return True
        else:
            return False
    if k > K:
        return False
    if visited[n][a][b][k]:
        return False
    visited[n][a][b][k] = True
    S[n] = 'A'
    if make(n + 1, a + 1, b, k):
        return True
    S[n] = 'B'
    if make(n + 1, a, b + 1, k + a):
        return True
    S[n] = 'C'
    if make(n + 1, a, b, k + a + b):
        return True
    return False


N, K = map(int, sys.stdin.readline().split())
S = [0] * N
visited = [[[[False] * (K + 1) for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
if make(0, 0, 0, 0):
    print(''.join(S))
else:
    print(-1)
