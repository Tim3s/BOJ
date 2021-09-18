import sys
import copy


def calc(operator, former, latter):
    if operator == 0:
        return former + latter
    if operator == 1:
        return former - latter
    if operator == 2:
        return former * latter
    if former < 0:
        return -((-former) // latter)
    else:
        return former // latter



N = int(sys.stdin.readline())
A = [int(i) for i in sys.stdin.readline().split()]
op = [[int(i) for i in sys.stdin.readline().split()]]
num = [A[0]]
for i in range(N - 1):
    curop = []
    curnum = []
    for j in range(len(num)):
        for k in range(4):
            if op[j][k] != 0 and not (k == 3 and A[i + 1] == 0):
                curnum.append(calc(k, num[j], A[i + 1]))
                curop.append(copy.deepcopy(op[j]))
                curop[-1][k] -= 1
    op = curop
    num = curnum
print(max(num))
print(min(num))
