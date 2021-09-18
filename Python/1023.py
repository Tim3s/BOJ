import sys

N, K = map(int, input().split())
if N % 2:
    ans = []
    if K >= 2 ** N:
        print(-1)
        sys.exit(0)
    while K > 0:
        if K % 2:
            ans.append(')')
        else:
            ans.append('(')
        K //= 2
    print('(' * (N - len(ans)) + ''.join(reversed(ans)))
    sys.exit(0)
pair = N // 2
Catalan = [[1] * i for i in range(2, pair + 3)]
Catalan[0][1] = 0
for i in range(1, pair + 1):
    Catalan[i][0] = sum([Catalan[j][0] * Catalan[i - j - 1][0] for j in range(i)])
    Catalan[i][-1] = 0
    for j in range(i - 1, 0, -1):
        Catalan[i][j] = Catalan[i - 1][j - 1] + Catalan[i][j + 1]
if K >= 2 ** N - Catalan[pair][0]:
    print(-1)
    sys.exit(0)
x, y = pair, 0
while N > 0:
    if 2 ** (N - 1) - Catalan[x][y + 1] <= K:
        print(')', end='')
        K -= 2 ** (N - 1) - Catalan[x][y + 1]
        x -= 1
        y -= 1
    else:
        print('(', end='')
        y += 1
    N -= 1
    if x < 0 or y > x or y < 0:
        break
while N > 0:
    if 2 ** (N - 1) <= K:
        print(')', end='')
        K -= 2 ** (N - 1)
    else:
        print('(', end='')
    N -= 1
