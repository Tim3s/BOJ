import sys

N, K = map(int, input().split())
N //= 2
Catalan = [[1] * i for i in range(1, N + 2)]
for i in range(1, N + 1):
    Catalan[i][0] = sum([Catalan[j][0] * Catalan[i - j - 1][0] for j in range(i)])
    for j in range(i - 1, 0, -1):
        Catalan[i][j] = Catalan[i - 1][j - 1] + Catalan[i][j + 1]
if K >= Catalan[N][0]:
    print(-1)
    sys.exit(0)
x, y = N, 0
while x != 0:
    if x == y or K >= Catalan[x][y + 1]:
        print(')', end='')
        if x != y:
            K -= Catalan[x][y + 1]
        x -= 1
        y -= 1
    else:
        print('(', end='')
        y += 1
