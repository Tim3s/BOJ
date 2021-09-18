import sys


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


def intersect(pos1, pos2, pos3, pos4):
    a = cross(pos1, pos2, pos3) * cross(pos1, pos2, pos4)
    b = cross(pos3, pos4, pos1) * cross(pos3, pos4, pos2)
    return a < 0 and b < 0


l = list(map(int, sys.stdin.readline().split()))
print(1 if intersect(l[:2], l[2:4], l[4:6], l[6:]) else 0)
