import math
import sys


def dist(pos1, pos2, pos3):
    a = -(pos2[1] - pos1[1])
    b = pos2[0] - pos1[0]
    c = -(pos1[0] * a + pos1[1] * b)
    return abs(a * pos3[0] + b * pos3[1] + c) / math.sqrt(a ** 2 + b ** 2)


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


idx = 0
while True:
    idx += 1
    N = int(sys.stdin.readline())
    if not N:
        break
    loc = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    loc.sort()
    S1 = []
    for i in range(len(loc)):
        while len(S1) >= 2:
            if cross(S1[-2], S1[-1], loc[i]) > 0:
                break
            S1.pop()
        S1.append(loc[i])
    S2 = []
    for i in range(len(loc) - 1, -1, -1):
        while len(S2) >= 2:
            if cross(S2[-2], S2[-1], loc[i]) > 0:
                break
            S2.pop()
        S2.append(loc[i])
    res = S1 + S2[1:]
    ans = sys.maxsize
    for i in range(len(res) - 1):
        ans = min(ans, max([dist(res[i], res[i + 1], res[j]) for j in range(len(res) - 1) if i != j and i + 1 != j]))
    print("Case ", idx, ": ", format(math.ceil(ans * 100) / 100, '.2f'), sep='')
