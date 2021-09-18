import sys


def check(x, y, length):
    for i in range(x, x + length):
        for j in range(y, y + length):
            if num[i][j] != num[x][y]:
                newlength = length // 2
                check(x, y, newlength)
                check(x + newlength, y, newlength)
                check(x, y + newlength, newlength)
                check(x + newlength, y + newlength, newlength)
                return
    if num[x][y]:
        global cntb
        cntb += 1
    else:
        global cntw
        cntw += 1


N = int(sys.stdin.readline())
num = [[int(i) for i in input().split()] for j in range(N)]
cntw = 0
cntb = 0
check(0, 0, N)
print(cntw, cntb, sep='\n')