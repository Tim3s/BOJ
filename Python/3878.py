import sys


def dist(pos1, pos2):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2


def cmpb(pos1, pos2):
    res = cross(b[0], pos1, pos2)
    if res == 0:
        return dist(b[0], pos1) < dist(b[0], pos2)
    return res > 0


def mergesortb(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = mergesortb(l[:mid])
    right = mergesortb(l[mid:])
    lidx = 0
    ridx = 0
    res = []
    while lidx != len(left) and ridx != len(right):
        if cmpb(left[lidx], right[ridx]):
            res.append(left[lidx])
            lidx += 1
        else:
            res.append(right[ridx])
            ridx += 1
    return res + left[lidx:] + right[ridx:]


def cmpw(pos1, pos2):
    res = cross(w[0], pos1, pos2)
    if res == 0:
        return dist(w[0], pos1) < dist(w[0], pos2)
    return res > 0


def mergesortw(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = mergesortw(l[:mid])
    right = mergesortw(l[mid:])
    lidx = 0
    ridx = 0
    res = []
    while lidx != len(left) and ridx != len(right):
        if cmpb(left[lidx], right[ridx]):
            res.append(left[lidx])
            lidx += 1
        else:
            res.append(right[ridx])
            ridx += 1
    return res + left[lidx:] + right[ridx:]


def ccw(pos1, pos2):
    res = pos1[0] * pos2[1] - pos1[1] * pos2[0]
    return 1 if res > 0 else (-1 if res < 0 else 0)


def cross(pos1, pos2, pos3):
    return ccw([pos2[0] - pos1[0], pos2[1] - pos1[1]], [pos3[0] - pos2[0], pos3[1] - pos2[1]])


def intersect(pos1, pos2, pos3, pos4):
    x = cross(pos1, pos2, pos3) * cross(pos1, pos2, pos4)
    y = cross(pos3, pos4, pos1) * cross(pos3, pos4, pos2)
    if x <= 0 and y <= 0:
        if (pos1[0] < pos3[0] and pos1[0] < pos4[0] and pos2[0] < pos3[0] and pos2[0] < pos4[0]) or \
                (pos3[0] < pos1[0] and pos3[0] < pos2[0] and pos4[0] < pos1[0] and pos4[0] < pos2[0]):
            return False
        if (pos1[1] < pos3[1] and pos1[1] < pos4[1] and pos2[1] < pos3[1] and pos2[1] < pos4[1]) or \
                (pos3[1] < pos1[1] and pos3[1] < pos2[1] and pos4[1] < pos1[1] and pos4[1] < pos2[1]):
            return False
        return True
    return False


T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    w = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    b.sort(key=lambda x: (x[1], x[0]))
    b = [b[0]] + mergesortb(b[1:])
    w.sort(key=lambda x: (x[1], x[0]))
    w = [w[0]] + mergesortw(w[1:])
    bHull = []
    wHull = []
    bHull.append(0)
    if n > 1:
        bHull.append(1)
    i = 2
    while i < n:
        while len(bHull) >= 2:
            if cross(b[bHull[-2]], b[bHull[-1]], b[i]) > 0:
                break
            bHull.pop()
        bHull.append(i)
        i += 1
    bHull.sort()
    bHull.append(bHull[0])
    wHull.append(0)
    if m > 1:
        wHull.append(1)
    i = 2
    while i < m:
        while len(wHull) >= 2:
            if cross(w[wHull[-2]], w[wHull[-1]], w[i]) > 0:
                break
            wHull.pop()
        wHull.append(i)
        i += 1
    wHull.sort()
    wHull.append(wHull[0])
    # print(bHull, wHull)
    invalid = False
    for i in range(len(bHull) - 1):
        for j in range(len(wHull) - 1):
            if intersect(b[bHull[i]], b[bHull[i + 1]], w[wHull[j]], w[wHull[j + 1]]):
                invalid = True
                break
        if invalid:
            break
    if invalid:
        print('NO')
        continue
    # print(valid1, valid2, valid3)
    invalid = True
    for i in range(len(bHull) - 1):
        for j in range(len(wHull) - 1):
            if cross(b[bHull[i]], b[bHull[i + 1]], w[wHull[j]]) <= 0:
                invalid = False
                break
        if not invalid:
            break
    if invalid:
        print('NO')
        continue
    invalid = True
    for i in range(len(wHull) - 1):
        for j in range(len(bHull) - 1):
            if cross(w[wHull[i]], w[wHull[i + 1]], b[bHull[j]]) <= 0:
                invalid = False
                break
        if not invalid:
            break
    if invalid:
        print('NO')
        continue
    print('YES')
