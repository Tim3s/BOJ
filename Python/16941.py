import sys
from itertools import permutations


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


def intersect(pos1, pos2, pos3, pos4):
    a = cross(pos1, pos2, pos3) * cross(pos1, pos2, pos4)
    b = cross(pos3, pos4, pos1) * cross(pos3, pos4, pos2)
    if a == b == 0:
        return min(pos1[0], pos2[0]) <= max(pos3[0], pos4[0]) and min(pos3[0], pos4[0]) <= max(pos1[0], pos2[0]) and\
            min(pos1[1], pos2[1]) <= max(pos3[1], pos4[1]) and min(pos3[1], pos4[1]) <= max(pos1[1], pos2[1])
    return a <= 0 and b <= 0


def valid(cur):
    for i in range(N):
        for j in range(i + 1, N):
            if intersect(robots[i], vaults[cur[i]], robots[j], vaults[cur[j]]):
                return
    for i in cur:
        print(i + 1)
    sys.exit(0)


N = int(sys.stdin.readline())
check = list(permutations([i for i in range(N)], N))
robots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
vaults = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in check:
    valid(i)
