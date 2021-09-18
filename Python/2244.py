import sys


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
loc = [[A[i][0] + B[j][0], A[i][1] + B[j][1]] for i in range(N) for j in range(M)]
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
res = S1 + S2[1:-1]
print(len(res))
for i in res:
    print(*i)
