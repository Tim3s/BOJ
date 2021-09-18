import sys
import copy

N = int(sys.stdin.readline())
first = [0] + list(map(int, list(sys.stdin.readline().rstrip())))
last = [0] + list(map(int, list(sys.stdin.readline().rstrip())))
rotate = [[100000] * 10 for _ in range(N + 1)]
memo = [[-1] * 10 for _ in range(N + 1)]
for i in range(10):
    rotate[0][i] = i
for i in range(1, N + 1):
    for j in range(10):
        left = (last[i] - first[i] - j) % 10
        right = (-left) % 10
        if rotate[i][j] > rotate[i - 1][j] + right:
            rotate[i][j] = rotate[i - 1][j] + right
            memo[i][j] = j
        if rotate[i][(j + left) % 10] > rotate[i - 1][j] + left:
            rotate[i][(j + left) % 10] = rotate[i - 1][j] + left
            memo[i][(j + left) % 10] = j
ans = min(rotate[-1])
print(ans)
idx = rotate[-1].index(ans)
cur = []
for i in range(N, 0, -1):
    if memo[i][idx] == idx:
        cur.append(-(rotate[i][idx] - rotate[i-1][idx]))
    else:
        cur.append(rotate[i][idx] - rotate[i-1][memo[i][idx]])
    idx = memo[i][idx]
cur.reverse()
for i in range(1, N + 1):
    if cur[i - 1]:
        print(i, cur[i - 1])
