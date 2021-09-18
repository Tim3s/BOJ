def draw(slist, n, row, column):
    if n == 1:
        slist[row][column] = '*'
    else:
        n = int(n / 3)
        draw(slist, n, row, column)
        draw(slist, n, row + n, column)
        draw(slist, n, row + 2 * n, column)
        draw(slist, n, row, column + n)
        draw(slist, n, row + 2 * n, column + n)
        draw(slist, n, row, column + 2 * n)
        draw(slist, n, row + n, column + 2 * n)
        draw(slist, n, row + 2 * n, column + 2 * n)
    return slist


N = int(input())
mylist = draw([[' '] * N for i in range(N)], N, 0, 0)
for i in range(N):
    print(''.join(mylist[i]))
