import sys


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


T = int(sys.stdin.readline())
for _ in range(T):
    loc = list(map(int, sys.stdin.readline().split()))
    loc = [loc[1 + (i << 1): 3 + (i << 1)] + [i] for i in range(loc[0])]
    loc.sort()
    S = []
    for i in range(len(loc)):
        while len(S) >= 2:
            if cross(S[-2], S[-1], loc[i]) >= 0:
                break
            S.pop()
        S.append(loc[i])
    for i in range(len(loc) - 2, -1, -1):
        if loc[i] not in S:
            S.append(loc[i])
    print(*[S[i][2] for i in range(len(loc))])
