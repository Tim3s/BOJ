import math
import sys


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


P = int(sys.stdin.readline())
for _ in range(P):
    N = int(sys.stdin.readline())
    loc = []
    for _ in range(math.ceil(N / 5)):
        tmp = list(map(int, sys.stdin.readline().split()))
        loc += [tmp[i:i + 2] for i in range(0, len(tmp), 2)]
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
    ans = S1 + S2[1:-1]
    ans.reverse()
    ymax = -100
    xmin = 100
    idx = -1
    for i in range(-len(ans), 0):
        if ans[i][1] > ymax or (ans[i][1] == ymax and ans[i][0] < xmin):
            ymax = ans[i][1]
            xmin = ans[i][0]
            idx = i
    print(len(ans))
    for i in range(idx, idx + len(ans)):
        print(*ans[i])
