import sys


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


N = int(sys.stdin.readline())
wall = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
wall.sort()
S = []
for i in range(len(wall)):
    while len(S) >= 2:
        if cross(wall[S[-2]], wall[S[-1]], wall[i]) > 0:
            break
        S.pop()
    S.append(i)
S2 = []
for i in range(len(wall) - 1, -1, -1):
    while len(S2) >= 2:
        if cross(wall[S2[-2]], wall[S2[-1]], wall[i]) > 0:
            break
        S2.pop()
    S2.append(i)
print(len(S + S2) - 2)
