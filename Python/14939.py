import sys
import copy


def click(x, y):
    tmp[x][y] = not tmp[x][y]
    if x > 0:
        tmp[x - 1][y] = not tmp[x - 1][y]
    if x < 9:
        tmp[x + 1][y] = not tmp[x + 1][y]
    if y > 0:
        tmp[x][y - 1] = not tmp[x][y - 1]
    if y < 9:
        tmp[x][y + 1] = not tmp[x][y + 1]


def check():
    for _i in range(10):
        if tmp[9][_i]:
            return False
    return True


light = [list(map(lambda x: x != '#', list(sys.stdin.readline().rstrip()))) for _ in range(10)]
ans = -1
for i in range(1 << 10):
    cnt = 0
    tmp = copy.deepcopy(light)
    for j in range(10):
        if i & 1 << j:
            click(0, j)
            cnt += 1
    for j in range(1, 10):
        for k in range(10):
            if tmp[j - 1][k]:
                click(j, k)
                cnt += 1
    if check():
        ans = max(ans, cnt)
print(ans)
