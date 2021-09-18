import sys


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


N, Px, Py = map(int, sys.stdin.readline().split())
P = [Px, Py]
wall = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
wall.sort()
cnt = 0
while True:
    S = []
    for i in range(len(wall)):
        while len(S) >= 2:
            if cross(wall[S[-2]], wall[S[-1]], wall[i]) >= 0:
                break
            S.pop()
        S.append(i)
    for i in range(len(wall) - 2, -1, -1):
        while len(S) >= 2:
            if cross(wall[S[-2]], wall[S[-1]], wall[i]) >= 0:
                break
            S.pop()
        S.append(i)
    for i in range(len(S) - 1):
        if cross(wall[S[i]], wall[S[i + 1]], P) < 0:
            print(cnt)
            sys.exit(0)
    S.pop()
    S.sort(reverse=True)
    for i in S:
        del wall[i]
    cnt += 1
    if len(wall) <= 2:
        print(cnt)
        sys.exit(0)
