N = int(input())
center = 2 * N - 2
res = [[' '] * (2 * center + 1) for i in range(2 * center + 1)]
while N > 0:
    x = [center - 2 * N + 2, center + 2 * N - 2]
    for y in range(center - (2 * N - 2), center + 2 * N - 1):
        res[x[0]][y] = '*'
        res[x[1]][y] = '*'
        res[y][x[0]] = '*'
        res[y][x[1]] = '*'
    N -= 1
for i in range(2 * center + 1):
    print(''.join(res[i]))
