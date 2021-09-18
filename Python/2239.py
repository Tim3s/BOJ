import sys


def checkvalid(cx, cy, item):
    for i in range(9):
        if num[cx][i] == item or num[i][cy] == item:
            return False
    rcx = cx // 3 * 3
    rcy = cy // 3 * 3
    for i in range(rcx, rcx + 3):
        for j in range(rcy, rcy + 3):
            if num[i][j] == item:
                return False
    return True


def printresult(n):
    global done
    if done:
        return
    if n == len(zero):
        for i in range(9):
            print(''.join(num[i]))
        done = True
        return
    cx, cy = zero[n]
    for item in possibility[n]:
        if checkvalid(cx, cy, item):
            num[cx][cy] = item
            printresult(n + 1)
            num[cx][cy] = 0


num = [list(sys.stdin.readline().rstrip()) for j in range(9)]
zero = [(x, y) for x in range(9) for y in range(9) if num[x][y] == '0']
possibility = [["1", "2", "3", "4", "5", "6", "7", "8", "9"] for i in range(len(zero))]
for i in range(len(zero) - 1, -1, -1):
    x, y = zero[i]
    curp = possibility[i]
    for j in range(9):
        if num[x][j] in curp:
            curp.remove(num[x][j])
        if num[j][y] in curp:
            curp.remove(num[j][y])
    rx = x // 3 * 3
    ry = y // 3 * 3
    for j in range(rx, rx + 3):
        for k in range(ry, ry + 3):
            if num[j][k] in curp:
                curp.remove(num[j][k])
    if len(curp) == 1:
        num[x][y] = curp[0]
        del possibility[i]
        del zero[i]
done = False
printresult(0)
