import sys


def draw(n, row, col):
    if n == 1:
        res[row][col] = '*'
    elif n % 2:
        for _i in range(2 ** n - 2):
            res[row][col - _i] = '*'
            res[row][col + _i] = '*'
            row += 1
        for _i in range(-(2 ** n - 2), 2 ** n - 1):
            res[row][col + _i] = '*'
        draw(n - 1, row - 1, col)
    else:
        for _i in range(2 ** n - 2):
            res[row][col - _i] = '*'
            res[row][col + _i] = '*'
            row -= 1
        for _i in range(-(2 ** n - 2), 2 ** n - 1):
            res[row][col + _i] = '*'
        draw(n - 1, row + 1, col)


N = int(sys.stdin.readline())
res = [[' '] * (2 ** (N + 1) - 3) for _ in range(2 ** N - 1)]
draw(N, 0 if N % 2 else 2 ** N - 2, 2 ** N - 2)
for i in range(2 ** N - 1):
    print(''.join(res[i][:2 ** N - 1 + i if N % 2 else 2 ** (N + 1) - 3 - i]))
