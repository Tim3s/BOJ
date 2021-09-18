def draw(slist, n, row, column):
    if n == 3:
        slist[row][column] = '*'
        slist[row + 1][column - 1] = '*'
        slist[row + 1][column + 1] = '*'
        for _i in range(-2, 3):
            slist[row + 2][column + _i] = '*'
    else:
        n = n // 2
        draw(slist, n, row, column)
        draw(slist, n, row + n, column - n)
        draw(slist, n, row + n, column + n)
    return slist


N = int(input())
mylist = draw([[' '] * (2 * N - 1) for _ in range(N)], N, 0, N - 1)
for i in range(N):
    print(''.join(mylist[i]))
