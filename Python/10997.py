import sys

N = int(sys.stdin.readline())
if N == 1:
    print('*')
    sys.exit(0)
res = [[' '] * (4 * N - 3) for _ in range(4 * N - 1)]
row, col = 2 * N - 2, 2 * N - 2
res[row + 2][col] = res[row + 1][col] = res[row][col] = '*'
rush = 4
for _ in range(N - 1):
    for _ in range(2):
        col += 1
        res[row][col] = '*'
    for _ in range(rush):
        row += 1
        res[row][col] = '*'
    for _ in range(rush):
        col -= 1
        res[row][col] = '*'
    rush += 2
    for _ in range(rush):
        row -= 1
        res[row][col] = '*'
    for _ in range(rush - 2):
        col += 1
        res[row][col] = '*'
    rush += 2
for i in range(4 * N - 1):
    if i != 1:
        print(''.join(res[i]))
    else:
        print('*')
