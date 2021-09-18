import sys


def check(x, y, length):
    for i in range(x, x + length):
        for j in range(y, y + length):
            if num[i][j] != num[x][y]:
                newlength = length // 3
                check(x, y, newlength)
                check(x, y + newlength, newlength)
                check(x, y + 2 * newlength, newlength)
                check(x + newlength, y, newlength)
                check(x + newlength, y + newlength, newlength)
                check(x + newlength, y + 2 * newlength, newlength)
                check(x + 2 * newlength, y, newlength)
                check(x + 2 * newlength, y + newlength, newlength)
                check(x + 2 * newlength, y + 2 * newlength, newlength)
                return
    res[num[x][y] + 1] += 1


N = int(sys.stdin.readline())
num = [[int(i) for i in sys.stdin.readline().split()] for j in range(N)]
res = [0] * 3
check(0, 0, N)
print(res[0], res[1], res[2], sep='\n')
