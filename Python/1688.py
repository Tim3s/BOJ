import sys


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


def intersect(pos1, pos2, pos3, pos4):
    a = cross(pos1, pos2, pos3) * cross(pos1, pos2, pos4)
    b = cross(pos3, pos4, pos1) * cross(pos3, pos4, pos2)
    if a == b == 0:
        return min(pos1, pos2) <= max(pos3, pos4) and min(pos3, pos4) <= max(pos1, pos2)
    return a <= 0 and b <= 0


N = int(sys.stdin.readline())
barrier = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
friends = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
for i in range(3):
    cnt = 0
    protected = False
    for j in range(N):
        if intersect(friends[i], friends[i], barrier[j - 1], barrier[j]):
            protected = True
            break
        if intersect(friends[i], [-1, friends[i][1] + 1], barrier[j - 1], barrier[j]):
            cnt += 1
    print(1 if protected or cnt % 2 else 0)
