import sys

N = int(sys.stdin.readline())
game = [0] * (N + 1)
for i in range(10, N + 1):
    cur = str(i)
    L = len(cur)
    for j in range(L):
        for k in range(j + 1, L + 1):
            if j == 0 and k == L:
                continue
            tmp = int(cur[j:k])
            if tmp != 0 and not game[i - tmp]:
                if not (game[i] and game[i] < tmp):
                    game[i] = tmp
print(game[N] if game[N] else -1)
