import sys


N, M, K, S, T = map(int, sys.stdin.readline().split())
forward = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    forward[a].append([b, t])
memo = [[-1] * (K + 1) for _ in range(N + 1)]
memo[S][0] = 0
for i in range(S, N + 1):
    if memo[i][0] != -1:
        for j, k in forward[i]:
            memo[j][0] = max(memo[j][0], memo[i][0] + k)
for cnt in range(1, K + 1):
    for up in range(1, N + 1):
        for i, _ in forward[up]:
            if not (memo[up][cnt] != -1 and memo[up][cnt] > memo[i][cnt - 1]) and memo[i][cnt - 1] != -1:
                memo[up][cnt] = memo[i][cnt - 1]
        if memo[up][cnt] != -1:
            for j, k in forward[up]:
                # print(j, k)
                # print(memo[up][cnt])
                memo[j][cnt] = max(memo[j][cnt], memo[up][cnt] + k)
print(memo[T][K])
# print(memo)
