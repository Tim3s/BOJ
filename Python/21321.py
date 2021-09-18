import sys


def dp(seq, bits, res):
    global ans
    if seq == N + 1:
        ans = max(ans, res)
        return
    idx = -1
    cur = sys.maxsize
    for i in range(N):
        if not bits & 1 << i and not blind[i]:
            if not blinding[i]:
                if clay[i][1] < cur:
                    idx = i
                    cur = clay[i][1]
                continue
            for j in blinding[i]:
                blind[j] -= 1
            dp(seq + 1, bits | 1 << i, res + seq * clay[i][1])
            for j in blinding[i]:
                blind[j] += 1
    if idx != -1:
        dp(seq + 1, bits | 1 << idx, res + seq * clay[idx][1])


N = int(sys.stdin.readline())
clay = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
blind = [0] * N
blinding = [[] for _ in range(N)]
for i in range(N - 1):
    for j in range(i + 1, N):
        if not clay[j][0] % clay[i][0]:
            blind[j] += 1
            blinding[i].append(j)
ans = 0
# visited = [False] * N
# for i in range(1, N + 1):
#     cur = sys.maxsize
#     idx = -1
#     for j in range(len(blind)):
#         if not visited[j] and not blind[j] and cur > clay[j][1]:
#             cur = clay[j][1]
#             idx = j
#     ans += i * cur
#     visited[idx] = True
#     print(idx)
#     for j in blinding[idx]:
#         if idx in blind[j]:
#             blind[j].remove(idx)
# print(ans)
dp(1, 0, 0)
print(ans)
