import sys


def check(x, y, length):
    global text
    for i in range(x, x + length):
        for j in range(y, y + length):
            if num[i][j] != num[x][y]:
                newlength = length // 2
                text += '('
                check(x, y, newlength)
                check(x, y + newlength, newlength)
                check(x + newlength, y, newlength)
                check(x + newlength, y + newlength, newlength)
                text += ')'
                return
    text += num[x][y]


N = int(sys.stdin.readline())
num = [list(sys.stdin.readline().rstrip()) for j in range(N)]
text = ""
check(0, 0, N)
print(text)