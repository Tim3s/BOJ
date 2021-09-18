import sys


def ccw(pos1, pos2):
    return pos1[0] * pos2[1] - pos1[1] * pos2[0]


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


n = int(sys.stdin.readline())
loc = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
start, end = list(map(lambda x: (int(x) - 1) % n + 1, sys.stdin.readline().split()))
loc.append(loc[0])
check = start < end
if not check:
    start, end = end, start
S = []
for i in range(start, end + 1):
    while len(S) >= 2:
        if cross(loc[S[-2]], loc[S[-1]], loc[i]) < 0:
            break
        S.pop()
    S.append(i if i != n else 0)
print(len(S))
if not check:
    S.reverse()
print(*S)
